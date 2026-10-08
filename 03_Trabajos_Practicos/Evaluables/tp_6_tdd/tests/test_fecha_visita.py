from datetime import date

import pytest

from formulario_entrada import ErrorValidacion, validar_fecha_visita


def test_fecha_visita_actual_es_valida():
    hoy = date(2026, 10, 8)

    assert validar_fecha_visita(hoy, hoy) == hoy


def test_fecha_visita_futura_es_valida():
    hoy = date(2026, 10, 8)
    fecha = date(2026, 10, 9)

    assert validar_fecha_visita(fecha, hoy) == fecha


def test_fecha_visita_pasada_informa_error():
    hoy = date(2026, 10, 8)
    fecha = date(2026, 10, 7)

    with pytest.raises(ErrorValidacion, match="anterior"):
        validar_fecha_visita(fecha, hoy)
