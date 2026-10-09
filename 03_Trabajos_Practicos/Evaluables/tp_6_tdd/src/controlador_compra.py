from formulario_entrada import registrar_formulario, registrar_compra

def comprar_entradas(datos, destinatario, pasarela, servicio_mail, fyh_actual, horario):
    formulario = registrar_formulario(**datos, ahora=fyh_actual, horario=horario)

    return registrar_compra(formulario, destinatario, pasarela, servicio_mail)