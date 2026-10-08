import pytest
from formulario_entrada import ErrorValidacion, TipoPase, validar_tipo_pase


# 4.1 Probar seleccionar pase VIP. PASA
def test_pase_vip():
    assert validar_tipo_pase("VIP") == TipoPase.VIP


# 4.2 Probar seleccionar pase Regular. PASA
def test_pase_regular():
    assert validar_tipo_pase("Regular") == TipoPase.REGULAR


# 4.3 Probar un tipo de pase distinto de VIP o Regular. FALLA
@pytest.mark.parametrize("valor", ["Premium", "", None])
def test_pase_invalido(valor):
    with pytest.raises(ErrorValidacion):
        validar_tipo_pase(valor)
