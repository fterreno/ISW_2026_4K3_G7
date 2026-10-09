import os
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
from formulario_entrada import FormaPago, FormularioEntrada

load_dotenv()
MAIL_ECOHARMONY = os.getenv('MAIL_ECOHARMONY')
MAIL_CONTRASENA_ECOHARMONY = os.getenv('MAIL_CONTRASENA_ECOHARMONY')


class ErrorPago(Exception):
    """Se lanza cuando Mercado Pago rechaza el pago."""


class ErrorMail(Exception):
    """Se lanza cuando se intenta enviar un mail inválido (por ejemplo, vacío)."""


def generar_mail(formulario: FormularioEntrada) -> EmailMessage:
    cuerpo_pago = ''
    mensaje = EmailMessage()
    mensaje['Subject'] = 'EcoHarmony Park: Compra Confirmada'
    mensaje['From'] = MAIL_ECOHARMONY
    mensaje['To'] = formulario.usuario.mail

    if formulario.forma_pago == FormaPago.EFECTIVO:
        cuerpo_pago = '<small>Se informa que, al haber seleccionado la modalidad de pago en efectivo, deberá abonar el importe total correspondiente a su reserva al momento de ingresar al parque. En caso de no efectuarse el pago, el parque se reserva el derecho de admisión del visitante.</small>'
    
    cuerpo_html = f"""
    <html>
    <body>
        <h1 style="text-align: center;">¡Gracias por comprar en EcoHarmony Park!</h1>
        <p>Buenos días {formulario.usuario.apellido} {formulario.usuario.nombre}, gracias por comprar en EcoHarmony Park.</p>
        <p>Gracias por su compra. En el archivo adjunto se encuentra generado un pdf con las entradas que se le solicitaran a la entrada de EcoHarmony Park.</p>
        <br>
        <p style="margin-left: 40px;"> Tipo de pase: {formulario.tipo_pase.value}</p>
        <p style="margin-left: 40px;"> Cantidad de entradas compradas: {formulario.cantidad}</p>
        <p style="margin-left: 40px;"> Forma de Pago: {formulario.forma_pago.value}</p>
        <p style="margin-left: 40px;"> Total: $ {formulario.detalle_compra.monto_total}</p>
        <br>
        <p>Saludos desde EcoHarmony Park.</p>
        {cuerpo_pago}
    </body>
    </html>
    """
    mensaje.add_alternative(cuerpo_html, subtype='html')
    return mensaje


def enviar_mail(formulario: FormularioEntrada) -> bool:
    mensaje = generar_mail(formulario) 
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(MAIL_ECOHARMONY, MAIL_CONTRASENA_ECOHARMONY)
            servidor.send_message(mensaje)
        return True
    except Exception as error:
        print(f"Error al enviar: {error}")
        return False
    

# aca simplemente se encargar de generar el mail y enviarlo y llamar a la pasarela de mercado pago de ser necesario
def registrar_compra(formulario: FormularioEntrada) -> None:
    mail_enviado = enviar_mail(formulario)
    if not mail_enviado:
        # avisar al usuario que no se envio el mail
        raise NotImplementedError

# abria que fijarse de crear una funcion extra para mercado pago prob