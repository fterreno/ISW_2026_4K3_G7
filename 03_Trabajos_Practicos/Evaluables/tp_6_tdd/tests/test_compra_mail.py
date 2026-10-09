import pytest
from compra_entradas import ErrorMail, Mail, generar_mail, registrar_compra, enviar_mail


# 7.1 Probar que una compra confirmada envíe el mail de confirmación. PASA
def test_compra_confirmada_envia_mail(formulario, destinatario, pasarela_aprobada, servicio_mail):
    registrar_compra(formulario, destinatario, pasarela_aprobada, servicio_mail)
    assert len(servicio_mail.enviados) == 1
    assert servicio_mail.enviados[0].destinatario == destinatario


# 7.2 Probar que el mail enviado tenga el contenido y formato esperado. PASA
def test_mail_tiene_contenido_formato_esperado(formulario, destinatario):
    mail = generar_mail(formulario, destinatario)
    assert mail.destinatario == "visitante@mail.com"
    assert mail.asunto == "Confirmación de compra - EcoHarmony Park"
    assert "Fecha de visita: 09/10/2026" in mail.cuerpo
    assert "Cantidad de entradas: 2" in mail.cuerpo
    assert "Tipo de pase: Regular" in mail.cuerpo
    assert "Forma de pago: Tarjeta" in mail.cuerpo


# 7.3 Probar el envío de un mail de confirmación vacío. FALLA
@pytest.mark.parametrize("asunto, cuerpo", [("", ""), ("Confirmación de compra - EcoHarmony Park", ""), ("", "Fecha de visita: 09/10/2026")],)
def test_mail_vacio_no_se_envia(destinatario, servicio_mail, asunto, cuerpo):
    with pytest.raises(ErrorMail):
        enviar_mail(Mail(destinatario, asunto, cuerpo), servicio_mail)
    assert servicio_mail.enviados == []
