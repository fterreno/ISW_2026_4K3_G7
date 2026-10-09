from abc import ABC, abstractmethod
from email.message import EmailMessage
import os
import smtplib

from dotenv import load_dotenv

load_dotenv()
MAIL_ECOHARMONY = os.getenv('MAIL_ECOHARMONY')
MAIL_CONTRASENA_ECOHARMONY = os.getenv('MAIL_CONTRASENA_ECOHARMONY')


class ServicioMail(ABC):
    """Target del adaptador: la interfaz que espera el controller para mandar un mail."""

    @abstractmethod
    def enviar(self, mensaje: EmailMessage) -> bool:
        """Envía el mensaje y devuelve True si se pudo enviar."""


class AdaptadorMailGmail(ServicioMail):
    """Adapter: traduce enviar(mensaje) a la interfaz de smtplib (el adaptado),
    que necesita conectarse al servidor, iniciar sesión y recién ahí mandar el mensaje."""

    def __init__(self, cliente_smtp=smtplib.SMTP_SSL, servidor: str = 'smtp.gmail.com', puerto: int = 465,
                 usuario: str | None = MAIL_ECOHARMONY, contrasena: str | None = MAIL_CONTRASENA_ECOHARMONY):
        # el cliente smtp se recibe por parámetro para poder reemplazarlo en los tests
        self.cliente_smtp = cliente_smtp
        self.servidor = servidor
        self.puerto = puerto
        self.usuario = usuario
        self.contrasena = contrasena

    def enviar(self, mensaje: EmailMessage) -> bool:
        # el remitente es la cuenta del parque, que solo conoce el adaptador
        if mensaje['From'] is None:
            mensaje['From'] = self.usuario
        try:
            with self.cliente_smtp(self.servidor, self.puerto) as conexion:
                conexion.login(self.usuario, self.contrasena)
                conexion.send_message(mensaje)
            return True
        except Exception as error:
            print(f"Error al enviar: {error}")
            return False
