from dataclasses import dataclass
from datetime import date, datetime
from email.message import EmailMessage

from entities.parque import Parque
from entities.tipo_pase import TipoPase
from entities.errores import ErrorValidacion, ErroresValidacion, validar_campo
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
        """Valida todos los datos y, si hay errores, los informa todos juntos."""
        errores: list[ErrorValidacion] = []
        validar_campo("fecha", lambda: self.validar_fecha(parque, ahora), errores)
        cantidad_valida = validar_campo("cantidad", self.validar_cantidad_entradas, errores)
        edades_validas = validar_campo("edades", self.validar_edades, errores)
        # solo se comparan si las dos son válidas; si no, ya se informó el error de la que falló
        if cantidad_valida and edades_validas:
            validar_campo("edades", self.validar_cantidad_edad_entradas, errores)
        validar_campo("tipo_pase", self.validar_tipo_pase, errores)
        validar_campo("forma_pago", self.validar_forma_pago, errores)
        if errores:
            raise ErroresValidacion(errores)
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
        """Valida todas las edades e informa juntas las inválidas, cada una con la posición de su visitante."""
        edades_validadas = []
        errores = []
        for indice, edad in enumerate(self.edades):
            try:
                edades_validadas.append(self.validar_edad(edad))
            except ErrorValidacion as error:
                error.indice = indice
                errores.append(error)
        if errores:
            raise ErroresValidacion(errores)
        self.edades = edades_validadas

    @staticmethod
    def validar_edad(edad) -> int:
        edad_minima = 0
        edad_maxima = 100
        if isinstance(edad, (bool, float)):
            raise ErrorValidacion("La edad debe ser un número entero")
        try:
            edad = int(edad)
        except (ValueError, TypeError):
            raise ErrorValidacion("La edad debe ser un número entero")
        if edad < 0:
            raise ErrorValidacion("La edad debe ser un número positivo.")
        if edad < edad_minima:
            raise ErrorValidacion(f"La edad minima permitida es de {edad_minima} años.")
        if edad > edad_maxima:
            raise ErrorValidacion(f"La edad maxima permitida es de {edad_maxima} años.")
        return edad

    def validar_cantidad_edad_entradas(self) -> None:
        if len(self.edades) != self.cantidad:
            raise ErrorValidacion("Las cantidades de edades y la cantidad de entradas no coincide.")

    def validar_tipo_pase(self) -> None:
        try:
            self.tipo_pase = TipoPase(self.tipo_pase)
        except ValueError:
            raise ErrorValidacion("Debe seleccionar una opcion.")

    def validar_forma_pago(self) -> None:
        try:
            self.forma_pago = FormaPago(self.forma_pago)
        except ValueError:
            raise ErrorValidacion("Debe seleccionar una opcion.")

    def generar_monto_total(self) -> None:
        # el monto total es la suma de lo que paga cada visitante según el tipo de pase y su edad
        self.monto_total = sum(self.monto_por_edad(edad) for edad in self.edades)

    def monto_por_edad(self, edad: int) -> float:
        """Lo que paga el visitante: el precio del pase menos el descuento de su categoría de edad."""
        _, descuento = self.categoria_por_edad(edad)
        return self.tipo_pase.monto_entrada() * (1 - descuento)

    @staticmethod
    def categoria_por_edad(edad: int) -> tuple[str, float]:
        """Devuelve la categoría del visitante y su descuento (1 es 100%): hasta 3 años no paga;
        hasta 15 años y desde 60 años paga la mitad del pase."""
        if edad <= 3:
            return "Hasta 3 años", 1.0
        if edad <= 15:
            return "Hasta 15 años", 0.5
        if edad >= 60:
            return "Desde 60 años", 0.5
        return "General", 0.0