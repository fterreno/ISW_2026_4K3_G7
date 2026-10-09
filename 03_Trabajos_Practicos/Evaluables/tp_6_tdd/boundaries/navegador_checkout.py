import asyncio

import flet as ft


class NavegadorCheckout:
    """Abre el checkout de Mercado Pago en el dispositivo donde se está usando la app.
    En el celular lo abre en el navegador interno de la app (in-app web view): la app no pasa a segundo
    plano, así que no pierde la conexión y al terminar el pago muestra el resultado.
    Ese navegador guarda su propia sesión de Mercado Pago (no la de Chrome)."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.modo: ft.LaunchMode | None = None

    def es_celular(self) -> bool:
        return self.page.platform in (ft.PagePlatform.ANDROID, ft.PagePlatform.IOS)

    def elegir_modo(self) -> ft.LaunchMode:
        return ft.LaunchMode.IN_APP_WEB_VIEW if self.es_celular() else ft.LaunchMode.PLATFORM_DEFAULT

    def abrir(self, url: str) -> None:
        async def abrir_url():
            self.modo = self.elegir_modo()
            await ft.UrlLauncher().launch_url(url, mode=self.modo)

        # la pasarela llama a abrir() desde el hilo de la compra; run_task lo ejecuta en la página
        self.page.run_task(abrir_url)

    def cerrar(self) -> None:
        """Cierra el navegador interno del celular cuando el pago terminó (aprobado o no).
        No bloquea: si el celular no responde en 5 segundos, se deja de intentar."""
        if self.modo != ft.LaunchMode.IN_APP_WEB_VIEW:
            return
        modo, self.modo = self.modo, None

        async def cerrar_pestana():
            launcher = ft.UrlLauncher()
            try:
                if await asyncio.wait_for(launcher.supports_close_for_launch_mode(modo), timeout=5):
                    await asyncio.wait_for(launcher.close_in_app_web_view(), timeout=5)
            except Exception:
                pass

        self.page.run_task(cerrar_pestana)
