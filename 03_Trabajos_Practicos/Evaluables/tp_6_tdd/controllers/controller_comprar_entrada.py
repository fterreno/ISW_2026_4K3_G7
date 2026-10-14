from dataclasses import dataclass, field
from datetime import date, datetime
from email.message import EmailMessage

from boundaries.mail_confirmacion import MailConfirmacion
from entities.mail import AdaptadorMailGmail, ServicioMail
from entities.entrada import Entrada
from entities.factura import Factura
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
        return MailConfirmacion(self.factura).generar()
