import os
import time
import uuid
import webbrowser

import mercadopago
from dotenv import load_dotenv
from formulario_entrada import ErrorPago, FormularioEntrada

load_dotenv()
MP_ACCESS_TOKEN = os.getenv('MP_ACCESS_TOKEN')


# Motivos de rechazo que devuelve Mercado Pago en "status_detail"
MOTIVOS_RECHAZO = {
    'cc_rejected_insufficient_amount': 'Saldo insuficiente',
    'cc_rejected_bad_filled_security_code': 'Código de seguridad inválido',
    'cc_rejected_bad_filled_date': 'Fecha de vencimiento inválida',
    'cc_rejected_bad_filled_other': 'Datos de la tarjeta inválidos',
    'cc_rejected_call_for_authorize': 'El pago debe ser autorizado por el emisor de la tarjeta',
}


class PasarelaMercadoPago:
    """Cobra con Checkout Pro: crea la preferencia, abre el checkout en el navegador
    y consulta a Mercado Pago hasta que el pago se apruebe o se rechace."""

    def __init__(self, access_token: str | None = None, sdk=None, abrir_url=webbrowser.open,
                 intervalo_segundos: float = 3, timeout_segundos: float = 600):
        access_token = access_token or MP_ACCESS_TOKEN
        if sdk is None and not access_token:
            raise ErrorPago('Falta configurar MP_ACCESS_TOKEN en el archivo .env')
        self.access_token = access_token or ''
        self.sdk = sdk or mercadopago.SDK(access_token)
        self.abrir_url = abrir_url
        self.intervalo_segundos = intervalo_segundos
        self.timeout_segundos = timeout_segundos

    def crear_preferencia(self, formulario: FormularioEntrada, referencia: str) -> str:
        """Crea la preferencia de pago y devuelve la URL del checkout."""
        preferencia = {
            'items': [{
                'title': f'EcoHarmony Park - {formulario.cantidad} entradas {formulario.tipo_pase.value} para el {formulario.fecha:%d/%m/%Y}',
                'quantity': 1,
                'currency_id': 'ARS',
                'unit_price': float(formulario.detalle_compra.monto_total),
            }],
            'external_reference': referencia,
        }
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
        if respuesta['status'] != 200:
            raise ErrorPago(f"No se pudo consultar el pago en Mercado Pago: {respuesta['response']}")
        resultados = respuesta['response'].get('results', [])
        return resultados[0] if resultados else None

    def cobrar(self, formulario: FormularioEntrada) -> dict:
        referencia = str(uuid.uuid4())
        self.abrir_url(self.crear_preferencia(formulario, referencia))

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
