import flet as ft

from boundaries.pantalla_formulario_entrada import PantallaFormularioEntrada
from entities.parque import Parque
from entities.usuario import Usuario
from entities.errores import ErrorValidacion


class PantallaInicio:
    """Landing page: pide los datos del usuario y lo lleva al formulario para comprar la entrada."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.usuario: Usuario | None = None  # se conserva para no volver a pedir los datos al volver al inicio
        self.campo_nombre = ft.TextField(label="Nombre", prefix_icon=ft.Icons.PERSON, width=350)
        self.campo_apellido = ft.TextField(label="Apellido", prefix_icon=ft.Icons.PERSON_OUTLINE, width=350)
        self.campo_mail = ft.TextField(label="Mail", prefix_icon=ft.Icons.EMAIL, keyboard_type=ft.KeyboardType.EMAIL, width=350)
        self.texto_error = ft.Text(color=ft.Colors.RED, text_align=ft.TextAlign.CENTER)

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
                            ft.Icon(ft.Icons.PARK, size=64, color=ft.Colors.GREEN),
                            ft.Text(Parque.nombre, size=32, weight=ft.FontWeight.BOLD),
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
            self.texto_error.value = str(error)
            self.page.update()
            return

        # si es el mismo usuario que ya compró, se conservan sus entradas
        if self.usuario is None or self.usuario.mail != usuario.mail:
            self.usuario = usuario
        self.texto_error.value = ""
        PantallaFormularioEntrada(self.page, self.usuario, al_volver=self.mostrar).mostrar()
