import asyncio
from typing import Callable

import flet as ft

from boundaries.pantalla_resultado_pago import PantallaResultadoPago
from controllers.controller_comprar_entrada import ControllerComprarEntrada
from entities.mercado_pago import PasarelaMercadoPago
from entities.usuario import Usuario
from entities.errores import ErrorMail, ErrorPago, ErrorValidacion, ErroresValidacion


class PantallaFormularioEntrada:
    """Formulario con los datos de la entrada; al confirmar le pide al controller que haga la compra."""

    # se crea una card por visitante, cuando se escribe la edad se desliza a la izquierda y aparece la siguiente
    ANCHO_CARD = 350
    ALTO_CARD = 160
    MAXIMO_CARDS = 10

    def __init__(self, page: ft.Page, usuario: Usuario, al_volver: Callable[[], None]):
        self.page = page
        self.usuario = usuario
        self.al_volver = al_volver
        self.campo_fecha = ft.TextField(label="Fecha de visita", hint_text="dd/mm/aaaa", prefix_icon=ft.Icons.CALENDAR_MONTH, width=350)
        self.campo_cantidad = ft.TextField(
            label="Cantidad de entradas", keyboard_type=ft.KeyboardType.NUMBER, prefix_icon=ft.Icons.CONFIRMATION_NUMBER, width=350,
            on_change=lambda e: self.cambiar_cantidad_edades(self.campo_cantidad.value),
        )
        self.armar_carrusel_edades()
        self.campo_tipo_pase = ft.Dropdown(
            label="Tipo de pase", width=350,
            options=[ft.DropdownOption(key="Regular", text="Regular"), ft.DropdownOption(key="VIP", text="VIP")],
        )
        self.campo_forma_pago = ft.Dropdown(
            label="Forma de pago", width=350,
            options=[ft.DropdownOption(key="Efectivo", text="Efectivo"), ft.DropdownOption(key="Tarjeta", text="Tarjeta (Mercado Pago)")],
        )
        self.texto_error = ft.Text(color=ft.Colors.RED, text_align=ft.TextAlign.CENTER)  # errores que no son de un campo del formulario
        self.procesando = ft.Row(
            visible=False, tight=True,
            controls=[ft.ProgressRing(width=20, height=20), ft.Text("Procesando la compra...")],
        )
        self.aviso_checkout = ft.Text(
            "Pagá en Mercado Pago; cuando termines, el resultado aparece acá.",
            visible=False, text_align=ft.TextAlign.CENTER,
        )
        self.boton_confirmar = ft.FilledButton(content="Confirmar compra", icon=ft.Icons.CHECK, on_click=self.confirmar_compra)
        self.modo_checkout: ft.LaunchMode | None = None  # cómo se abrió el checkout de Mercado Pago, para poder cerrarlo

    def armar_carrusel_edades(self) -> None:
        self.campos_edad: list[ft.TextField] = []
        self.edades_guardadas: list[str] = []
        self.cards_edad: list[ft.Container] = []
        self.card_actual = 0
        self.pila_edades = ft.Stack(width=self.ANCHO_CARD, height=self.ALTO_CARD, clip_behavior=ft.ClipBehavior.HARD_EDGE, visible=False)
        self.indicador_edades = ft.Text()
        self.boton_edad_anterior = ft.IconButton(icon=ft.Icons.CHEVRON_LEFT, on_click=self.ir_edad_anterior)
        self.boton_edad_siguiente = ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT, on_click=self.ir_edad_siguiente)
        self.aviso_edades = ft.Text("Ingresá la cantidad de entradas para cargar las edades", italic=True, color=ft.Colors.GREY)
        # errores de las edades en general
        self.error_edades = ft.Text(color=ft.Colors.RED, size=12, text_align=ft.TextAlign.CENTER, visible=False)
        self.navegacion_edades = ft.Row(
            tight=True, visible=False,
            controls=[self.boton_edad_anterior, self.indicador_edades, self.boton_edad_siguiente],
        )
        self.carrusel_edades = ft.Column(
            tight=True, spacing=4,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(tight=True, controls=[ft.Icon(ft.Icons.GROUP), ft.Text("Edades de los visitantes")]),
                self.aviso_edades,
                self.pila_edades,
                self.navegacion_edades,
                self.error_edades,
            ],
        )

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
                            self.carrusel_edades,
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

    def cambiar_cantidad_edades(self, texto: str | None) -> None:
        """arma una card por entrada. las edades ya cargadas se mantienen."""
        try:
            cantidad = int(texto or "")
        except ValueError:
            cantidad = 0
        if cantidad < 1 or cantidad > self.MAXIMO_CARDS:
            cantidad = 0

        self.edades_guardadas = [campo.value for campo in self.campos_edad] + self.edades_guardadas[len(self.campos_edad):]
        self.campos_edad = [
            ft.TextField(
                label="Edad", value=self.edades_guardadas[i] if i < len(self.edades_guardadas) else "",
                keyboard_type=ft.KeyboardType.NUMBER, prefix_icon=ft.Icons.PERSON,
                on_submit=self.ir_edad_siguiente,
            )
            for i in range(cantidad)
        ]
        self.cards_edad = [self.armar_card_edad(i, campo) for i, campo in enumerate(self.campos_edad)]
        self.pila_edades.controls = self.cards_edad
        self.card_actual = min(self.card_actual, max(cantidad - 1, 0))

        self.aviso_edades.visible = cantidad == 0
        self.pila_edades.visible = cantidad > 0
        self.navegacion_edades.visible = cantidad > 0
        self.ubicar_cards_edad()

    def armar_card_edad(self, indice: int, campo: ft.TextField) -> ft.Container:
        return ft.Container(
            width=self.ANCHO_CARD, height=self.ALTO_CARD, top=0,
            animate_position=ft.Animation(duration=300, curve=ft.AnimationCurve.EASE_OUT),
            content=ft.Card(
                content=ft.Container(
                    padding=16,
                    content=ft.Column(
                        tight=True, spacing=12,
                        controls=[
                            ft.Text(f"Visitante {indice + 1} de {len(self.campos_edad)}", weight=ft.FontWeight.BOLD),
                            campo,
                        ],
                    ),
                ),
            ),
        )

    def ubicar_cards_edad(self) -> None:
        for i, card in enumerate(self.cards_edad):
            card.left = (i - self.card_actual) * self.ANCHO_CARD
        self.indicador_edades.value = f"{self.card_actual + 1} / {len(self.cards_edad)}"
        self.boton_edad_anterior.disabled = self.card_actual == 0
        self.boton_edad_siguiente.disabled = self.card_actual >= len(self.cards_edad) - 1
        self.page.update()

    async def mover_a_card_edad(self, indice: int) -> None:
        if not 0 <= indice < len(self.cards_edad):
            return
        self.card_actual = indice
        self.ubicar_cards_edad()
        await self.campos_edad[indice].focus()

    async def ir_edad_siguiente(self, e=None) -> None:
        await self.mover_a_card_edad(self.card_actual + 1)

    async def ir_edad_anterior(self, e=None) -> None:
        await self.mover_a_card_edad(self.card_actual - 1)

    def leer_edades(self) -> list[str]:
        """Devuelve una edad por card, en orden (vacía si no se cargó), para que cada error vuelva a su card; la entrada las valida."""
        return [(campo.value or "").strip() for campo in self.campos_edad]

    def limpiar_errores(self) -> None:
        self.texto_error.value = ""
        self.campo_fecha.error = None
        self.campo_cantidad.error = None
        self.campo_tipo_pase.error_text = None
        self.campo_forma_pago.error_text = None
        self.error_edades.value = ""
        self.error_edades.visible = False
        for campo in self.campos_edad:
            campo.error = None

    def mostrar_errores(self, error: ErrorValidacion) -> None:
        """Muestra todos los errores juntos, cada uno debajo del campo que lo produjo."""
        errores = error.errores if isinstance(error, ErroresValidacion) else [error]
        mensajes: dict[str, list[str]] = {}
        cards_con_error = []
        for encontrado in errores:
            if encontrado.campo == "edades" and encontrado.indice is not None and encontrado.indice < len(self.campos_edad):
                self.campos_edad[encontrado.indice].error = str(encontrado)
                cards_con_error.append(encontrado.indice)
            else:
                mensajes.setdefault(encontrado.campo, []).append(str(encontrado))

        def mensaje(campo: str | None) -> str | None:
            return "\n".join(mensajes[campo]) if campo in mensajes else None

        self.campo_fecha.error = mensaje("fecha")
        self.campo_cantidad.error = mensaje("cantidad")
        self.campo_tipo_pase.error_text = mensaje("tipo_pase")
        self.campo_forma_pago.error_text = mensaje("forma_pago")
        self.error_edades.value = mensaje("edades") or ""
        self.error_edades.visible = "edades" in mensajes
        otros = [texto for campo, textos in mensajes.items() if campo not in ("fecha", "cantidad", "tipo_pase", "forma_pago", "edades") for texto in textos]
        self.texto_error.value = "\n".join(otros)
        if cards_con_error:
            # se muestra la primera card con error para que se vea qué visitante corregir
            self.card_actual = cards_con_error[0]
            self.ubicar_cards_edad()

    def cambiar_estado_procesando(self, procesando: bool, con_tarjeta: bool = False) -> None:
        self.procesando.visible = procesando
        self.aviso_checkout.visible = procesando and con_tarjeta
        self.boton_confirmar.disabled = procesando
        self.page.update()

    async def confirmar_compra(self, e=None) -> None:
        self.limpiar_errores()
        con_tarjeta = self.campo_forma_pago.value == "Tarjeta"
        self.cambiar_estado_procesando(True, con_tarjeta=con_tarjeta)

        try:
            pasarela = None
            if con_tarjeta:
                # en efectivo no se accede a Mercado Pago se tiene en cuenta donde se usa la app
                pasarela = PasarelaMercadoPago()
                pasarela.configurar_apertura(self.abrir_checkout)
            controller = ControllerComprarEntrada(self.usuario, pasarela=pasarela)
            # la compra con tarjeta espera a que Mercado Pago confirme el pago
            entrada = await asyncio.to_thread(
                controller.comprar_entrada,
                self.campo_fecha.value,
                self.campo_cantidad.value,
                self.leer_edades(),
                self.campo_tipo_pase.value,
                self.campo_forma_pago.value,
            )
        except ErrorValidacion as error:
            # datos inválidos se quedan en el formulario, con cada error debajo de su campo, para corregirlos
            self.mostrar_errores(error)
            self.cambiar_estado_procesando(False)
            return
        except ErrorPago as error:
            self.terminar_compra(motivo_rechazo=str(error))
            return
        except ErrorMail:
            # la compra se hizo, solo falló el mail de confirmación
            self.terminar_compra(entrada=controller.entrada, mail_enviado=False)
            return

        self.terminar_compra(entrada=entrada)

    def terminar_compra(self, **resultado) -> None:
        # primero se muestra el resultado y después se intenta cerrar el checkout, si cerrarlo no anda, el resultado igual queda en la app
        PantallaResultadoPago(self.page, self.al_volver, **resultado).mostrar()
        self.cerrar_checkout()

    # checkout de Mercado Pago: se abre en el dispositivo donde se está usando la app.
    # En el celular lo abre en el navegador interno de la app (in-app web view): la app no pasa a segundo
    # plano, así que no pierde la conexión y al terminar el pago muestra el resultado.
    # Ese navegador guarda su propia sesión de Mercado Pago (no la de Chrome).

    def es_celular(self) -> bool:
        return self.page.platform in (ft.PagePlatform.ANDROID, ft.PagePlatform.IOS)

    def elegir_modo_checkout(self) -> ft.LaunchMode:
        return ft.LaunchMode.IN_APP_WEB_VIEW if self.es_celular() else ft.LaunchMode.PLATFORM_DEFAULT

    def abrir_checkout(self, url: str) -> None:
        async def abrir_url():
            self.modo_checkout = self.elegir_modo_checkout()
            await ft.UrlLauncher().launch_url(url, mode=self.modo_checkout)

        # la pasarela llama a abrir_checkout() desde el hilo de la compra; run_task lo ejecuta en la página
        self.page.run_task(abrir_url)

    def cerrar_checkout(self) -> None:
        """Cierra el navegador interno del celular cuando el pago terminó (aprobado o no).
        No bloquea: si el celular no responde en 5 segundos, se deja de intentar."""
        if self.modo_checkout != ft.LaunchMode.IN_APP_WEB_VIEW:
            return
        modo, self.modo_checkout = self.modo_checkout, None

        async def cerrar_pestana():
            launcher = ft.UrlLauncher()
            try:
                if await asyncio.wait_for(launcher.supports_close_for_launch_mode(modo), timeout=5):
                    await asyncio.wait_for(launcher.close_in_app_web_view(), timeout=5)
            except Exception:
                pass

        self.page.run_task(cerrar_pestana)
