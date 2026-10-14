import pytest
from datetime import date, datetime
from entities.entrada import Entrada
from entities.errores import ErrorValidacion
from conftest import crear_entrada


def validar_fecha(texto, ahora, parque):
    entrada = crear_entrada(fecha_entrada=texto)
    entrada.validar_fecha(parque, ahora)
    return entrada.fecha_entrada


# 1.1 Probar que la fecha de visita sea la fecha actual. PASA
def test_fecha_actual_es_valida(ahora, parque):
    assert validar_fecha("08/10/2026", ahora, parque) == date(2026, 10, 8)


# 1.2 Probar que la fecha de visita sea posterior a la fecha actual. PASA
def test_fecha_posterior_es_valida(ahora, parque):
    assert validar_fecha("09/10/2026", ahora, parque) == date(2026, 10, 9)


# 1.3 Probar que la fecha de visita sea anterior a la fecha actual. FALLA, se debe informar un error
def test_fecha_anterior_informa_error(ahora, parque):
    with pytest.raises(ErrorValidacion, match="anterior"):
        validar_fecha("07/10/2026", ahora, parque)


# 1.4 Probar que la fecha tenga el formato correspondiente (dd/mm/aaaa). PASA
def test_fecha_con_formato_correcto(ahora, parque):
    assert validar_fecha("15/10/2026", ahora, parque) == date(2026, 10, 15)


# 1.5 Probar que la fecha no tenga el formato correspondiente. FALLA
@pytest.mark.parametrize("texto", ["2026-10-15", "15-10-2026", "15/10/26", "31/02/2027", "mañana", ""])
def test_fecha_con_formato_incorrecto(ahora, parque, texto):
    with pytest.raises(ErrorValidacion):
        validar_fecha(texto, ahora, parque)


# 1.6 Probar una fecha correspondiente a un día en que el parque está abierto. PASA
def test_fecha_en_dia_abierto(ahora, parque):
    assert validar_fecha("13/10/2026", ahora, parque) == date(2026, 10, 13)  # martes


# 1.7 Probar una fecha correspondiente a un día en que el parque está cerrado. FALLA
def test_fecha_en_dia_cerrado(ahora, parque):
    with pytest.raises(ErrorValidacion):
        validar_fecha("12/10/2026", ahora, parque)  # lunes


# 1.8 Probar que se cargó la fecha de visita en el formulario. PASA
def test_formulario_tiene_fecha_cargada(datos_validos, parque, ahora):
    entrada = Entrada(**datos_validos)
    entrada.registrar(parque, ahora)
    assert entrada.fecha_entrada == date(2026, 10, 9)


# 1.9 Probar una fecha que corresponde al horario de abierto del parque. PASA
# (comprar para hoy mientras el parque todavía está abierto)
def test_fecha_actual_dentro_del_horario_abierto(parque):
    ahora = datetime(2026, 10, 8, 17, 0)
    assert validar_fecha("08/10/2026", ahora, parque) == date(2026, 10, 8)


# 1.10 Probar una fecha anterior a que pase un mes desde la fecha actual PASA
def test_fecha_antes_de_un_mes_es_valida(ahora, parque):
    assert validar_fecha("07/11/2026", ahora, parque) == date(2026, 11, 7)  # sábado


# 1.11 Probar una fecha posterior a que pase un mes desde la fecha actual FALLA
def test_fecha_despues_de_un_mes_informa_error(ahora, parque):
    with pytest.raises(ErrorValidacion, match="mes"):
        validar_fecha("10/11/2026", ahora, parque)  # martes


# 1.12 Probar para la fecha actual en un horario anterior a las 17:30 PASA
def test_fecha_actual_antes_de_las_17_30(parque):
    ahora = datetime(2026, 10, 8, 17, 29)
    assert validar_fecha("08/10/2026", ahora, parque) == date(2026, 10, 8)


# 1.13 Probar para la fecha actual en el horario 17:30 PASA
def test_fecha_actual_a_las_17_30(parque):
    ahora = datetime(2026, 10, 8, 17, 30)
    assert validar_fecha("08/10/2026", ahora, parque) == date(2026, 10, 8)


# 1.14 Probar para la fecha actual en un horario posterior a las 17:30 FALLA
def test_fecha_actual_despues_de_las_17_30_informa_error(parque):
    ahora = datetime(2026, 10, 8, 17, 31)
    with pytest.raises(ErrorValidacion):
        validar_fecha("08/10/2026", ahora, parque)


# 1.15 Probar una fecha correspondiente a un domingo PASA
def test_fecha_en_domingo_es_valida(ahora, parque):
    assert validar_fecha("11/10/2026", ahora, parque) == date(2026, 10, 11)  # domingo

# 1.16 Probar una fecha correspondiente a un día festivo FALLA
@pytest.mark.parametrize("texto", ["25/12/2026", "01/01/2027"])
def test_fecha_en_dia_festivo_informa_error(ahora, parque, texto):
    with pytest.raises(ErrorValidacion, match="cerrado"):
        validar_fecha(texto, ahora, parque)
