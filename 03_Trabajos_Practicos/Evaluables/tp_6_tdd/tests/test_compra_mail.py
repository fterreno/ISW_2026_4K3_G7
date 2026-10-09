import os
from unittest.mock import MagicMock

import pytest
import compra_entradas
from compra_entradas import ErrorMail, enviar_mail
from formulario_entrada import FormaPago, Usuario


# Es para utilizar un servidor falso al correr cada test. Para hacer una prueba con el test real mirar README
@pytest.fixture
def servidor_smtp(monkeypatch):
    """Reemplaza a smtplib.SMTP_SSL: no se conecta a Gmail, solo registra las llamadas."""
    monkeypatch.setattr(compra_entradas, "MAIL_ECOHARMONY", "ecoharmony@gmail.com")
    monkeypatch.setattr(compra_entradas, "MAIL_CONTRASENA_ECOHARMONY", "clave-de-prueba")
    smtp_ssl = MagicMock()
    monkeypatch.setattr(compra_entradas.smtplib, "SMTP_SSL", smtp_ssl)
    # El servidor que se obtiene con "with smtplib.SMTP_SSL(...) as servidor"
    servidor = smtp_ssl.return_value.__enter__.return_value
    return smtp_ssl, servidor


# 7.1 Probar que una compra confirmada envíe el mail de confirmación. PASA
@pytest.mark.skipif(os.getenv("ENVIAR_MAIL_REAL") != "1", reason="Solo corre con ENVIAR_MAIL_REAL=1 para no mandar mails en cada ejecución")
def test_enviar_mail_real(formulario):
    formulario.usuario = Usuario(mail="terrenoflorencia13@gmail.com", nombre="Florencia", apellido="Terreno")
    formulario.forma_pago = FormaPago.EFECTIVO
    assert enviar_mail(formulario) is True


# 7.2 Probar el envío de un mail de confirmación vacío. FALLA
@pytest.mark.parametrize("asunto, cuerpo", [("", ""), ("Confirmación de compra - EcoHarmony Park", ""), ("", "Fecha de visita: 09/10/2026")],)
def test_mail_vacio_no_se_envia(destinatario, servicio_mail, asunto, cuerpo):
    with pytest.raises(ErrorMail):
        enviar_mail(Mail(destinatario, asunto, cuerpo), servicio_mail)
    assert servicio_mail.enviados == []
