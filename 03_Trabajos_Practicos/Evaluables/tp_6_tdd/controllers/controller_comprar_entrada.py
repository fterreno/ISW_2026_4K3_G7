from dataclasses import dataclass, field
from datetime import date, datetime
from email.message import EmailMessage

from entities.mail import AdaptadorMailGmail, ServicioMail
from entities.entrada import Entrada
from entities.parque import Parque
from entities.mercado_pago import PasarelaMercadoPago
from entities.tipo_pase import TipoPase
from entities.usuario import Usuario
from entities.errores import ErrorMail
from entities.forma_pago import FormaPago


@dataclass
class ControllerComprarEntrada:
    usuario: Usuario
    parque: Parque = field(default_factory=Parque)
    entrada: Entrada | None = field(default=None, init=False)  # la crea el controller en comprar_entrada
    pasarela: PasarelaMercadoPago = field(default_factory=PasarelaMercadoPago)  # siempre la instancia única
    servicio_mail: ServicioMail = field(default_factory=AdaptadorMailGmail)  # adaptador de smtplib para Gmail

    def comprar_entrada(self, fecha_entrada: date | str, cantidad: int, edades: list[int], tipo_pase: TipoPase | str, forma_pago: FormaPago | str, ahora: datetime | None = None) -> Entrada:
        if ahora is None:  # si viene cargada es porque viene por el test
            ahora = datetime.now()

        self.usuario.registrar()
        self.entrada = Entrada(fecha_entrada, cantidad, edades, tipo_pase, forma_pago)
        self.entrada.registrar(self.parque, ahora)

        # si el pago con tarjeta es rechazado, cobrar lanza ErrorPago y no se guarda la entrada ni se envía el mail
        if self.entrada.forma_pago == FormaPago.TARJETA:
            self.pasarela.cobrar(self.entrada)

        self.entrada.fecha_compra = ahora.date()
        self.usuario.agregar_entrada(self.entrada)
        self.enviar_mail()
        return self.entrada

    def enviar_mail(self) -> None:
        if self.entrada is None:
            raise ErrorMail("No hay una entrada para enviar el mail de confirmación.")
        mail_enviado = self.servicio_mail.enviar(self.generar_mail())
        if not mail_enviado:
            raise ErrorMail("No se pudo enviar el mail de confirmación.")

    def generar_mail(self) -> EmailMessage:
        cuerpo_pago = ''
        mensaje = EmailMessage()
        mensaje['Subject'] = f'{self.parque.nombre}: Compra Confirmada'
        mensaje['To'] = self.usuario.mail

        if self.entrada.forma_pago == FormaPago.EFECTIVO:
            cuerpo_pago = '<small>Se informa que al haber seleccionado la modalidad de pago en efectivo, deberá abonar el importe total correspondiente a su reserva al momento de ingresar al parque. En caso de no efectuarse el pago, el parque se reserva el derecho de admisión del visitante.</small>'

        cuerpo_html = f"""
        <html>
        <body>
            <h1 style="text-align: center;">¡Gracias por comprar en {self.parque.nombre}!</h1>
            <p>Buenos días {self.usuario.apellido} {self.usuario.nombre}, gracias por comprar en {self.parque.nombre}.</p>
            <p>Gracias por su compra. En el archivo adjunto se encuentra generado un pdf con las entradas que se le solicitaran a la entrada de {self.parque.nombre}.</p>
            <br>
            <p style="margin-left: 40px;"> Fecha de visita: {self.entrada.fecha_entrada:%d/%m/%Y}</p>
            <p style="margin-left: 40px;"> Tipo de pase: {self.entrada.tipo_pase.value}</p>
            <p style="margin-left: 40px;"> Cantidad de entradas compradas: {self.entrada.cantidad}</p>
            <p style="margin-left: 40px;"> Forma de Pago: {self.entrada.forma_pago.value}</p>
            <p style="margin-left: 40px;"> Total: $ {self.entrada.monto_total}</p>
            <br>
            <p>Saludos desde {self.parque.nombre}.</p>
            <br>
            {cuerpo_pago}
        </body>
        </html>
        """
        mensaje.add_alternative(cuerpo_html, subtype='html')
        return mensaje
