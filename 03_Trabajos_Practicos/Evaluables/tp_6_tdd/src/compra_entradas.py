from dataclasses import dataclass
from datetime import date

from formulario_entrada import FormularioEntrada


class ErrorPago(Exception):
    """Se lanza cuando Mercado Pago rechaza el pago."""


class ErrorMail(Exception):
    """Se lanza cuando se intenta enviar un mail inválido (por ejemplo, vacío)."""


@dataclass
class ResultadoPago:
    aprobado: bool
    motivo: str = ""


@dataclass
class Mail:
    destinatario: str
    asunto: str
    cuerpo: str


@dataclass
class ResultadoCompra:
    cantidad: int
    fecha: date
    mensaje: str


def armar_mail_confirmacion(formulario: FormularioEntrada, destinatario: str) -> Mail:
    raise NotImplementedError


def enviar_mail(mail: Mail, servicio_mail) -> None:
    raise NotImplementedError


def confirmar_compra(formulario: FormularioEntrada, destinatario: str, pasarela, servicio_mail) -> ResultadoCompra:
    raise NotImplementedError
