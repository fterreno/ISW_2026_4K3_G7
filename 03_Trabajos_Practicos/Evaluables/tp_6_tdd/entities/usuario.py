from dataclasses import dataclass, field

from entities.entrada import Entrada
from entities.errores import ErrorValidacion


@dataclass
class Usuario:
    nombre: str
    apellido: str
    mail: str
    entradas: list[Entrada] = field(default_factory=list)  # entradas que compró el usuario

    def registrar(self) -> None:
        self.validar_nombre()
        self.validar_apellido()
        self.validar_mail()

    def validar_nombre(self) -> None:
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorValidacion("El nombre no puede estar vacío.")
        self.nombre = self.nombre.strip()

    def validar_apellido(self) -> None:
        if not isinstance(self.apellido, str) or not self.apellido.strip():
            raise ErrorValidacion("El apellido no puede estar vacío.")
        self.apellido = self.apellido.strip()

    def validar_mail(self) -> None:
        """El mail debe tener un usuario antes del @ y un dominio terminado en .com después."""
        if not isinstance(self.mail, str):
            raise ErrorValidacion("El mail debe ser un texto.")
        self.mail = self.mail.strip()

        if self.mail.count("@") != 1:
            raise ErrorValidacion("El mail debe contener un solo @.")

        usuario_mail, dominio = self.mail.split("@")
        if not usuario_mail:
            raise ErrorValidacion("El mail debe tener un usuario antes del @.")
        if not dominio.endswith(".com") or dominio == ".com":
            raise ErrorValidacion("El dominio del mail debe terminar en .com.")

    def agregar_entrada(self, entrada: Entrada) -> None:
        """Agrega una entrada ya validada y pagada a las entradas del usuario."""
        self.entradas.append(entrada)
