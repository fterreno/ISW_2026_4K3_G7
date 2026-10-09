import os

import pytest
from controllers.controller_comprar_entrada import ControllerComprarEntrada
from entities.errores import ErrorPago
from entities.mercado_pago import PasarelaMercadoPago
from conftest import PasarelaEspia, PasarelaFalsa, SDKMercadoPagoSimulado


# Cada test corre contra 3 pasarelas:
# - falsa: doble de prueba, no usa PasarelaMercadoPago
# - simulada: PasarelaMercadoPago con un SDK que imita las respuestas de Mercado Pago (sin conexión)
# - real: PasarelaMercadoPago contra Mercado Pago. Solo corre con MP_PAGO_REAL=1 porque hay que pagar a mano (ver README)
requiere_pago_real = pytest.mark.skipif(
    not os.getenv("MP_ACCESS_TOKEN") or os.getenv("MP_PAGO_REAL") != "1",
    reason="Solo corre con MP_ACCESS_TOKEN y MP_PAGO_REAL=1 porque requiere pagar a mano en el navegador",
)

# Mercado Pago no acepta tarjeta para montos muy bajos, así que en los pagos reales se cobran $1000
MONTO_PAGO_REAL = 1000.0

PAGO_APROBADO = {"id": 1, "status": "approved", "status_detail": "accredited"}
PAGO_SIN_SALDO = {"id": 2, "status": "rejected", "status_detail": "cc_rejected_insufficient_amount"}


@pytest.fixture(params=["falsa", "simulada", pytest.param("real", marks=requiere_pago_real)])
def crear_pasarela(request):
    # titular de la tarjeta de prueba: APRO aprueba el pago y FUND lo rechaza por saldo insuficiente
    def crear(titular):
        if request.param == "falsa":
            return PasarelaFalsa(error=None if titular == "APRO" else "Saldo insuficiente")
        # PasarelaMercadoPago es singleton: se reinicia para crearla con la configuración de cada test
        PasarelaMercadoPago.reiniciar()
        if request.param == "simulada":
            pago = PAGO_APROBADO if titular == "APRO" else PAGO_SIN_SALDO
            return PasarelaEspia(PasarelaMercadoPago(sdk=SDKMercadoPagoSimulado(pago), abrir_url=lambda url: None))
        # No se abre el navegador por defecto porque suele tener la sesión real de Mercado Pago:
        # el link se abre a mano en incógnito con el comprador de prueba
        avisar = lambda url: print(f"\nAbrí este link en incógnito y pagá con titular {titular}: {url}", flush=True)
        return PasarelaEspia(PasarelaMercadoPago(timeout_segundos=300, abrir_url=avisar))
    return crear


@pytest.fixture
def pasarela_aprobada(crear_pasarela):
    return crear_pasarela("APRO")


@pytest.fixture
def pasarela_sin_saldo(crear_pasarela):
    return crear_pasarela("FUND")


# 6.1 Probar que al confirmar una compra con tarjeta se redirija a Mercado Pago. PASA
def test_compra_con_tarjeta_redirige_a_mercado_pago(datos_validos, ahora, parque, destinatario, pasarela_aprobada, servicio_mail):
    controller = ControllerComprarEntrada(destinatario, parque, pasarela=pasarela_aprobada, servicio_mail=servicio_mail)
    controller.comprar_entrada(**datos_validos, ahora=ahora)
    assert pasarela_aprobada.pagos == [controller.entrada]


# 6.2 Probar un pago rechazado por falta de saldo. FALLA la operación de pago, se debe informar el problema
def test_pago_rechazado_por_falta_de_saldo(datos_validos, ahora, parque, destinatario, pasarela_sin_saldo, servicio_mail):
    controller = ControllerComprarEntrada(destinatario, parque, pasarela=pasarela_sin_saldo, servicio_mail=servicio_mail)
    with pytest.raises(ErrorPago, match="Saldo insuficiente"):
        controller.comprar_entrada(**datos_validos, ahora=ahora)


# 6.3 Probar que, si el pago no se confirma, no se envíe el mail de confirmación. PASA si no se envía el mail
def test_pago_no_confirmado_no_envia_mail(datos_validos, ahora, parque, destinatario, pasarela_sin_saldo, servicio_mail):
    controller = ControllerComprarEntrada(destinatario, parque, pasarela=pasarela_sin_saldo, servicio_mail=servicio_mail)
    with pytest.raises(ErrorPago):
        controller.comprar_entrada(**datos_validos, ahora=ahora)
    assert servicio_mail.enviados == []


# Crea una preferencia real en Mercado Pago (no cobra nada, solo genera el link de pago)
@pytest.mark.skipif(not os.getenv("MP_ACCESS_TOKEN"), reason="Falta MP_ACCESS_TOKEN en el .env")
def test_crear_preferencia_real(entrada):
    entrada.monto_total = MONTO_PAGO_REAL
    PasarelaMercadoPago.reiniciar()
    pasarela = PasarelaMercadoPago()
    url = pasarela.crear_preferencia(entrada, referencia="test-preferencia")
    assert url.startswith("https://")
    assert "mercadopago" in url
