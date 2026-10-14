from datetime import date
from entities.entrada import Entrada
from entities.forma_pago import FormaPago
from entities.tipo_pase import TipoPase


def monto_de_una_entrada(tipo_pase, edad):
    entrada = Entrada(date(2026, 10, 9), 1, [edad], tipo_pase, FormaPago.EFECTIVO)
    entrada.generar_monto_total()
    return entrada.monto_total


# 9.1 Probar una entrada VIP con una edad de 3 años o menor y el monto de la entrada es cero PASA
def test_vip_hasta_3_anios_es_gratis():
    assert monto_de_una_entrada(TipoPase.VIP, 3) == 0


# 9.2 Probar una entrada Regular con una edad de 3 años o menor y el monto de la entrada es cero PASA
def test_regular_hasta_3_anios_es_gratis():
    assert monto_de_una_entrada(TipoPase.REGULAR, 3) == 0


# 9.3 Probar una entrada VIP con edad menor o igual a 15 años y el monto de la entrada es 10000 PASA
def test_vip_hasta_15_anios_paga_10000():
    assert monto_de_una_entrada(TipoPase.VIP, 15) == 10000


# 9.4 Probar una entrada Regular con edad menor o igual a 15 años y el monto de la entrada es 5000 PASA
def test_regular_hasta_15_anios_paga_5000():
    assert monto_de_una_entrada(TipoPase.REGULAR, 15) == 5000


# 9.5 Probar una entrada VIP con edad mayor o igual a 60 años y el monto de la entrada es 10000 PASA
def test_vip_desde_60_anios_paga_10000():
    assert monto_de_una_entrada(TipoPase.VIP, 60) == 10000


# 9.6 Probar una entrada Regular con edad mayor o igual a 60 años y el monto de la entrada es 5000 PASA
def test_regular_desde_60_anios_paga_5000():
    assert monto_de_una_entrada(TipoPase.REGULAR, 60) == 5000
