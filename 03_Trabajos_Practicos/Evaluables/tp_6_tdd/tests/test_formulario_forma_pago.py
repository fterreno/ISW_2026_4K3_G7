import pytest
from formulario_entrada import ErrorValidacion, FormaPago, registrar_formulario, validar_forma_pago


# 5.1 Probar seleccionar pago en efectivo. PASA
def test_pago_en_efectivo():
    assert validar_forma_pago("Efectivo") == FormaPago.EFECTIVO


# 5.2 Probar seleccionar pago con tarjeta (Mercado Pago). PASA
def test_pago_con_tarjeta():
    assert validar_forma_pago("Tarjeta") == FormaPago.TARJETA


# 5.3 Probar realizar la compra sin seleccionar una forma de pago. FALLA
@pytest.mark.parametrize("valor", [None, ""])
def test_compra_sin_forma_de_pago(datos_validos, valor):
    with pytest.raises(ErrorValidacion):
        registrar_formulario(**{**datos_validos, "forma_pago": valor})


# 5.4 Probar una forma de pago distinta de efectivo o tarjeta. FALLA
@pytest.mark.parametrize("valor", ["transferencia", "cripto"])
def test_forma_de_pago_invalida(valor):
    with pytest.raises(ErrorValidacion):
        validar_forma_pago(valor)
