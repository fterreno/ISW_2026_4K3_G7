from pathlib import Path

from fpdf import FPDF
from fpdf.fonts import FontFace

from assets.style import tema
from assets.style.formato_moneda_peso import formatear_monto
from entities.factura import Factura

CARPETA_ASSETS = Path(__file__).resolve().parent.parent / "assets"


def hex_a_rgb(color: str) -> tuple[int, int, int]:
    return tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))


class FacturaPDF:
    """Dibuja la factura en un PDF A4 con el logo, la fuente Lato y la paleta del parque."""

    def __init__(self, factura: Factura):
        self.factura = factura
        self.pdf = FPDF(format="A4")

    def generar(self) -> bytes:
        self.preparar_documento()
        self.dibujar_encabezado()
        self.dibujar_cliente()
        self.dibujar_detalle()
        self.dibujar_totales()
        self.dibujar_pie()
        return bytes(self.pdf.output())

    def preparar_documento(self) -> None:
        self.pdf.set_title(f"Factura {self.factura.numero}")
        self.pdf.set_author(self.factura.nombre_parque)
        self.pdf.add_font("Lato", "", CARPETA_ASSETS / "fonts" / "Lato-Regular.ttf")
        self.pdf.add_font("Lato", "B", CARPETA_ASSETS / "fonts" / "Lato-Bold.ttf")
        self.usar_color(tema.TEXTO)
        self.pdf.add_page()

    def dibujar_encabezado(self) -> None:
        """Logo y nombre del parque a la izquierda; número y fecha de la factura a la derecha."""
        pdf = self.pdf
        pdf.image(CARPETA_ASSETS / "images" / "image.png", x=pdf.l_margin, y=pdf.t_margin, h=22)
        pdf.set_font("Lato", "B", 22)
        pdf.set_xy(pdf.l_margin + 28, pdf.t_margin + 2)
        self.usar_color(tema.VERDE_OSCURO)
        pdf.cell(text=self.factura.nombre_parque)
        pdf.set_font("Lato", "B", 16)
        pdf.set_xy(pdf.l_margin, pdf.t_margin + 2)
        pdf.cell(w=pdf.epw, text="FACTURA", align="R")
        pdf.set_font("Lato", "", 10)
        self.usar_color(tema.TEXTO)
        pdf.set_xy(pdf.l_margin, pdf.t_margin + 11)
        pdf.multi_cell(w=pdf.epw, align="R",
                       text=f"N° {self.factura.numero}\nFecha de emisión: {self.factura.fecha_emision:%d/%m/%Y}")

        pdf.set_y(pdf.t_margin + 30)
        pdf.set_draw_color(*hex_a_rgb(tema.VERDE_CLARO))
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.l_margin + pdf.epw, pdf.get_y())
        pdf.ln(5)

    def dibujar_cliente(self) -> None:
        usuario, entrada = self.factura.usuario, self.factura.entrada
        self.pdf.set_font("Lato", "B", 11)
        self.pdf.cell(text="Datos del cliente", new_x="LMARGIN", new_y="NEXT")
        self.pdf.set_font("Lato", "", 10)
        self.pdf.multi_cell(w=self.pdf.epw, text=(
            f"{usuario.apellido} {usuario.nombre}\n"
            f"{usuario.mail}\n"
            f"Fecha de visita: {entrada.fecha_entrada:%d/%m/%Y}   ·   "
            f"Tipo de pase: {entrada.tipo_pase.value}   ·   "
            f"Forma de pago: {entrada.forma_pago.value}"
        ))
        self.pdf.ln(5)

    def dibujar_detalle(self) -> None:
        """Una fila por visitante con el precio del pase, el descuento por edad y lo que paga."""
        self.pdf.set_draw_color(*hex_a_rgb(tema.VERDE_CLARO))
        encabezado = FontFace(emphasis="BOLD", color=hex_a_rgb(tema.CREMA), fill_color=hex_a_rgb(tema.VERDE_OSCURO))
        with self.pdf.table(col_widths=(10, 15, 25, 25, 25), text_align=("CENTER", "CENTER", "RIGHT", "RIGHT", "RIGHT"),
                            headings_style=encabezado, cell_fill_color=hex_a_rgb(tema.CREMA_CLARO), cell_fill_mode="ROWS",
                            line_height=7, borders_layout="HORIZONTAL_LINES") as tabla:
            tabla.row(["N°", "Edad", "Precio", "Descuento", "Subtotal"])
            for linea in self.factura.lineas:
                tabla.row([str(linea.visitante), str(linea.edad), formatear_monto(linea.precio_unitario),
                           f"- {formatear_monto(linea.descuento)}", formatear_monto(linea.subtotal)])
        self.pdf.ln(4)

    def dibujar_totales(self) -> None:
        self.dibujar_total("Subtotal", formatear_monto(self.factura.subtotal))
        self.dibujar_total("Descuentos", f"- {formatear_monto(self.factura.descuentos)}")
        self.usar_color(tema.VERDE_OSCURO)
        self.dibujar_total("Total", formatear_monto(self.factura.total), destacado=True)
        self.usar_color(tema.TEXTO)

    def dibujar_total(self, etiqueta: str, valor: str, destacado: bool = False) -> None:
        """Una fila de totales alineada a la derecha; el total final va más grande y en negrita."""
        self.pdf.set_font("Lato", "B" if destacado else "", 13 if destacado else 10)
        self.pdf.cell(w=self.pdf.epw - 40, h=7, text=etiqueta, align="R")
        self.pdf.cell(w=40, h=7, text=valor, align="R", new_x="LMARGIN", new_y="NEXT")

    def dibujar_pie(self) -> None:
        self.pdf.ln(10)
        self.pdf.set_font("Lato", "", 9)
        self.usar_color(tema.VERDE)
        self.pdf.multi_cell(w=self.pdf.epw, align="C", text=f"Gracias por elegir {self.factura.nombre_parque}. "
                            "Presentá este comprobante junto con tu documento al ingresar al parque.")

    def usar_color(self, color: str) -> None:
        self.pdf.set_text_color(*hex_a_rgb(color))
