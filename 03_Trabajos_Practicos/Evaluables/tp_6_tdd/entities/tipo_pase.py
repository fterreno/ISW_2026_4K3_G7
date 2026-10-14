from enum import Enum


class TipoPase(Enum):
    REGULAR = "Regular" # $ 10000
    VIP = "VIP" # $ 20000

    def monto_entrada(self) -> float:
        return 20000.00 if self is TipoPase.VIP else 10000.00
