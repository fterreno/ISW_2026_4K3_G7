import os
import time
import uuid
import webbrowser

import mercadopago
from dotenv import load_dotenv

from entities.entrada import Entrada
from entities.errores import ErrorPago

load_dotenv()
MP_ACCESS_TOKEN = os.getenv('MP_ACCESS_TOKEN')
# mail del comprador de prueba: si está cargado, el checkout no pide el mail (ver .env.example)
MP_EMAIL_COMPRADOR_PRUEBA = os.getenv('MP_EMAIL_COMPRADOR_PRUEBA')


# Motivos de rechazo que devuelve Mercado Pago en "status_detail"
MOTIVOS_RECHAZO = {
    'cc_rejected_insufficient_amount': 'Saldo insuficiente',
    'cc_rejected_bad_filled_security_code': 'Código de seguridad inválido',
    'cc_rejected_bad_filled_date': 'Fecha de vencimiento inválida',
    'cc_rejected_bad_filled_other': 'Datos de la tarjeta inválidos',
    'cc_rejected_call_for_authorize': 'El pago debe ser autorizado por el emisor de la tarjeta',
}


class PasarelaMercadoPago:
    """Singleton: hay una sola conexión con Mercado Pago en toda la aplicación.
    Cobra con Checkout Pro: crea la preferencia, abre el checkout en el navegador
    y consulta a Mercado Pago hasta que el pago se apruebe o se rechace."""

    _instancia = None

    def __new__(cls, *args, **kwargs):
        # siempre se devuelve la misma instancia; se crea solo la primera vez
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializada = False
        return cls._instancia

    def __init__(self, access_token: str | None = None, sdk=None, abrir_url=webbrowser.open,
                 intervalo_segundos: float = 3, timeout_segundos: float = 60):
        # __init__ se ejecuta en cada PasarelaMercadoPago(), pero la configuración se carga una sola vez
        if self._inicializada:
            return

        access_token = access_token or MP_ACCESS_TOKEN
        if sdk is None and not access_token:
            raise ErrorPago('Falta configurar MP_ACCESS_TOKEN en el archivo .env')
        self.access_token = access_token or ''
        self.sdk = sdk or mercadopago.SDK(access_token)
        self.abrir_url = abrir_url
        self.intervalo_segundos = intervalo_segundos
        self.timeout_segundos = timeout_segundos
        self._inicializada = True

    @classmethod
    def reiniciar(cls) -> None:
        """Descarta la instancia actual; los tests lo usan para crear la pasarela con otra configuración."""
        cls._instancia = None

    def configurar_apertura(self, abrir_url) -> None:
        """Cambia cómo se abre el checkout, por ejemplo en el navegador del celular en vez del de la computadora."""
        self.abrir_url = abrir_url

    def crear_preferencia(self, entrada: Entrada, referencia: str) -> str:
        """Crea la preferencia de pago y devuelve la URL del checkout."""
        preferencia = {
            'items': [{
                'title': f'EcoHarmony Park - {entrada.cantidad} entradas {entrada.tipo_pase.value} para el {entrada.fecha_entrada:%d/%m/%Y}',
                'quantity': 1,
                'currency_id': 'ARS',
                'unit_price': float(entrada.monto_total),
            }],
            'external_reference': referencia,
        }
        if MP_EMAIL_COMPRADOR_PRUEBA:
            preferencia['payer'] = {'email': MP_EMAIL_COMPRADOR_PRUEBA}
        respuesta = self.sdk.preference().create(preferencia)
        if respuesta['status'] not in (200, 201):
            raise ErrorPago(f"No se pudo crear el pago en Mercado Pago: {respuesta['response']}")

        datos = respuesta['response']
        # Las credenciales de prueba (TEST-...) usan el checkout sandbox
        if self.access_token.startswith('TEST-'):
            return datos['sandbox_init_point']
        return datos['init_point']

    def buscar_pago(self, referencia: str) -> dict | None:
        """Devuelve el último pago asociado a la referencia, o None si todavía no se pagó."""
        respuesta = self.sdk.payment().search({
            'external_reference': referencia,
            'sort': 'date_created',
            'criteria': 'desc',
        })
        if respuesta['status'] != 50:
            raise ErrorPago(f"No se pudo consultar el pago en Mercado Pago: {respuesta['response']}")
        resultados = respuesta['response'].get('results', [])
        return resultados[0] if resultados else None

    def cobrar(self, entrada: Entrada) -> dict:
        referencia = str(uuid.uuid4())
        self.abrir_url(self.crear_preferencia(entrada, referencia))

        limite = time.monotonic() + self.timeout_segundos
        while time.monotonic() < limite:
            pago = self.buscar_pago(referencia)
            if pago is not None:
                if pago['status'] == 'approved':
                    return pago
                if pago['status'] in ('rejected', 'cancelled'):
                    raise ErrorPago(MOTIVOS_RECHAZO.get(pago.get('status_detail'), 'Pago rechazado'))
            time.sleep(self.intervalo_segundos)

        raise ErrorPago('El pago no se confirmó a tiempo')
