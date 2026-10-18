import flet as ft

from assets.style import tema
from boundaries.pantalla_formulario_entrada import PantallaFormularioEntrada
from entities.parque import Parque
from entities.usuario import Usuario
from entities.errores import ErrorValidacion, ErroresValidacion


class PantallaInicio:
    """Landing page: pide los datos del usuario y lo lleva al formulario para comprar la entrada."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.usuario: Usuario | None = None  # se conserva para no volver a pedir los datos al volver al inicio
        self.campo_nombre = ft.TextField(label="Nombre", prefix_icon=ft.Icons.PERSON, width=350, error_max_lines=3)
        self.campo_apellido = ft.TextField(label="Apellido", prefix_icon=ft.Icons.PERSON_OUTLINE, width=350, error_max_lines=3)
        self.campo_mail = ft.TextField(label="Mail", prefix_icon=ft.Icons.EMAIL, keyboard_type=ft.KeyboardType.EMAIL, width=350, error_max_lines=3)
        self.texto_error = ft.Text(color=tema.ROJO, text_align=ft.TextAlign.CENTER)  # errores que no son de un campo

    def mostrar(self) -> None:
        self.page.clean()
        self.page.add(
            ft.SafeArea(
                expand=True,
                content=ft.Container(
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        tight=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=16,
                        controls=[
                            ft.Image(src=tema.LOGO, width=120, fit=ft.BoxFit.CONTAIN, color=tema.VERDE_OSCURO, color_blend_mode=ft.BlendMode.SRC_IN),
                            ft.Text(Parque.nombre, size=32, font_family=tema.FUENTE_TITULOS, color=tema.VERDE_OSCURO),
                            ft.Text("Ingresá tus datos para comprar tus entradas"),
                            self.campo_nombre,
                            self.campo_apellido,
                            self.campo_mail,
                            self.texto_error,
                            ft.FilledButton(content="Comprar entrada", icon=ft.Icons.SHOPPING_CART, on_click=self.comprar_entrada),
                        ],
                    ),
                ),
            )
        )

    def comprar_entrada(self, e=None) -> None:
        usuario = Usuario(self.campo_nombre.value, self.campo_apellido.value, self.campo_mail.value)
        try:
            usuario.registrar()
        except ErrorValidacion as error:
            self.mostrar_errores(error)
            self.page.update()
            return
        if self.usuario is None or self.usuario.mail != usuario.mail:
            self.usuario = usuario
        self.mostrar_errores(None)
        PantallaFormularioEntrada(self.page, self.usuario, al_volver=self.mostrar).mostrar()

    def mostrar_errores(self, error: ErrorValidacion | None) -> None:
        """Muestra todos los errores juntos, cada uno debajo del campo que lo produjo; con None los borra."""
        errores = [] if error is None else error.errores if isinstance(error, ErroresValidacion) else [error]
        mensajes: dict[str | None, list[str]] = {}
        for encontrado in errores:
            mensajes.setdefault(encontrado.campo, []).append(str(encontrado))

        def mensaje(campo: str | None) -> str | None:
            return "\n".join(mensajes[campo]) if campo in mensajes else None

        self.campo_nombre.error = mensaje("nombre")
        self.campo_apellido.error = mensaje("apellido")
        self.campo_mail.error = mensaje("mail")
        self.texto_error.value = mensaje(None) or ""
