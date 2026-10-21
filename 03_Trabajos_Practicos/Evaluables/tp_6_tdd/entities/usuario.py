from dataclasses import dataclass, field

from entities.entrada import Entrada
from entities.errores import ErrorValidacion, ErroresValidacion, validar_campo


@dataclass
class Usuario:
    nombre: str
    apellido: str
    mail: str
    entradas: list[Entrada] = field(default_factory=list)  # entradas que compró el usuario

    def registrar(self) -> None:
        """Valida todos los datos y, si hay errores, los informa todos juntos."""
        errores: list[ErrorValidacion] = []
        validar_campo("nombre", self.validar_nombre, errores)
        validar_campo("apellido", self.validar_apellido, errores)
        validar_campo("mail", self.validar_mail, errores)
        if errores:
            raise ErroresValidacion(errores)

    def validar_nombre(self) -> None:
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorValidacion("El nombre no puede estar vacío.")
        self.nombre = self.nombre.strip()
        if not self.nombre.replace(" ", "").isalpha():
            raise ErrorValidacion("Debe ingresar caracteres validos")

    def validar_apellido(self) -> None:
        if not isinstance(self.apellido, str) or not self.apellido.strip():
            raise ErrorValidacion("El apellido no puede estar vacío.")
        self.apellido = self.apellido.strip()
        if not self.apellido.replace(" ", "").isalpha():
            raise ErrorValidacion("Debe ingresar caracteres validos")

    def validar_mail(self) -> None:
        """El mail debe tener un usuario antes del @ y un dominio terminado en .com después."""
        if not isinstance(self.mail, str):
            raise ErrorValidacion("El mail debe ser un texto.")
        self.mail = self.mail.strip()

        if self.mail.count("@") != 1:
            raise ErrorValidacion("Ingrese un mail valido")

        usuario_mail, dominio = self.mail.split("@")
        if not usuario_mail:
            raise ErrorValidacion("Ingrese un mail valido")
        if not dominio.endswith(".com") or dominio == ".com":
            raise ErrorValidacion("Ingrese un mail valido")

    def agregar_entrada(self, entrada: Entrada) -> None:
        """Agrega una entrada ya validada y pagada a las entradas del usuario."""
        self.entradas.append(entrada)
