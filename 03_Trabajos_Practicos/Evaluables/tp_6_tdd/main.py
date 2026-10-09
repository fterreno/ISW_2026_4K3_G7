import sys
from pathlib import Path

# las capas (boundaries, controllers, entities) están en la raíz del proyecto;
# se agrega al path para poder ejecutar main.py desde cualquier carpeta
RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))

import flet as ft

from boundaries.pantalla_inicio import PantallaInicio


def main(page: ft.Page):
    page.title = "EcoHarmony Park"
    page.scroll = ft.ScrollMode.AUTO
    PantallaInicio(page).mostrar()


if __name__ == "__main__":
    ft.run(main)
