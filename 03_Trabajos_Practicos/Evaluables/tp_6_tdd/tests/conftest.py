import pytest
from datetime import date, datetime, time
from formulario_entrada import FormaPago, FormularioEntrada, HorarioParque, TipoPase
from compra_entradas import ResultadoPago


class PasarelaFalsa:
    """Reemplaza a Mercado Pago en los tests: no cobra nada, devuelve el resultado
    que le indiquemos y registra cada pago que se le pidió."""

    def __init__(self, resultado: ResultadoPago):
        self.resultado = resultado
        self.pagos = []

    def pagar(self, formulario):
        self.pagos.append(formulario)
        return self.resultado


class ServicioMailFalso:
    """Reemplaza al servidor de mail: no envía nada, solo guarda los mails."""

    def __init__(self):
        self.enviados = []

    def enviar(self, mail):
        self.enviados.append(mail)


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


@pytest.fixture
def formulario():
    # Formulario ya validado: 2 entradas para el viernes 09/10/2026, pago con tarjeta
    return FormularioEntrada(
        fecha=date(2026, 10, 9),
        cantidad=2,
        edades=[30, 8],
        tipo_pase=TipoPase.REGULAR,
        forma_pago=FormaPago.TARJETA,
    )


@pytest.fixture
def destinatario():
    # Mail con el que se registró el visitante
    return "visitante@mail.com"


@pytest.fixture
def pasarela_aprobada():
    return PasarelaFalsa(ResultadoPago(aprobado=True))


@pytest.fixture
def pasarela_sin_saldo():
    return PasarelaFalsa(ResultadoPago(aprobado=False, motivo="Saldo insuficiente"))


@pytest.fixture
def servicio_mail():
    return ServicioMailFalso()
