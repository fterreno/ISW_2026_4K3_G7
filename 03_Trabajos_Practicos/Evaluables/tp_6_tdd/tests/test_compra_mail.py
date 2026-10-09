import os
from unittest.mock import MagicMock

import pytest
from controllers.controller_comprar_entrada import ControllerComprarEntrada
from entities.errores import ErrorMail
from entities.forma_pago import FormaPago
from entities.mail import AdaptadorMailGmail
from entities.usuario import Usuario


# Es para utilizar un servidor falso al correr cada test. Para hacer una prueba con el test real mirar README
@pytest.fixture
def servidor_smtp():
    """Reemplaza a smtplib.SMTP_SSL: no se conecta a Gmail, solo registra las llamadas."""
    smtp_ssl = MagicMock()
    adaptador = AdaptadorMailGmail(cliente_smtp=smtp_ssl, usuario="ecoharmony@gmail.com", contrasena="clave-de-prueba")
    # El servidor que se obtiene con "with smtplib.SMTP_SSL(...) as servidor"
    servidor = smtp_ssl.return_value.__enter__.return_value
    return adaptador, servidor


# 7.1 Probar que una compra confirmada envíe el mail de confirmación. PASA
@pytest.mark.skipif(os.getenv("ENVIAR_MAIL_REAL") != "1", reason="Solo corre con ENVIAR_MAIL_REAL=1 para no mandar mails en cada ejecución")
def test_enviar_mail_real(entrada, pasarela_aprobada):
    usuario = Usuario(nombre="Florencia", apellido="Terreno", mail="terrenoflorencia13@gmail.com")
    entrada.forma_pago = FormaPago.EFECTIVO
    controller = ControllerComprarEntrada(usuario, pasarela=pasarela_aprobada)
    controller.entrada = entrada
    assert controller.servicio_mail.enviar(controller.generar_mail()) is True


# 7.2 Probar el envío de un mail de confirmación vacío. FALLA
def test_mail_vacio_no_se_envia(destinatario, pasarela_aprobada, servicio_mail):
    controller = ControllerComprarEntrada(destinatario, pasarela=pasarela_aprobada, servicio_mail=servicio_mail)
    controller.entrada = None
    with pytest.raises(ErrorMail):
        controller.enviar_mail()
