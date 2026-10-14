from email.message import EmailMessage
from html import escape

from boundaries.factura_pdf import FacturaPDF
from assets.style.formato_moneda_peso import formatear_monto
from entities.factura import Factura
from entities.forma_pago import FormaPago

# el mail va sin colores: tablas simples con borde fino y la fuente Lato
FUENTE = "font-family: Lato, Arial, sans-serif;"
# Lato desde Google Fonts para los clientes de mail que cargan fuentes web (Apple Mail, iOS); el resto usa Arial
LINK_FUENTE = '<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">'
CELDA = "padding: 6px 8px; border: 1px solid #000000; text-align: left;"
MONTO = "text-align: right; white-space: nowrap;"
TOTAL = f"padding: 4px 8px; {MONTO}"

# estilos para celulares: los clientes de mail que soportan media queries (Gmail, Apple Mail) los aplican
# y pisan los estilos en línea con !important; los que no, muestran la versión de escritorio
ESTILOS = """
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

AVISO_EFECTIVO = ("Se informa que al haber seleccionado la modalidad de pago en efectivo, deberá abonar el importe total "
                  "correspondiente a su reserva al momento de ingresar al parque. En caso de no efectuarse el pago, "
                  "el parque se reserva el derecho de admisión del visitante.")


class MailConfirmacion:
    """Arma el mail de confirmación de la compra: el detalle de las entradas, la factura y la factura en PDF adjunta."""

    def __init__(self, factura: Factura):
        self.factura = factura
        self.usuario = factura.usuario
        self.entrada = factura.entrada
        self.nombre_parque = factura.nombre_parque

    def generar(self) -> EmailMessage:
        mensaje = EmailMessage()
        mensaje['Subject'] = f'{self.nombre_parque}: Compra Confirmada'
        mensaje['To'] = self.usuario.mail
        mensaje.add_alternative(self.generar_html(), subtype='html')
        mensaje.add_attachment(FacturaPDF(self.factura).generar(), maintype='application', subtype='pdf',
                               filename=self.factura.nombre_archivo)
        return mensaje

    def generar_html(self) -> str:
        nombre = escape(self.usuario.nombre)
        apellido = escape(self.usuario.apellido)
        return f"""
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            {LINK_FUENTE}
            <style>{ESTILOS}</style>
        </head>
        <body class="contenedor-mail" style="margin: 0; padding: 16px; {FUENTE}">
          <div style="max-width: 640px; margin: 0 auto;">
            <h1 style="{FUENTE}">¡Gracias por comprar en {self.nombre_parque}!</h1>
            <p>Buenos días, gracias por comprar en {self.nombre_parque}.</p>
            <p>A continuación se listan los datos de la compra del visitante {nombre} {apellido}. La factura también va adjunta en PDF.</p>
            <h2 style="{FUENTE}">Detalle de las entradas</h2>
            {self.tabla_entradas()}
            <h2 style="{FUENTE}">Factura</h2>
            {self.datos_factura()}
            {self.tabla_factura()}
            {self.tabla_totales()}
            <p>Saludos desde {self.nombre_parque}.</p>
            {self.aviso_pago()}
          </div>
        </body>
        </html>
        """

    def tabla_entradas(self) -> str:
        """Una fila por visitante con los datos de su entrada.
        En el celular se ocultan las columnas Fecha y Pase y se muestran debajo del visitante."""
        fecha = f"{self.entrada.fecha_entrada:%d/%m/%Y}"
        pase = self.entrada.tipo_pase.value
        filas = "".join(f"""
                <tr>
                    <td style="{CELDA}">
                        {visitante}
                        <div class="solo-mobile" style="{SOLO_MOBILE}">{fecha} · {pase}</div>
                    </td>
                    <td class="ocultar-mobile" style="{CELDA}">{fecha}</td>
                    <td class="ocultar-mobile" style="{CELDA}">{pase}</td>
                    <td style="{CELDA} white-space: nowrap;">{edad} años</td>
                    <td style="{CELDA} {MONTO}">{formatear_monto(self.entrada.monto_por_edad(edad))}</td>
                </tr>""" for visitante, edad in enumerate(self.entrada.edades, start=1))
        return f"""
            <table class="tabla-mail" style="width: 100%; border-collapse: collapse; {FUENTE}">
                <tr>
                    <th style="{CELDA}">Visitante</th>
                    <th class="ocultar-mobile" style="{CELDA}">Fecha</th>
                    <th class="ocultar-mobile" style="{CELDA}">Pase</th>
                    <th style="{CELDA}">Edad</th>
                    <th style="{CELDA} {MONTO}">Precio</th>
                </tr>{filas}
            </table>
        """

    def datos_factura(self) -> str:
        return f"""
            <p style="{FUENTE}">
                N° {self.factura.numero}<br>
                Fecha de emisión: {self.factura.fecha_emision:%d/%m/%Y}<br>
                {escape(self.nombre_parque)}<br>
                Cliente: {escape(self.usuario.apellido)} {escape(self.usuario.nombre)}<br>
                Mail: <span style="word-break: break-all;">{escape(self.usuario.mail)}</span><br>
                Forma de pago: {self.entrada.forma_pago.value}
            </p>
        """

    def tabla_factura(self) -> str:
        """Una fila por visitante con el precio, el descuento y el subtotal.
        En el celular se oculta la columna Precio y se muestra debajo del concepto."""
        pase = escape(self.entrada.tipo_pase.value)
        filas = "".join(f"""
                <tr>
                    <td style="{CELDA}">
                        <span class="ocultar-mobile">Entrada {pase} - </span>Visitante {linea.visitante} <span style="white-space: nowrap;">({linea.edad} años)</span>
                        <div class="solo-mobile" style="{SOLO_MOBILE}">Entrada {pase}: <span style="white-space: nowrap;">{formatear_monto(linea.precio_unitario)}</span></div>
                    </td>
                    <td class="ocultar-mobile" style="{CELDA} {MONTO}">{formatear_monto(linea.precio_unitario)}</td>
                    <td style="{CELDA} {MONTO}">- {formatear_monto(linea.descuento)}</td>
                    <td style="{CELDA} {MONTO}">{formatear_monto(linea.subtotal)}</td>
                </tr>""" for linea in self.factura.lineas)
        return f"""
            <table class="tabla-mail" style="width: 100%; border-collapse: collapse; {FUENTE}">
                <tr>
                    <th style="{CELDA}">Concepto</th>
                    <th class="ocultar-mobile" style="{CELDA} {MONTO}">Precio</th>
                    <th style="{CELDA} {MONTO}">Descuento</th>
                    <th style="{CELDA} {MONTO}">Subtotal</th>
                </tr>{filas}
            </table>
        """

    def tabla_totales(self) -> str:
        # los totales van en otra tabla: con la columna Precio oculta en el celular, un colspan desarmaría la grilla
        return f"""
            <table class="tabla-mail" style="width: 100%; border-collapse: collapse; margin-top: 8px; {FUENTE}">
                <tr>
                    <td style="{TOTAL}">Subtotal</td>
                    <td style="{TOTAL} width: 1%;">{formatear_monto(self.factura.subtotal)}</td>
                </tr>
                <tr>
                    <td style="{TOTAL}">Descuentos</td>
                    <td style="{TOTAL} width: 1%;">- {formatear_monto(self.factura.descuentos)}</td>
                </tr>
                <tr>
                    <td style="{TOTAL} font-weight: bold;">Total</td>
                    <td style="{TOTAL} width: 1%; font-weight: bold;">{formatear_monto(self.factura.total)}</td>
                </tr>
            </table>
        """

    def aviso_pago(self) -> str:
        if self.entrada.forma_pago == FormaPago.EFECTIVO:
            return f"<p><small>{AVISO_EFECTIVO}</small></p>"
        return ""
