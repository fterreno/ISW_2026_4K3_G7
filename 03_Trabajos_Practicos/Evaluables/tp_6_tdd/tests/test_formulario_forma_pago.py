import pytest
from entities.entrada import Entrada
from entities.errores import ErrorValidacion
from entities.forma_pago import FormaPago
from conftest import crear_entrada


def validar_forma_pago(valor):
    entrada = crear_entrada(forma_pago=valor)
    entrada.validar_forma_pago()
    return entrada.forma_pago


# 5.1 Probar seleccionar pago en efectivo. PASA
def test_pago_en_efectivo():
    assert validar_forma_pago("Efectivo") == FormaPago.EFECTIVO


# 5.2 Probar seleccionar pago con tarjeta (Mercado Pago). PASA
def test_pago_con_tarjeta():
    assert validar_forma_pago("Tarjeta") == FormaPago.TARJETA


# 5.3 Probar realizar la compra sin seleccionar una forma de pago. FALLA
@pytest.mark.parametrize("valor", [None, ""])
def test_compra_sin_forma_de_pago(datos_validos, parque, ahora, valor):
    with pytest.raises(ErrorValidacion):
        Entrada(**{**datos_validos, "forma_pago": valor}).registrar(parque, ahora)


# 5.4 Probar una forma de pago distinta de efectivo o tarjeta. FALLA
@pytest.mark.parametrize("valor", ["transferencia", "cripto"])
def test_forma_de_pago_invalida(valor):
    with pytest.raises(ErrorValidacion):
        validar_forma_pago(valor)
