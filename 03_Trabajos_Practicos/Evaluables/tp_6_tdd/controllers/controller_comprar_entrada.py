from dataclasses import dataclass, field
from datetime import date, datetime
from email.message import EmailMessage
from html import escape

from entities.mail import AdaptadorMailGmail, ServicioMail
from entities.entrada import Entrada
from entities.factura import (CELDA_MAIL, ESTILOS_MAIL, FUENTE_MAIL, LINK_FUENTE_MAIL, MONTO_MAIL, SOLO_MOBILE,
                              Factura, formatear_monto)
from entities.parque import Parque
from entities.mercado_pago import PasarelaMercadoPago
from entities.tipo_pase import TipoPase
from entities.usuario import Usuario
from entities.errores import ErrorMail, ErrorValidacion
from entities.forma_pago import FormaPago


@dataclass
class ControllerComprarEntrada:
    usuario: Usuario
    parque: Parque = field(default_factory=Parque)
    entrada: Entrada | None = field(default=None, init=False)  # la crea el controller en comprar_entrada
    pasarela: PasarelaMercadoPago | None = None  # si no viene, se crea como instancia única recién al pagar con tarjeta
    servicio_mail: ServicioMail = field(default_factory=AdaptadorMailGmail)
    factura: Factura | None = field(default=None, init=False)  # se emite al confirmar la compra

    def comprar_entrada(self, fecha_entrada: date | str, cantidad: int, edades: list[int], tipo_pase: TipoPase | str, forma_pago: FormaPago | str, ahora: datetime | None = None) -> Entrada:
        if ahora is None:  # si viene cargada es porque viene por el test
            ahora = datetime.now()

        self.usuario.registrar()
        self.entrada = Entrada(fecha_entrada, cantidad, edades, tipo_pase, forma_pago)
        self.entrada.registrar(self.parque, ahora)
        self.validar_maximo_entradas_por_fecha()

        # si el pago con tarjeta es rechazado, cobrar lanza ErrorPago y no se guarda la entrada ni se envía el mail
        if self.entrada.forma_pago == FormaPago.TARJETA:
            if self.pasarela is None:
                self.pasarela = PasarelaMercadoPago()
            self.pasarela.cobrar(self.entrada)

        self.entrada.fecha_compra = ahora.date()
        self.factura = Factura.emitir(self.usuario, self.entrada, self.parque.nombre, ahora)
        self.usuario.agregar_entrada(self.entrada)
        self.enviar_mail()
        return self.entrada

    def validar_maximo_entradas_por_fecha(self, maximo: int = 10) -> None:
        """El usuario puede comprar hasta 10 entradas para una misma fecha, en una o varias transacciones."""
        compradas = sum(entrada.cantidad for entrada in self.usuario.entradas
                        if entrada.fecha_entrada == self.entrada.fecha_entrada)
        if compradas + self.entrada.cantidad > maximo:
            raise ErrorValidacion(f"Solo se pueden comprar {maximo} entradas para una misma fecha; "
                                  f"ya compraste {compradas}.", campo="cantidad")

    def enviar_mail(self) -> None:
        if self.entrada is None:
            raise ErrorMail("No hay una entrada para enviar el mail de confirmación.")
        mail_enviado = self.servicio_mail.enviar(self.generar_mail())
        if not mail_enviado:
            raise ErrorMail("No se pudo enviar el mail de confirmación.")

    def generar_mail(self) -> EmailMessage:
        # si la entrada se cargó sin pasar por comprar_entrada, la factura se emite recién ahora
        if self.factura is None or self.factura.entrada is not self.entrada:
            self.factura = Factura.emitir(self.usuario, self.entrada, self.parque.nombre, datetime.now())

        cuerpo_pago = ''
        mensaje = EmailMessage()
        mensaje['Subject'] = f'{self.parque.nombre}: Compra Confirmada'
        mensaje['To'] = self.usuario.mail

        if self.entrada.forma_pago == FormaPago.EFECTIVO:
            cuerpo_pago = '<p><small>Se informa que al haber seleccionado la modalidad de pago en efectivo, deberá abonar el importe total correspondiente a su reserva al momento de ingresar al parque. En caso de no efectuarse el pago, el parque se reserva el derecho de admisión del visitante.</small></p>'

        nombre = escape(self.usuario.nombre)
        apellido = escape(self.usuario.apellido)
        cuerpo_html = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            {LINK_FUENTE_MAIL}
            <style>{ESTILOS_MAIL}</style>
        </head>
        <body class="contenedor-mail" style="margin: 0; padding: 16px; {FUENTE_MAIL}">
          <div style="max-width: 640px; margin: 0 auto;">
            <h1 style="{FUENTE_MAIL}">¡Gracias por comprar en {self.parque.nombre}!</h1>
            <p>Buenos días, gracias por comprar en {self.parque.nombre}.</p>
            <p>A continuación se listan los datos de la compra del visitante {nombre} {apellido}. La factura también va adjunta en PDF.</p>
            <h2 style="{FUENTE_MAIL}">Detalle de las entradas</h2>
            {self.generar_tabla_entradas()}
            {self.factura.generar_html()}
            <p>Saludos desde {self.parque.nombre}.</p>
            {cuerpo_pago}
          </div>
        </body>
        </html>
        """
        mensaje.add_alternative(cuerpo_html, subtype='html')
        mensaje.add_attachment(self.factura.generar_pdf(), maintype='application', subtype='pdf',
                               filename=self.factura.nombre_archivo)
        return mensaje

    def generar_tabla_entradas(self) -> str:
        """Una fila por visitante con los datos de su entrada.
        En el celular se ocultan las columnas Fecha y Pase y se muestran debajo del visitante (ver ESTILOS_MAIL)."""
        fecha = f"{self.entrada.fecha_entrada:%d/%m/%Y}"
        pase = self.entrada.tipo_pase.value
        filas = "".join(f"""
            <tr>
                <td style="{CELDA_MAIL}">
                    {visitante}
                    <div class="solo-mobile" style="{SOLO_MOBILE}">{fecha} · {pase}</div>
                </td>
                <td class="ocultar-mobile" style="{CELDA_MAIL}">{fecha}</td>
                <td class="ocultar-mobile" style="{CELDA_MAIL}">{pase}</td>
                <td style="{CELDA_MAIL} white-space: nowrap;">{edad} años</td>
                <td style="{CELDA_MAIL} {MONTO_MAIL}">{formatear_monto(self.entrada.monto_por_edad(edad))}</td>
            </tr>""" for visitante, edad in enumerate(self.entrada.edades, start=1))
        return f"""
            <table class="tabla-mail" style="width: 100%; border-collapse: collapse; {FUENTE_MAIL}">
                <tr>
                    <th style="{CELDA_MAIL}">Visitante</th>
                    <th class="ocultar-mobile" style="{CELDA_MAIL}">Fecha</th>
                    <th class="ocultar-mobile" style="{CELDA_MAIL}">Pase</th>
                    <th style="{CELDA_MAIL}">Edad</th>
                    <th style="{CELDA_MAIL} {MONTO_MAIL}">Precio</th>
                </tr>{filas}
            </table>
        """
