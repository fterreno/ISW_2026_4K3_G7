import pytest
from datetime import date, datetime, time
from formulario_entrada import DetalleCompra, ErrorPago, FormaPago, FormularioEntrada, HorarioParque, TipoPase, Usuario


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
        detalle_compra=DetalleCompra(monto_total=1.0, fecha_compra=date(2026, 10, 8)),
        usuario=Usuario(mail="terrenoflorencia13@gmail.com", nombre="Ana", apellido="Pérez"),
    )


# Dobles de prueba para no cobrar ni mandar mails en cada ejecución.
# La pasarela real es PasarelaMercadoPago (ver test_mercado_pago_real.py)
class PasarelaFalsa:
    def __init__(self, error: str | None = None):
        self.error = error
        self.pagos = []

    def cobrar(self, formulario):
        if self.error:
            raise ErrorPago(self.error)
        self.pagos.append(formulario)
        return {"status": "approved"}


class ServicioMailFalso:
    def __init__(self):
        self.enviados = []

    def enviar(self, formulario):
        self.enviados.append(formulario)
        return True


@pytest.fixture
def destinatario():
    return Usuario(mail="terrenoflorencia13@gmail.com", nombre="Ana", apellido="Pérez")


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
    """Envuelve una pasarela de verdad y guarda los formularios cobrados, igual que PasarelaFalsa."""

    def __init__(self, pasarela):
        self.pasarela = pasarela
        self.pagos = []

    def cobrar(self, formulario):
        pago = self.pasarela.cobrar(formulario)
        self.pagos.append(formulario)
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
