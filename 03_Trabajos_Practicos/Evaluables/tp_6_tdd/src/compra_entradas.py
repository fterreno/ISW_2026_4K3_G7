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


def generar_mail(formulario: FormularioEntrada, destinatario: str) -> Mail:
    raise NotImplementedError


def enviar_mail(mail: Mail, servicio_mail) -> None:
    raise NotImplementedError

# aca simplemente se encargar de generar el mail y enviarlo y llamar a la pasarela de mercado pago de ser necesario
def registrar_compra(formulario: FormularioEntrada, destinatario: str, pasarela, servicio_mail) -> ResultadoCompra:
    raise NotImplementedError

# abria que fijarse de crear una funcion extra para mercado pago prob