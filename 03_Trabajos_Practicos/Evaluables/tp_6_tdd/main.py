import sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))

import flet as ft

from assets.style.tema import aplicar_tema
from boundaries.pantalla_inicio import PantallaInicio
from entities.parque import Parque


def main(page: ft.Page):
    page.title = Parque.nombre
    page.scroll = ft.ScrollMode.AUTO
    aplicar_tema(page)
    PantallaInicio(page).mostrar()


if __name__ == "__main__":
    ft.run(main, assets_dir=str(RAIZ / "assets"))
