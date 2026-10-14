import uuid
from dataclasses import dataclass
from datetime import date, datetime
from html import escape
from pathlib import Path

from fpdf import FPDF
from fpdf.fonts import FontFace

from entities.entrada import Entrada
from entities.usuario import Usuario

# misma paleta y fuente que la aplicación (assets/style/tema.py), copiada acá para no depender de flet
VERDE_OSCURO = "#386641"
VERDE = "#6A994E"
VERDE_CLARO = "#A7C957"
CREMA = "#F2E8CF"
CREMA_CLARO = "#FAF6EA"
TEXTO = "#1F3324"
CARPETA_ASSETS = Path(__file__).resolve().parent.parent / "assets"

# el mail va sin colores: tablas simples con borde fino y la fuente Lato
FUENTE_MAIL = "font-family: Lato, Arial, sans-serif;"
# Lato desde Google Fonts para los clientes de mail que cargan fuentes web (Apple Mail, iOS); el resto usa Arial
LINK_FUENTE_MAIL = '<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">'
CELDA_MAIL = "padding: 6px 8px; border: 1px solid #000000; text-align: left;"
MONTO_MAIL = "text-align: right; white-space: nowrap;"

# estilos del mail para celulares: los clientes de mail que soportan media queries (Gmail, Apple Mail) los aplican
# y pisan los estilos en línea con !important; los que no, muestran la versión de escritorio
ESTILOS_MAIL = """
    body, table, td, th { font-family: Lato, Arial, sans-serif; }
    @media only screen and (max-width: 600px) {
        .contenedor-mail { padding: 8px !important; }
        .contenedor-mail h1 { font-size: 24px !important; }
        .tabla-mail th, .tabla-mail td { padding: 4px 6px !important; font-size: 14px !important; }
        .ocultar-mobile { display: none !important; }
        .solo-mobile { display: block !important; max-height: none !important; overflow: visible !important; }
    }
"""
# lo que solo se ve en el celular: oculto por defecto (mso-hide es para Outlook de escritorio)
SOLO_MOBILE = "display: none; max-height: 0; overflow: hidden; mso-hide: all; font-size: 13px;"


def formatear_monto(monto: float) -> str:
    """Formato de moneda argentino: $ 20.000,00"""
    return "$ " + f"{monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def hex_a_rgb(color: str) -> tuple[int, int, int]:
    return tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))


@dataclass
class LineaFactura:
    """Lo que paga un visitante: el precio del pase y el descuento según su edad."""
    visitante: int
    edad: int
    precio_unitario: float
    descuento: float  # en pesos
    subtotal: float


@dataclass
class Factura:
    numero: str
    fecha_emision: date
    usuario: Usuario
    entrada: Entrada
    nombre_parque: str

    @classmethod
    def emitir(cls, usuario: Usuario, entrada: Entrada, nombre_parque: str, ahora: datetime) -> "Factura":
        numero = f"{ahora:%Y%m%d}-{uuid.uuid4().hex[:6].upper()}"
        return cls(numero, ahora.date(), usuario, entrada, nombre_parque)

    @property
    def lineas(self) -> list[LineaFactura]:
        lineas = []
        precio = self.entrada.tipo_pase.monto_entrada()
        for visitante, edad in enumerate(self.entrada.edades, start=1):
            subtotal = self.entrada.monto_por_edad(edad)
            lineas.append(LineaFactura(visitante, edad, precio, precio - subtotal, subtotal))
        return lineas

    @property
    def subtotal(self) -> float:
        return sum(linea.precio_unitario for linea in self.lineas)

    @property
    def descuentos(self) -> float:
        return sum(linea.descuento for linea in self.lineas)

    @property
    def total(self) -> float:
        return sum(linea.subtotal for linea in self.lineas)

    @property
    def nombre_archivo(self) -> str:
        return f"factura-{self.numero}.pdf"

    def generar_html(self) -> str:
        """La factura para el mail: los datos y una tabla simple sin colores, con estilos en línea,
        que es lo que respetan los clientes de mail.
        En el celular se oculta la columna Precio y se muestra debajo del concepto (ver ESTILOS_MAIL)."""
        filas = "".join(f"""
                <tr>
                    <td style="{CELDA_MAIL}">
                        <span class="ocultar-mobile">Entrada {escape(self.entrada.tipo_pase.value)} - </span>Visitante {linea.visitante} <span style="white-space: nowrap;">({linea.edad} años)</span>
                        <div class="solo-mobile" style="{SOLO_MOBILE}">Entrada {escape(self.entrada.tipo_pase.value)}: <span style="white-space: nowrap;">{formatear_monto(linea.precio_unitario)}</span></div>
                    </td>
                    <td class="ocultar-mobile" style="{CELDA_MAIL} {MONTO_MAIL}">{formatear_monto(linea.precio_unitario)}</td>
                    <td style="{CELDA_MAIL} {MONTO_MAIL}">- {formatear_monto(linea.descuento)}</td>
                    <td style="{CELDA_MAIL} {MONTO_MAIL}">{formatear_monto(linea.subtotal)}</td>
                </tr>""" for linea in self.lineas)
        return f"""
            <h2 style="{FUENTE_MAIL}">Factura</h2>
            <p style="{FUENTE_MAIL}">
                N° {self.numero}<br>
                Fecha de emisión: {self.fecha_emision:%d/%m/%Y}<br>
                {escape(self.nombre_parque)}<br>
                Cliente: {escape(self.usuario.apellido)} {escape(self.usuario.nombre)}<br>
                Mail: <span style="word-break: break-all;">{escape(self.usuario.mail)}</span><br>
                Forma de pago: {self.entrada.forma_pago.value}
            </p>
            <table class="tabla-mail" style="width: 100%; border-collapse: collapse; {FUENTE_MAIL}">
                <tr>
                    <th style="{CELDA_MAIL}">Concepto</th>
                    <th class="ocultar-mobile" style="{CELDA_MAIL} {MONTO_MAIL}">Precio</th>
                    <th style="{CELDA_MAIL} {MONTO_MAIL}">Descuento</th>
                    <th style="{CELDA_MAIL} {MONTO_MAIL}">Subtotal</th>
                </tr>{filas}
            </table>
            <!-- los totales van en otra tabla: con la columna Precio oculta, un colspan desarmaría la grilla -->
            <table class="tabla-mail" style="width: 100%; border-collapse: collapse; margin-top: 8px; {FUENTE_MAIL}">
                <tr>
                    <td style="padding: 4px 8px; {MONTO_MAIL}">Subtotal</td>
                    <td style="padding: 4px 8px; {MONTO_MAIL} width: 1%;">{formatear_monto(self.subtotal)}</td>
                </tr>
                <tr>
                    <td style="padding: 4px 8px; {MONTO_MAIL}">Descuentos</td>
                    <td style="padding: 4px 8px; {MONTO_MAIL} width: 1%;">- {formatear_monto(self.descuentos)}</td>
                </tr>
                <tr>
                    <td style="padding: 4px 8px; {MONTO_MAIL} font-weight: bold;">Total</td>
                    <td style="padding: 4px 8px; {MONTO_MAIL} width: 1%; font-weight: bold;">{formatear_monto(self.total)}</td>
                </tr>
            </table>
        """

    def generar_pdf(self) -> bytes:
        pdf = FPDF(format="A4")
        pdf.set_title(f"Factura {self.numero}")
        pdf.set_author(self.nombre_parque)
        pdf.add_font("Lato", "", CARPETA_ASSETS / "fonts" / "Lato-Regular.ttf")
        pdf.add_font("Lato", "B", CARPETA_ASSETS / "fonts" / "Lato-Bold.ttf")
        pdf.set_text_color(*hex_a_rgb(TEXTO))
        pdf.add_page()

        # encabezado: logo, nombre del parque y datos de la factura
        pdf.image(CARPETA_ASSETS / "images" / "image.png", x=pdf.l_margin, y=pdf.t_margin, h=22)
        pdf.set_font("Lato", "B", 22)
        pdf.set_xy(pdf.l_margin + 28, pdf.t_margin + 2)
        pdf.set_text_color(*hex_a_rgb(VERDE_OSCURO))
        pdf.cell(text=self.nombre_parque)
        pdf.set_font("Lato", "B", 16)
        pdf.set_xy(pdf.l_margin, pdf.t_margin + 2)
        pdf.cell(w=pdf.epw, text="FACTURA", align="R")
        pdf.set_font("Lato", "", 10)
        pdf.set_text_color(*hex_a_rgb(TEXTO))
        pdf.set_xy(pdf.l_margin, pdf.t_margin + 11)
        pdf.multi_cell(w=pdf.epw, text=f"N° {self.numero}\nFecha de emisión: {self.fecha_emision:%d/%m/%Y}", align="R")

        pdf.set_y(pdf.t_margin + 30)
        pdf.set_draw_color(*hex_a_rgb(VERDE_CLARO))
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.l_margin + pdf.epw, pdf.get_y())
        pdf.ln(5)

        # datos del cliente y de la visita
        pdf.set_font("Lato", "B", 11)
        pdf.cell(text="Datos del cliente", new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Lato", "", 10)
        pdf.multi_cell(w=pdf.epw, text=(
            f"{self.usuario.apellido} {self.usuario.nombre}\n"
            f"{self.usuario.mail}\n"
            f"Fecha de visita: {self.entrada.fecha_entrada:%d/%m/%Y}   ·   "
            f"Tipo de pase: {self.entrada.tipo_pase.value}   ·   "
            f"Forma de pago: {self.entrada.forma_pago.value}"
        ))
        pdf.ln(5)

        # detalle de las entradas
        pdf.set_draw_color(*hex_a_rgb(VERDE_CLARO))
        encabezado = FontFace(emphasis="BOLD", color=hex_a_rgb(CREMA), fill_color=hex_a_rgb(VERDE_OSCURO))
        with pdf.table(col_widths=(10, 15, 25, 25, 25), text_align=("CENTER", "CENTER", "RIGHT", "RIGHT", "RIGHT"),
                       headings_style=encabezado, cell_fill_color=hex_a_rgb(CREMA_CLARO), cell_fill_mode="ROWS",
                       line_height=7, borders_layout="HORIZONTAL_LINES") as tabla:
            tabla.row(["N°", "Edad", "Precio", "Descuento", "Subtotal"])
            for linea in self.lineas:
                tabla.row([str(linea.visitante), str(linea.edad), formatear_monto(linea.precio_unitario),
                           f"- {formatear_monto(linea.descuento)}", formatear_monto(linea.subtotal)])
        pdf.ln(4)

        # totales alineados a la derecha
        for etiqueta, valor, negrita in (("Subtotal", formatear_monto(self.subtotal), False),
                                         ("Descuentos", f"- {formatear_monto(self.descuentos)}", False),
                                         ("Total", formatear_monto(self.total), True)):
            pdf.set_font("Lato", "B" if negrita else "", 13 if negrita else 10)
            if negrita:
                pdf.set_text_color(*hex_a_rgb(VERDE_OSCURO))
            pdf.cell(w=pdf.epw - 40, h=7, text=etiqueta, align="R")
            pdf.cell(w=40, h=7, text=valor, align="R", new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(*hex_a_rgb(TEXTO))

        pdf.ln(10)
        pdf.set_font("Lato", "", 9)
        pdf.set_text_color(*hex_a_rgb(VERDE))
        pdf.multi_cell(w=pdf.epw, align="C", text=f"Gracias por elegir {self.nombre_parque}. "
                       "Presentá este comprobante junto con tu documento al ingresar al parque.")
        return bytes(pdf.output())
