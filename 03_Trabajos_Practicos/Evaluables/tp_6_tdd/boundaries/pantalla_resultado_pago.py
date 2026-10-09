from typing import Callable

import flet as ft

from entities.entrada import Entrada
from entities.forma_pago import FormaPago


class PantallaResultadoPago:
    """Muestra si la compra se confirmó (con el detalle de la entrada) o si el pago no se realizó."""

    def __init__(self, page: ft.Page, al_volver: Callable[[], None], entrada: Entrada | None = None,
                 motivo_rechazo: str | None = None, mail_enviado: bool = True):
        self.page = page
        self.al_volver = al_volver
        self.entrada = entrada
        self.motivo_rechazo = motivo_rechazo
        self.mail_enviado = mail_enviado

    def mostrar(self) -> None:
        contenido = self.contenido_rechazado() if self.entrada is None else self.contenido_confirmado()
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
                        controls=contenido + [
                            ft.FilledButton(content="Volver al inicio", icon=ft.Icons.HOME, on_click=lambda e: self.al_volver()),
                        ],
                    ),
                ),
            )
        )

    def contenido_confirmado(self) -> list[ft.Control]:
        if self.entrada.forma_pago == FormaPago.TARJETA:
            titulo = "¡Pago confirmado!"
            aviso = "El pago con tarjeta fue aprobado por Mercado Pago."
        else:
            titulo = "¡Reserva confirmada!"
            aviso = "Recordá abonar el total en efectivo al ingresar al parque."

        detalle = [
            f"Fecha de visita: {self.entrada.fecha_entrada:%d/%m/%Y}",
            f"Cantidad de entradas: {self.entrada.cantidad}",
            f"Tipo de pase: {self.entrada.tipo_pase.value}",
            f"Forma de pago: {self.entrada.forma_pago.value}",
            f"Total: $ {self.entrada.monto_total:.2f}",
        ]
        mensaje_mail = ("Te enviamos el detalle de la compra por mail." if self.mail_enviado
                        else "No pudimos enviarte el mail de confirmación; guardá estos datos.")

        return [
            ft.Icon(ft.Icons.CHECK_CIRCLE, size=72, color=ft.Colors.GREEN),
            ft.Text(titulo, size=28, weight=ft.FontWeight.BOLD),
            ft.Text(aviso, text_align=ft.TextAlign.CENTER),
            ft.Card(content=ft.Container(padding=20, content=ft.Column(tight=True, controls=[ft.Text(linea) for linea in detalle]))),
            ft.Text(mensaje_mail, color=None if self.mail_enviado else ft.Colors.ORANGE, text_align=ft.TextAlign.CENTER),
        ]

    def contenido_rechazado(self) -> list[ft.Control]:
        return [
            ft.Icon(ft.Icons.CANCEL, size=72, color=ft.Colors.RED),
            ft.Text("No se ha realizado el pago", size=28, weight=ft.FontWeight.BOLD),
            ft.Text(f"Motivo: {self.motivo_rechazo}", text_align=ft.TextAlign.CENTER),
            ft.Text("La entrada no fue comprada. Podés intentarlo de nuevo.", text_align=ft.TextAlign.CENTER),
        ]
