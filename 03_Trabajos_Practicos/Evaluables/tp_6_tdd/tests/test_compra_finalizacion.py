from datetime import date
from compra_entradas import registrar_compra


# 8.1 Probar que al finalizar una compra correcta se informe la cantidad de entradas compradas y la fecha de visita. PASA
def test_compra_finalizada_informa_cantidad_fecha(formulario, destinatario, pasarela_aprobada, servicio_mail):
    resultado = registrar_compra(formulario, destinatario, pasarela_aprobada, servicio_mail)
    assert resultado.cantidad == 2
    assert resultado.fecha == date(2026, 10, 9)
    assert "2 entradas" in resultado.mensaje
    assert "09/10/2026" in resultado.mensaje
