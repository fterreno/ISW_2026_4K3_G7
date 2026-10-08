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
    if isinstance(valor, bool):
        raise ErrorValidacion("La cantidad debe ser un número entero.")
    try:
        cantidad = int(valor)
    except (ValueError, TypeError):
        raise ErrorValidacion("La cantidad debe ser un número entero")

    if isinstance(valor, float) and valor != cantidad:
        raise ErrorValidacion("La cantidad debe ser un número entero.")
    
    if cantidad < 1 or cantidad > 10:
        raise ErrorValidacion("La cantidad debe estar entre 1 y 10")
    return cantidad


def validar_edad(valor) -> int:
    if isinstance(valor, bool):
        raise ErrorValidacion("La edad debe ser un número entero")
    try:
        edad = int(valor)
    except (ValueError, TypeError):
        raise ErrorValidacion("La edad debe ser un número entero")

    if isinstance(valor, float) and valor != edad:
        raise ErrorValidacion("La edad debe ser un número entero")

    if edad < 0:
        raise ErrorValidacion("La edad debe ser un número positivo.")

    return edad

def validar_edades(edades, cantidad: int) -> list[int]:
    cant = 0
    for i in edades:
        if validar_edad(i):
            cant += 1
            
    if cant != cantidad:
        raise ErrorValidacion("Las cantidades de edades y la cantidad de entradas no coincide.")
    return edades



def validar_tipo_pase(valor) -> TipoPase:
    if valor == "VIP":
        return TipoPase.VIP
    if valor == "Regular":
        return TipoPase.REGULAR
    raise ErrorValidacion("El tipo de pase debe ser VIP o Regular.")


def validar_forma_pago(valor) -> FormaPago:
    if valor == "Efectivo":
        return FormaPago.EFECTIVO
    if valor == "Tarjeta":
        return FormaPago.TARJETA
    raise ErrorValidacion("La forma de pago debe ser Efectivo o Tarjeta.")

# aca se ocupa que los datos esten validados al momento de apretar el boton de "comprar entradas"
def registrar_formulario(fecha, cantidad, edades, tipo_pase, forma_pago, ahora: datetime, horario: HorarioParque) -> FormularioEntrada:
    raise NotImplementedError
