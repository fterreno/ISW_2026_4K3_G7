import pytest
from formulario_entrada import ErrorValidacion, validar_edad, validar_edades


# 3.1 Probar cargar una edad numérica y entera. PASA
@pytest.mark.parametrize("valor, esperado", [(30, 30), ("30", 30)])
def test_edad_numerica_entera(valor, esperado):
    assert validar_edad(valor) == esperado


# 3.2 Probar cargar la edad de un visitante mayor a n años. PASA
@pytest.mark.parametrize("valor", [65, 90])
def test_edad_visitante_mayor(valor):
    assert validar_edad(valor) == valor


# 3.3 Probar cargar la edad de un visitante menor a m años. PASA
@pytest.mark.parametrize("valor", [0, 3])  # 0 = bebé
def test_edad_visitante_menor(valor):
    assert validar_edad(valor) == valor


# 3.4 Probar cargar una edad negativa. FALLA
def test_edad_negativa():
    with pytest.raises(ErrorValidacion):
        validar_edad(-1)


# 3.5 Probar cargar una edad no numérica. FALLA
@pytest.mark.parametrize("valor", ["treinta", "", None, True])
def test_edad_no_numerica(valor):
    with pytest.raises(ErrorValidacion):
        validar_edad(valor)


# 3.6 Probar cargar una edad decimal. FALLA
@pytest.mark.parametrize("valor", [8.5, "8.5"])
def test_edad_decimal(valor):
    with pytest.raises(ErrorValidacion):
        validar_edad(valor)


# 3.7 Probar cargar correctamente la edad de todos los visitantes. PASA
def test_edades_de_todos_los_visitantes():
    assert validar_edades([30, 28, 5], cantidad=3) == [30, 28, 5]


# 3.8 Probar cargar la edad de todos los visitantes y que una de ellas sea inválida. FALLA
@pytest.mark.parametrize("edades", [[30, -2, 5], [30, "abc", 5], [30, 7.5, 5]])
def test_una_edad_invalida(edades):
    with pytest.raises(ErrorValidacion):
        validar_edades(edades, cantidad=3)


# 3.9 Probar no cargar la edad de alguno de los visitantes. FALLA
@pytest.mark.parametrize("edades", [[30, 5], [30, None, 5]])
def test_falta_la_edad_de_un_visitante(edades):
    with pytest.raises(ErrorValidacion):
        validar_edades(edades, cantidad=3)
