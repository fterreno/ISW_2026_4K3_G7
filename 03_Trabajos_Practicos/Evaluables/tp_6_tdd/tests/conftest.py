import pytest
from datetime import date, datetime, time
from entities.entrada import Entrada
from entities.errores import ErrorPago
from entities.forma_pago import FormaPago
from entities.parque import Parque
from entities.tipo_pase import TipoPase
from entities.usuario import Usuario


@pytest.fixture
def ahora():
    # Fecha y hora fija para que los tests no dependan del día en que se corren:
    # jueves 08/10/2026 a las 10:00
    return datetime(2026, 10, 8, 10, 0)


@pytest.fixture
def parque():
    # Supuesto: el parque abre de martes a domingo (cierra los lunes) de 9 a 18 hs
    return Parque(dias_abiertos={1, 2, 3, 4, 5, 6}, hora_apertura=time(9, 0), hora_cierre=time(18, 0))


@pytest.fixture
def datos_validos():
    return dict(
        fecha_entrada="09/10/2026",
        cantidad=2,
        edades=[30, 15],
        tipo_pase="Regular",
        forma_pago="Tarjeta",
    )


@pytest.fixture
def entrada():
    # Entrada ya validada: 2 entradas para el viernes 09/10/2026, pago con tarjeta
    return Entrada(
        fecha_entrada=date(2026, 10, 9),
        cantidad=2,
        edades=[30, 15],
        tipo_pase=TipoPase.REGULAR,
        forma_pago=FormaPago.TARJETA,
        monto_total=1.0,
        fecha_compra=date(2026, 10, 8),
    )


# Dobles de prueba para no cobrar ni mandar mails en cada ejecución.
# La pasarela real es PasarelaMercadoPago (ver test_mercado_pago_real.py)
class PasarelaFalsa:
    def __init__(self, error: str | None = None):
        self.error = error
        self.pagos = []

    def cobrar(self, entrada):
        if self.error:
            raise ErrorPago(self.error)
        self.pagos.append(entrada)
        return {"status": "approved"}


class ServicioMailFalso:
    def __init__(self):
        self.enviados = []

    def enviar(self, mensaje):
        self.enviados.append(mensaje)
        return True


@pytest.fixture
def destinatario():
    return Usuario(nombre="Ana", apellido="Pérez", mail="terrenoflorencia13@gmail.com")


@pytest.fixture
def pasarela_aprobada():
    return PasarelaFalsa()


@pytest.fixture
def pasarela_sin_saldo():
    return PasarelaFalsa(error="Saldo insuficiente")


@pytest.fixture
def servicio_mail():
    return ServicioMailFalso()


class PasarelaEspia:
    """Envuelve una pasarela de verdad y guarda las entradas cobradas, igual que PasarelaFalsa."""

    def __init__(self, pasarela):
        self.pasarela = pasarela
        self.pagos = []

    def cobrar(self, entrada):
        pago = self.pasarela.cobrar(entrada)
        self.pagos.append(entrada)
        return pago


class SDKMercadoPagoSimulado:
    """Imita las respuestas del SDK de Mercado Pago para usar PasarelaMercadoPago sin conexión.
    El mismo objeto responde a sdk.preference().create(...) y a sdk.payment().search(...)."""

    def __init__(self, pago: dict):
        self.pago = pago

    def preference(self):
        return self

    def payment(self):
        return self

    def create(self, preferencia):
        url = "https://www.mercadopago.com.ar/checkout/simulado"
        return {"status": 201, "response": {"init_point": url, "sandbox_init_point": url}}

    def search(self, filtros):
        return {"status": 200, "response": {"results": [self.pago]}}


def crear_entrada(fecha_entrada=None, cantidad=None, edades=None, tipo_pase=None, forma_pago=None):
    """Crea una entrada sin validar con solo los datos que necesita cada test."""
    return Entrada(fecha_entrada, cantidad, edades if edades is not None else [], tipo_pase, forma_pago)
