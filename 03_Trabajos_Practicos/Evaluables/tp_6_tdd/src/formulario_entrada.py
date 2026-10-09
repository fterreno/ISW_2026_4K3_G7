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
class Usuario:
    mail: str
    nombre: str
    apellido: str

@dataclass
class DetalleCompra:
    monto_total: float
    fecha_compra: date

@dataclass
class FormularioEntrada:
    fecha: date
    cantidad: int
    edades: list[int]
    tipo_pase: TipoPase
    forma_pago: FormaPago
    detalle_compra: DetalleCompra
    usuario: Usuario


def validar_fecha_visita(fecha: date, hoy: date) -> date:
    """Valida hoy o futuro; el formato de ingreso y la apertura se resuelven aparte."""
    if fecha < hoy:
        raise ErrorValidacion("La fecha de visita no puede ser anterior a la fecha actual.")
    return fecha


def validar_fecha(texto, ahora: datetime, horario: HorarioParque) -> date:
    """Recibe la fecha en formato dd/mm/aaaa y devuelve el date si es válida."""
    try:
        fecha = datetime.strptime(texto, "%d/%m/%Y").date()
    except (TypeError, ValueError):
        raise ErrorValidacion("La fecha debe tener el formato dd/mm/aaaa.")

    validar_fecha_visita(fecha, ahora.date())

    if fecha.weekday() not in horario.dias_abiertos:
        raise ErrorValidacion("El parque está cerrado ese día.")

    if fecha == ahora.date() and not (
        horario.hora_apertura <= ahora.time() <= horario.hora_cierre
    ):
        raise ErrorValidacion("La hora actual está fuera del horario de apertura.")

    return fecha


def validar_cantidad(valor) -> int:
    if isinstance(valor, bool):
        raise ErrorValidacion("La cantidad debe ser un número entero.")
    try:
        cantidad = int(valor)
    except (ValueError, TypeError):
        raise ErrorValidacion("La cantidad debe ser un número entero")

    if isinstance(valor, float):
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

    if isinstance(valor, float):
        raise ErrorValidacion("La edad debe ser un número entero")

    if edad < 0:
        raise ErrorValidacion("La edad debe ser un número positivo.")

    return edad

def validar_edades(edades, cantidad: int) -> list[int]:
    edades_validadas = [validar_edad(edad) for edad in edades]
    if len(edades_validadas) != cantidad:
        raise ErrorValidacion("Las cantidades de edades y la cantidad de entradas no coincide.")
    return edades_validadas


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
    cantidad_validada = validar_cantidad(cantidad)

    return FormularioEntrada(
        fecha=validar_fecha(fecha, ahora, horario),
        cantidad=cantidad_validada,
        edades=validar_edades(edades, cantidad_validada),
        tipo_pase=validar_tipo_pase(tipo_pase),
        forma_pago=validar_forma_pago(forma_pago),
    )

def generar_monto_total() -> float:
    # generamos el monto total de las entradas teniendo en cuenta que cada entrada vale 0.5 pesos
    return 0.5