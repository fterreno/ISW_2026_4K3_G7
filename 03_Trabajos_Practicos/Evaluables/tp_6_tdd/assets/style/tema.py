import flet as ft

# Paleta de colores: https://coolors.co/palette/386641-6a994e-a7c957-f2e8cf-bc4749
VERDE_OSCURO = "#386641"
VERDE = "#6A994E"
VERDE_CLARO = "#A7C957"
CREMA = "#F2E8CF"
ROJO = "#BC4749"
TEXTO = "#1F3324"
CREMA_CLARO = "#FAF6EA" 
FUENTE = "Lato"
FUENTE_TITULOS = "Lato Bold"
LOGO = "images/image.png"


def aplicar_tema(page: ft.Page) -> None:
    page.fonts = {
        FUENTE: "fonts/Lato-Regular.ttf",
        FUENTE_TITULOS: "fonts/Lato-Bold.ttf",
    }
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = CREMA
    page.theme = ft.Theme(
        font_family=FUENTE,
        scaffold_bgcolor=CREMA,
        card_bgcolor=CREMA_CLARO,
        color_scheme=ft.ColorScheme(
            primary=VERDE_OSCURO,
            on_primary=CREMA,
            primary_container=VERDE_CLARO,
            on_primary_container=VERDE_OSCURO,
            secondary=VERDE,
            on_secondary=CREMA,
            secondary_container=VERDE_CLARO,
            on_secondary_container=VERDE_OSCURO,
            tertiary=VERDE_CLARO,
            on_tertiary=VERDE_OSCURO,
            error=ROJO,
            on_error=CREMA,
            surface=CREMA,
            on_surface=TEXTO,
            on_surface_variant=VERDE_OSCURO,
            outline=VERDE,
            outline_variant=VERDE_CLARO,
            surface_container_lowest=CREMA_CLARO,
            surface_container_low=CREMA_CLARO,
            surface_container=CREMA_CLARO,
            surface_container_high=CREMA_CLARO,
            surface_container_highest=CREMA_CLARO,
        ),
    )
