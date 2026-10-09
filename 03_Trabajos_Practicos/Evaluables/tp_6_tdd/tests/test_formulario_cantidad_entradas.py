import pytest
from entities.entrada import Entrada
from entities.errores import ErrorValidacion
from conftest import crear_entrada


def validar_cantidad(valor):
    entrada = crear_entrada(cantidad=valor)
    entrada.validar_cantidad_entradas()
    return entrada.cantidad


def validar_edades(edades, cantidad):
    entrada = crear_entrada(cantidad=cantidad, edades=edades)
    entrada.validar_edades()
    entrada.validar_cantidad_edad_entradas()
    return entrada.edades


# 2.1 Probar una cantidad de entradas entre 1 y 10. PASA
@pytest.mark.parametrize("valor, esperado", [(1, 1), (5, 5), (9, 9), ("3", 3)])
def test_cantidad_entre_1_10(valor, esperado):
    assert validar_cantidad(valor) == esperado


# 2.2 Probar exactamente 10 entradas. PASA
def test_cantidad_10():
    assert validar_cantidad(10) == 10


# 2.3 Probar una cantidad de entradas mayor a 10. FALLA
@pytest.mark.parametrize("valor", [11, 50])
def test_cantidad_mayor_10(valor):
    with pytest.raises(ErrorValidacion):
        validar_cantidad(valor)


# 2.4 Probar una cantidad igual a 0. FALLA
def test_cantidad_cero():
    with pytest.raises(ErrorValidacion):
        validar_cantidad(0)


# 2.5 Probar una cantidad negativa. FALLA
@pytest.mark.parametrize("valor", [-1, -10])
def test_cantidad_negativa(valor):
    with pytest.raises(ErrorValidacion):
        validar_cantidad(valor)


# 2.6 Probar una cantidad decimal. FALLA
@pytest.mark.parametrize("valor", [2.5, "2.5"])
def test_cantidad_decimal(valor):
    with pytest.raises(ErrorValidacion):
        validar_cantidad(valor)

# 2.7 Probar una cantidad no numérica. FALLA
@pytest.mark.parametrize("valor", ["tres", "", None, True])
def test_cantidad_no_numerica(valor):
    with pytest.raises(ErrorValidacion):
        validar_cantidad(valor)


# 2.8 Probar que la cantidad de entradas sea la misma cantidad de edades a cargar. PASA
def test_cantidad_igual_a_cantidad_de_edades():
    assert validar_edades([30, 15, 65], cantidad=3) == [30, 15, 65]


# 2.9 Probar que se cargó la cantidad de entradas en el formulario. PASA
def test_formulario_tiene_cantidad_cargada(datos_validos, parque, ahora):
    entrada = Entrada(**datos_validos)
    entrada.registrar(parque, ahora)
    assert entrada.cantidad == 2
