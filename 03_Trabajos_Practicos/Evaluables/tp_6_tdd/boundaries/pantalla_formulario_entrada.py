import asyncio
from typing import Callable

import flet as ft

from boundaries.navegador_checkout import NavegadorCheckout
from boundaries.pantalla_resultado_pago import PantallaResultadoPago
from controllers.controller_comprar_entrada import ControllerComprarEntrada
from entities.mercado_pago import PasarelaMercadoPago
from entities.usuario import Usuario
from entities.errores import ErrorMail, ErrorPago, ErrorValidacion


class PantallaFormularioEntrada:
    """Formulario con los datos de la entrada; al confirmar le pide al controller que haga la compra."""

    def __init__(self, page: ft.Page, usuario: Usuario, al_volver: Callable[[], None]):
        self.page = page
        self.usuario = usuario
        self.al_volver = al_volver
        self.campo_fecha = ft.TextField(label="Fecha de visita", hint_text="dd/mm/aaaa", prefix_icon=ft.Icons.CALENDAR_MONTH, width=350)
        self.campo_cantidad = ft.TextField(label="Cantidad de entradas", keyboard_type=ft.KeyboardType.NUMBER, prefix_icon=ft.Icons.CONFIRMATION_NUMBER, width=350)
        self.campo_edades = ft.TextField(label="Edades de los visitantes", hint_text="separadas por coma, por ejemplo: 30, 15", prefix_icon=ft.Icons.GROUP, width=350)
        self.campo_tipo_pase = ft.Dropdown(
            label="Tipo de pase", width=350,
            options=[ft.DropdownOption(key="Regular", text="Regular"), ft.DropdownOption(key="VIP", text="VIP")],
        )
        self.campo_forma_pago = ft.Dropdown(
            label="Forma de pago", width=350,
            options=[ft.DropdownOption(key="Efectivo", text="Efectivo"), ft.DropdownOption(key="Tarjeta", text="Tarjeta (Mercado Pago)")],
        )
        self.texto_error = ft.Text(color=ft.Colors.RED, text_align=ft.TextAlign.CENTER)
        self.procesando = ft.Row(
            visible=False, tight=True,
            controls=[ft.ProgressRing(width=20, height=20), ft.Text("Procesando la compra...")],
        )
        self.aviso_checkout = ft.Text(
            "Pagá en Mercado Pago; cuando termines, el resultado aparece acá.",
            visible=False, text_align=ft.TextAlign.CENTER,
        )
        self.boton_confirmar = ft.FilledButton(content="Confirmar compra", icon=ft.Icons.CHECK, on_click=self.confirmar_compra)

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
                            ft.Text("Comprar entradas", size=28, weight=ft.FontWeight.BOLD),
                            ft.Text(f"{self.usuario.nombre} {self.usuario.apellido} · {self.usuario.mail}"),
                            self.campo_fecha,
                            self.campo_cantidad,
                            self.campo_edades,
                            self.campo_tipo_pase,
                            self.campo_forma_pago,
                            self.texto_error,
                            self.procesando,
                            self.aviso_checkout,
                            ft.Row(
                                tight=True, spacing=12,
                                controls=[
                                    ft.OutlinedButton(content="Volver", icon=ft.Icons.ARROW_BACK, on_click=lambda e: self.al_volver()),
                                    self.boton_confirmar,
                                ],
                            ),
                        ],
                    ),
                ),
            )
        )

    def leer_edades(self) -> list[str]:
        """Separa el texto de edades por comas; la entrada se encarga de validarlas."""
        return [edad.strip() for edad in (self.campo_edades.value or "").split(",") if edad.strip()]

    def cambiar_estado_procesando(self, procesando: bool, con_tarjeta: bool = False) -> None:
        self.procesando.visible = procesando
        self.aviso_checkout.visible = procesando and con_tarjeta
        self.boton_confirmar.disabled = procesando
        self.page.update()

    async def confirmar_compra(self, e=None) -> None:
        self.texto_error.value = ""
        self.cambiar_estado_procesando(True, con_tarjeta=self.campo_forma_pago.value == "Tarjeta")

        navegador = NavegadorCheckout(self.page)
        try:
            # el checkout de Mercado Pago se abre en el navegador del dispositivo donde se usa la app (en el celular, en el navegador interno de la app)
            pasarela = PasarelaMercadoPago()
            pasarela.configurar_apertura(navegador.abrir)
            controller = ControllerComprarEntrada(self.usuario, pasarela=pasarela)
            # la compra con tarjeta espera a que Mercado Pago confirme el pago (puede tardar minutos);
            # se hace en otro hilo para no bloquear la página, y las pantallas se actualizan acá, en la página
            entrada = await asyncio.to_thread(
                controller.comprar_entrada,
                self.campo_fecha.value,
                self.campo_cantidad.value,
                self.leer_edades(),
                self.campo_tipo_pase.value,
                self.campo_forma_pago.value,
            )
        except ErrorValidacion as error:
            # datos inválidos: se queda en el formulario para corregirlos
            self.texto_error.value = str(error)
            self.cambiar_estado_procesando(False)
            return
        except ErrorPago as error:
            self.terminar_compra(navegador, motivo_rechazo=str(error))
            return
        except ErrorMail:
            # la compra se hizo, solo falló el mail de confirmación
            self.terminar_compra(navegador, entrada=controller.entrada, mail_enviado=False)
            return

        self.terminar_compra(navegador, entrada=entrada)

    def terminar_compra(self, navegador: NavegadorCheckout, **resultado) -> None:
        # primero se muestra el resultado y después se intenta cerrar el checkout:
        # si cerrarlo no anda, el resultado igual queda en la app
        PantallaResultadoPago(self.page, self.al_volver, **resultado).mostrar()
        navegador.cerrar()
