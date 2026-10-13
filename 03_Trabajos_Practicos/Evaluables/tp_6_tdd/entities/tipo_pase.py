from enum import Enum


class TipoPase(Enum):
    REGULAR = "Regular"
    VIP = "VIP"

    def monto_entrada(self) -> float:
        return 1000.00 if self is TipoPase.VIP else 500.00
