from dataclasses import dataclass
from datetime import date, datetime, time
from enum import Enum


class ErrorValidacion(Exception):
    """Se lanza cuando un dato del formulario de compra de entradas no es válido."""


@dataclass
class HorarioParque:
    dias_abiertos: set[int]  # 0 es lunes ... 6 es domingo
    hora_apertura: time
    hora_cierre: time


class TipoPase(Enum):
    REGULAR = "Regular"
    VIP = "VIP"

class FormaPago(Enum):
    EFECTIVO = "Efectivo"
    TARJETA = "Tarjeta"

@dataclass
class FormularioEntrada:
    fecha: date
    cantidad: int
    edades: list[int]
    tipo_pase: TipoPase
    forma_pago: FormaPago


def validar_fecha(texto, ahora: datetime, horario: HorarioParque) -> date:
    """Recibe la fecha en formato dd/mm/aaaa y devuelve el date si es válida."""
    raise NotImplementedError


def validar_cantidad(valor) -> int:
    raise NotImplementedError


def validar_edad(valor) -> int:
    raise NotImplementedError


def validar_edades(edades, cantidad: int) -> list[int]:
    raise NotImplementedError


def validar_tipo_pase(valor) -> TipoPase:
    raise NotImplementedError


def validar_forma_pago(valor) -> FormaPago:
    raise NotImplementedError


def registrar_formulario(fecha, cantidad, edades, tipo_pase, forma_pago, ahora: datetime, horario: HorarioParque) -> FormularioEntrada:
    raise NotImplementedError
