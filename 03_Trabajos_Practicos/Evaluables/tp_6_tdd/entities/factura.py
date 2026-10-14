import uuid
from dataclasses import dataclass
from datetime import date, datetime

from entities.entrada import Entrada
from entities.usuario import Usuario


@dataclass
class LineaFactura:
    """Lo que paga un visitante: el precio del pase y el descuento según su edad."""
    visitante: int
    edad: int
    precio_unitario: float
    descuento: float  # en pesos
    subtotal: float


@dataclass
class Factura:
    """Los datos de la factura de una compra. Cómo se muestra (mail o PDF) lo resuelven las boundaries."""
    numero: str
    fecha_emision: date
    usuario: Usuario
    entrada: Entrada
    nombre_parque: str

    @classmethod
    def emitir(cls, usuario: Usuario, entrada: Entrada, nombre_parque: str, ahora: datetime) -> "Factura":
        numero = f"{ahora:%Y%m%d}-{uuid.uuid4().hex[:6].upper()}"
        return cls(numero, ahora.date(), usuario, entrada, nombre_parque)

    @property
    def lineas(self) -> list[LineaFactura]:
        lineas = []
        precio = self.entrada.tipo_pase.monto_entrada()
        for visitante, edad in enumerate(self.entrada.edades, start=1):
            subtotal = self.entrada.monto_por_edad(edad)
            lineas.append(LineaFactura(visitante, edad, precio, precio - subtotal, subtotal))
        return lineas

    @property
    def subtotal(self) -> float:
        return sum(linea.precio_unitario for linea in self.lineas)

    @property
    def descuentos(self) -> float:
        return sum(linea.descuento for linea in self.lineas)

    @property
    def total(self) -> float:
        return sum(linea.subtotal for linea in self.lineas)

    @property
    def nombre_archivo(self) -> str:
        return f"factura-{self.numero}.pdf"
