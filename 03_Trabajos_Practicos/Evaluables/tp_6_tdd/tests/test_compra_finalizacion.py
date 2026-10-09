from datetime import date
from controllers.controller_comprar_entrada import ControllerComprarEntrada


# 8.1 Probar que al finalizar una compra correcta se informe la cantidad de entradas compradas y la fecha de visita. PASA
def test_compra_finalizada_informa_cantidad_fecha(datos_validos, ahora, parque, destinatario, pasarela_aprobada, servicio_mail):
    controller = ControllerComprarEntrada(destinatario, parque, pasarela=pasarela_aprobada, servicio_mail=servicio_mail)
    resultado = controller.comprar_entrada(**datos_validos, ahora=ahora)
    assert resultado.cantidad == 2
    assert resultado.fecha_entrada == date(2026, 10, 9)
    # el mensaje que se le informa al usuario es el mail de confirmación
    mensaje = servicio_mail.enviados[0].get_body(preferencelist=("html",)).get_content()
    assert "Cantidad de entradas compradas: 2" in mensaje
    assert "Fecha de visita: 09/10/2026" in mensaje
