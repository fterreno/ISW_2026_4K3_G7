import pytest
from compra_entradas import ErrorPago, confirmar_compra


# 6.1 Probar que al confirmar una compra con tarjeta se redirija a Mercado Pago. PASA
def test_compra_con_tarjeta_redirige_a_mercado_pago(formulario, destinatario, pasarela_aprobada, servicio_mail):
    confirmar_compra(formulario, destinatario, pasarela_aprobada, servicio_mail)
    assert pasarela_aprobada.pagos == [formulario]


# 6.2 Probar un pago rechazado por falta de saldo. FALLA la operación de pago, se debe informar el problema
def test_pago_rechazado_por_falta_de_saldo(formulario, destinatario, pasarela_sin_saldo, servicio_mail):
    with pytest.raises(ErrorPago, match="Saldo insuficiente"):
        confirmar_compra(formulario, destinatario, pasarela_sin_saldo, servicio_mail)


# 6.3 Probar que, si el pago no se confirma, no se envíe el mail de confirmación. PASA si no se envía el mail
def test_pago_no_confirmado_no_envia_mail(formulario, destinatario, pasarela_sin_saldo, servicio_mail):
    with pytest.raises(ErrorPago):
        confirmar_compra(formulario, destinatario, pasarela_sin_saldo, servicio_mail)
    assert servicio_mail.enviados == []
