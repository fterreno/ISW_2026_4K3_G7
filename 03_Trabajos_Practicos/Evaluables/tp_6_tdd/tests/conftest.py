import pytest
from datetime import datetime, time
from formulario_entrada import HorarioParque

@pytest.fixture
def ahora():
    # Fecha y hora fija para que los tests no dependan del día en que se corren:
    # jueves 08/10/2026 a las 10:00
    return datetime(2026, 10, 8, 10, 0)


@pytest.fixture
def horario():
    # Supuesto: el parque abre de martes a domingo (cierra los lunes) de 9 a 18 hs
    return HorarioParque(dias_abiertos={1, 2, 3, 4, 5, 6}, hora_apertura=time(9, 0), hora_cierre=time(18, 0))


@pytest.fixture
def datos_validos(ahora, horario):
    return dict(
        fecha="09/10/2026",
        cantidad=2,
        edades=[30, 8],
        tipo_pase="Regular",
        forma_pago="Tarjeta",
        ahora=ahora,
        horario=horario,
    )
