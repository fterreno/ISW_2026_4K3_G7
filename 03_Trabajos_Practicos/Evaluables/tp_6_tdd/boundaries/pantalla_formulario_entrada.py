import asyncio
import calendar
from datetime import date, datetime
from typing import Callable

import flet as ft

from assets.style import tema
from boundaries.pantalla_resultado_pago import PantallaResultadoPago
from controllers.controller_comprar_entrada import ControllerComprarEntrada
from entities.mercado_pago import PasarelaMercadoPago
from entities.parque import Parque
from entities.usuario import Usuario
from entities.errores import ErrorMail, ErrorPago, ErrorValidacion, ErroresValidacion


class PantallaFormularioEntrada:
    """Formulario con los datos de la entrada; al confirmar le pide al controller que haga la compra."""

    # se crea una card por visitante, cuando se escribe la edad se desliza a la izquierda y aparece la siguiente;
    # deslizando con el dedo a la derecha se vuelve a la anterior (y a la izquierda se avanza)
    ANCHO_CARD = 350
    ALTO_CARD = 160
    MAXIMO_CARDS = 10
    ESPERA_AVANCE = 1.2  # segundos sin escribir para pasar solo a la card siguiente
    DISTANCIA_DESLIZAR = 60  # píxeles que hay que arrastrar el dedo para cambiar de card
    VELOCIDAD_DESLIZAR = 300  # o un deslizamiento rápido, en píxeles por segundo

    TAMANO_DIA = 40  # tamaño de cada día del calendario
    MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    DIAS_SEMANA = ["L", "M", "M", "J", "V", "S", "D"]

    def __init__(self, page: ft.Page, usuario: Usuario, al_volver: Callable[[], None]):
        self.page = page
        self.usuario = usuario
        self.al_volver = al_volver
        self.parque = Parque()
        self.fecha_elegida: date | None = None
        # la fecha no se escribe: al tocar el campo se abre el calendario con los días no disponibles deshabilitados
        self.campo_fecha = ft.TextField(
            label="Fecha de visita", hint_text="Elegí la fecha", prefix_icon=ft.Icons.CALENDAR_MONTH, width=350,
            read_only=True, mouse_cursor=ft.MouseCursor.CLICK, on_click=self.abrir_calendario,
        )
        self.armar_calendario()
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
        self.texto_error = ft.Text(color=tema.ROJO, text_align=ft.TextAlign.CENTER)  # errores que no son de un campo del formulario
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

    # calendario de la fecha de visita: solo se pueden tocar los días en que el parque está disponible.

    def armar_calendario(self) -> None:
        self.ahora_calendario = datetime.now()
        self.mes_calendario = date.today().replace(day=1)
        self.titulo_mes = ft.Text(size=16, font_family=tema.FUENTE_TITULOS)
        self.boton_mes_anterior = ft.IconButton(icon=ft.Icons.CHEVRON_LEFT, on_click=lambda e: self.cambiar_mes(-1))
        self.boton_mes_siguiente = ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT, on_click=lambda e: self.cambiar_mes(1))
        self.semanas_calendario = ft.Column(tight=True, spacing=4)
        self.dialogo_calendario = ft.AlertDialog(
            title=ft.Text("Fecha de visita", font_family=tema.FUENTE_TITULOS),
            content=ft.Column(
                tight=True, spacing=4, width=7 * self.TAMANO_DIA + 6 * 4,
                controls=[
                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                           controls=[self.boton_mes_anterior, self.titulo_mes, self.boton_mes_siguiente]),
                    ft.Row(spacing=4, controls=[self.celda_dia(ft.Text(dia, font_family=tema.FUENTE_TITULOS)) for dia in self.DIAS_SEMANA]),
                    self.semanas_calendario,
                    ft.Text("Los días deshabilitados son días en que el parque está cerrado o que no se pueden reservar.",
                            size=12, italic=True),
                ],
            ),
            actions=[ft.TextButton(content="Cancelar", on_click=lambda e: self.page.pop_dialog())],
        )

    def abrir_calendario(self, e=None) -> None:
        # la disponibilidad se calcula al abrirlo, por si ya pasó el horario de compra de hoy
        self.ahora_calendario = datetime.now()
        self.mes_calendario = (self.fecha_elegida or self.ahora_calendario.date()).replace(day=1)
        self.dibujar_mes()
        self.page.show_dialog(self.dialogo_calendario)

    def dia_disponible(self, dia: date) -> bool:
        try:
            self.parque.validar_disponibilidad(dia, self.ahora_calendario)
        except ErrorValidacion:
            return False
        return True

    def cambiar_mes(self, paso: int) -> None:
        mes = self.mes_calendario.month - 1 + paso
        self.mes_calendario = date(self.mes_calendario.year + mes // 12, mes % 12 + 1, 1)
        self.dibujar_mes()
        self.page.update()

    def dibujar_mes(self) -> None:
        hoy = self.ahora_calendario.date()
        # solo se puede ir del mes actual al de dentro de un mes, que son los que tienen días para reservar
        self.titulo_mes.value = f"{self.MESES[self.mes_calendario.month - 1]} {self.mes_calendario.year}"
        self.boton_mes_anterior.disabled = self.mes_calendario <= hoy.replace(day=1)
        self.boton_mes_siguiente.disabled = self.mes_calendario >= self.parque.sumar_un_mes(hoy).replace(day=1)
        semanas = calendar.Calendar(firstweekday=calendar.MONDAY).monthdatescalendar(self.mes_calendario.year, self.mes_calendario.month)
        self.semanas_calendario.controls = [
            ft.Row(spacing=4, controls=[self.dibujar_dia(dia) for dia in semana])
            for semana in semanas
        ]

    def dibujar_dia(self, dia: date) -> ft.Container:
        if dia.month != self.mes_calendario.month:
            return self.celda_dia(None)  # días del mes anterior o siguiente: lugar vacío
        disponible = self.dia_disponible(dia)
        seleccionado = dia == self.fecha_elegida
        es_hoy = dia == self.ahora_calendario.date()
        return self.celda_dia(
            ft.Text(str(dia.day), color=tema.CREMA if seleccionado else tema.TEXTO,
                    font_family=tema.FUENTE_TITULOS if es_hoy or seleccionado else tema.FUENTE),
            bgcolor=tema.VERDE_OSCURO if seleccionado else None,
            border=ft.Border.all(1, tema.VERDE_OSCURO) if es_hoy and not seleccionado else None,
            opacity=1 if disponible else 0.3,
            on_click=(lambda e, elegido=dia: self.elegir_fecha(elegido)) if disponible else None,
            disabled=not disponible,
        )

    def celda_dia(self, contenido: ft.Control | None, **estilo) -> ft.Container:
        return ft.Container(width=self.TAMANO_DIA, height=self.TAMANO_DIA, alignment=ft.Alignment.CENTER,
                            border_radius=self.TAMANO_DIA / 2, content=contenido, **estilo)

    def elegir_fecha(self, fecha: date) -> None:
        self.fecha_elegida = fecha
        self.page.pop_dialog()
        # el controller recibe la fecha como texto dd/mm/aaaa, igual que antes
        self.campo_fecha.value = f"{fecha:%d/%m/%Y}"
        self.campo_fecha.error = None
        self.page.update()

    def armar_carrusel_edades(self) -> None:
        self.campos_edad: list[ft.TextField] = []
        self.edades_guardadas: list[str] = []
        self.cards_edad: list[ft.Container] = []
        self.card_actual = 0
        self.arrastre = 0.0  # cuánto se movió el dedo en el deslizamiento actual
        self.pila_edades = ft.Stack(width=self.ANCHO_CARD, height=self.ALTO_CARD, clip_behavior=ft.ClipBehavior.HARD_EDGE)
        # el detector de gestos envuelve las cards para poder cambiarlas deslizando el dedo
        self.deslizador_edades = ft.GestureDetector(
            content=self.pila_edades, visible=False,
            on_horizontal_drag_start=self.empezar_deslizamiento,
            on_horizontal_drag_update=self.seguir_deslizamiento,
            on_horizontal_drag_end=self.terminar_deslizamiento,
        )
        self.aviso_edades = ft.Text("Ingresá la cantidad de entradas para cargar las edades", italic=True, color=tema.VERDE)
        self.ayuda_deslizar = ft.Text("Deslizá a la derecha para volver al visitante anterior", italic=True, size=12, visible=False)
        # errores de las edades en general
        self.error_edades = ft.Text(color=tema.ROJO, size=12, text_align=ft.TextAlign.CENTER, visible=False)
        self.carrusel_edades = ft.Column(
            tight=True, spacing=4,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(tight=True, controls=[ft.Icon(ft.Icons.GROUP), ft.Text("Edades de los visitantes")]),
                self.aviso_edades,
                self.deslizador_edades,
                self.ayuda_deslizar,
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
                            ft.Image(src=tema.LOGO, width=64, fit=ft.BoxFit.CONTAIN, color=tema.VERDE_OSCURO, color_blend_mode=ft.BlendMode.SRC_IN),
                            ft.Text("Comprar entradas", size=28, font_family=tema.FUENTE_TITULOS),
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
                on_change=self.avanzar_al_terminar_de_escribir,
                on_submit=self.ir_edad_siguiente,
            )
            for i in range(cantidad)
        ]
        self.cards_edad = [self.armar_card_edad(i, campo) for i, campo in enumerate(self.campos_edad)]
        self.pila_edades.controls = self.cards_edad
        self.card_actual = min(self.card_actual, max(cantidad - 1, 0))

        self.aviso_edades.visible = cantidad == 0
        self.deslizador_edades.visible = cantidad > 0
        self.ayuda_deslizar.visible = cantidad > 1
        self.ubicar_cards_edad()

    def armar_card_edad(self, indice: int, campo: ft.TextField) -> ft.Container:
        # sin card ni color de fondo: el visitante se ve sobre el mismo fondo crema de la pantalla
        return ft.Container(
            width=self.ANCHO_CARD, height=self.ALTO_CARD, top=0, padding=16,
            animate_position=ft.Animation(duration=300, curve=ft.AnimationCurve.EASE_OUT),
            content=ft.Column(
                tight=True, spacing=12,
                controls=[
                    ft.Text(f"Visitante {indice + 1} de {len(self.campos_edad)}", font_family=tema.FUENTE_TITULOS),
                    campo,
                ],
            ),
        )

    def ubicar_cards_edad(self) -> None:
        for i, card in enumerate(self.cards_edad):
            card.left = (i - self.card_actual) * self.ANCHO_CARD
        self.page.update()

    async def avanzar_al_terminar_de_escribir(self, e) -> None:
        """Cuando la persona deja de escribir una edad válida, la card se desliza sola a la siguiente."""
        campo = e.control
        valor = campo.value
        await asyncio.sleep(self.ESPERA_AVANCE)
        sigue_igual = campo.value == valor and campo in self.campos_edad
        if sigue_igual and (valor or "").strip().isdigit() and self.campos_edad.index(campo) == self.card_actual:
            await self.ir_edad_siguiente()

    def empezar_deslizamiento(self, e=None) -> None:
        self.arrastre = 0.0

    def seguir_deslizamiento(self, e: ft.DragUpdateEvent) -> None:
        self.arrastre += e.primary_delta or 0

    async def terminar_deslizamiento(self, e: ft.DragEndEvent) -> None:
        """Deslizar a la derecha vuelve al visitante anterior; a la izquierda pasa al siguiente."""
        velocidad = e.primary_velocity or 0
        if self.arrastre > self.DISTANCIA_DESLIZAR or velocidad > self.VELOCIDAD_DESLIZAR:
            await self.ir_edad_anterior()
        elif self.arrastre < -self.DISTANCIA_DESLIZAR or velocidad < -self.VELOCIDAD_DESLIZAR:
            await self.ir_edad_siguiente()
        self.arrastre = 0.0

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
            controller = ControllerComprarEntrada(self.usuario, self.parque, pasarela=pasarela)
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
