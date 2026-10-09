from dataclasses import dataclass
from datetime import date, datetime
from email.message import EmailMessage

from entities.parque import Parque
from entities.tipo_pase import TipoPase
from entities.errores import ErrorValidacion
from entities.forma_pago import FormaPago


@dataclass
class Entrada:
    fecha_entrada: date | str
    cantidad: int
    edades: list[int]
    tipo_pase: TipoPase | str
    forma_pago: FormaPago | str
    monto_total: float | None = None
    fecha_compra: date | None = None

    def registrar(self, parque: Parque, ahora: datetime | None = None) -> None:
        self.validar_fecha(parque, ahora)
        self.validar_cantidad_entradas()
        self.validar_edades()
        self.validar_cantidad_edad_entradas()
        self.validar_tipo_pase()
        self.validar_forma_pago()
        self.generar_monto_total()

    def validar_fecha(self, parque: Parque, ahora: datetime | None = None) -> None:
        """Recibe la fecha en formato dd/mm/aaaa, la convierte a date y le pide al parque que confirme si está disponible."""
        try:
            self.fecha_entrada = datetime.strptime(self.fecha_entrada, "%d/%m/%Y").date()
        except (TypeError, ValueError):
            raise ErrorValidacion("La fecha debe tener el formato dd/mm/aaaa.")
        parque.validar_disponibilidad(self.fecha_entrada, ahora)

    def validar_cantidad_entradas(self) -> None:
        if isinstance(self.cantidad, (bool, float)):
            raise ErrorValidacion("La cantidad debe ser un número entero.")
        try:
            self.cantidad = int(self.cantidad)
        except (ValueError, TypeError):
            raise ErrorValidacion("La cantidad debe ser un número entero")
        if self.cantidad < 1 or self.cantidad > 10:
            raise ErrorValidacion("La cantidad debe estar entre 1 y 10")

    def validar_edades(self) -> None:
        edad_minima = 12
        edad_maxima = 70
        edades_validadas = []
        for edad in self.edades:
            if isinstance(edad, (bool, float)):
                raise ErrorValidacion("La edad debe ser un número entero")
            try:
                edad = int(edad)
            except (ValueError, TypeError):
                raise ErrorValidacion("La edad debe ser un número entero")
            if edad < 0:
                raise ErrorValidacion("La edad debe ser un número positivo.")
            if edad < edad_minima:
                raise ErrorValidacion(f"No se permite el ingreso de una persona menor a {edad_minima} años.")
            if edad > edad_maxima:
                raise ErrorValidacion(f"No se permite el ingreso de una persona mayor a {edad_maxima} años.")
            edades_validadas.append(edad)
        self.edades = edades_validadas

    def validar_cantidad_edad_entradas(self) -> None:
        if len(self.edades) != self.cantidad:
            raise ErrorValidacion("Las cantidades de edades y la cantidad de entradas no coincide.")

    def validar_tipo_pase(self) -> None:
        try:
            self.tipo_pase = TipoPase(self.tipo_pase)
        except ValueError:
            raise ErrorValidacion("El tipo de pase debe ser VIP o Regular.")

    def validar_forma_pago(self) -> None:
        try:
            self.forma_pago = FormaPago(self.forma_pago)
        except ValueError:
            raise ErrorValidacion("La forma de pago debe ser Efectivo o Tarjeta.")

    def generar_monto_total(self) -> None:
    # generamos el monto total de las entradas teniendo en cuenta que cada entrada vale 1000 pesos
        self.monto_total = self.cantidad * 1000.00