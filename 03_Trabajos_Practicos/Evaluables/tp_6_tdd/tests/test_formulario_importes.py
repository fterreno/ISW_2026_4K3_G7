from types import SimpleNamespace

import pytest

from boundaries.pantalla_formulario_entrada import PantallaFormularioEntrada
from entities.usuario import Usuario


@pytest.fixture
def pantalla():
    pagina = SimpleNamespace(update=lambda: None)
    usuario = Usuario("Ana", "Pérez", "ana@example.com")
    return PantallaFormularioEntrada(pagina, usuario, al_volver=lambda: None)


def cargar_datos(pantalla, pase, edades):
    pantalla.campo_cantidad.value = str(len(edades))
    pantalla.cambiar_cantidad_edades(pantalla.campo_cantidad.value)
    for campo, edad in zip(pantalla.campos_edad, edades):
        campo.value = edad
    pantalla.campo_tipo_pase.value = pase
    pantalla.campo_tipo_pase.on_select(None)


def test_importes_piden_datos_al_iniciar(pantalla):
    assert pantalla.texto_subtotal.value == "Subtotal: -"
    assert pantalla.texto_total.value == "Total: -"
    assert pantalla.aviso_importes.visible


@pytest.mark.parametrize("pase, subtotal, total", [
    ("Regular", "Subtotal: $ 40.000,00", "Total: $ 20.000,00"),
    ("VIP", "Subtotal: $ 80.000,00", "Total: $ 40.000,00"),
])
def test_importes_se_muestran_antes_de_comprar(pantalla, pase, subtotal, total):
    cargar_datos(pantalla, pase, ["3", "15", "30", "60"])
    assert pantalla.texto_subtotal.value == subtotal
    assert pantalla.texto_total.value == total
    assert not pantalla.aviso_importes.visible
    assert pantalla.usuario.entradas == []


def test_cambiar_pase_actualiza_importes(pantalla):
    cargar_datos(pantalla, "Regular", ["30", "15"])
    pantalla.campo_tipo_pase.value = "VIP"
    pantalla.campo_tipo_pase.on_select(None)
    assert pantalla.texto_subtotal.value == "Subtotal: $ 40.000,00"
    assert pantalla.texto_total.value == "Total: $ 30.000,00"


def test_cambiar_cantidad_actualiza_importes(pantalla):
    cargar_datos(pantalla, "Regular", ["30", "15"])
    pantalla.campo_cantidad.value = "1"
    pantalla.campo_cantidad.on_change(None)
    assert pantalla.texto_subtotal.value == "Subtotal: $ 10.000,00"
    assert pantalla.texto_total.value == "Total: $ 10.000,00"


@pytest.mark.parametrize("edad", ["", "abc", "-1"])
def test_edad_invalida_quita_importes_anteriores(pantalla, edad):
    cargar_datos(pantalla, "Regular", ["30"])
    pantalla.campos_edad[0].value = edad
    pantalla.actualizar_importes()
    assert pantalla.texto_subtotal.value == "Subtotal: -"
    assert pantalla.texto_total.value == "Total: -"
    assert pantalla.aviso_importes.visible


async def test_cambiar_edad_actualiza_total_incluso_si_es_gratis(pantalla):
    cargar_datos(pantalla, "Regular", ["30"])
    pantalla.ESPERA_AVANCE = 0
    campo = pantalla.campos_edad[0]
    campo.value = "3"
    await campo.on_change(SimpleNamespace(control=campo))
    assert pantalla.texto_subtotal.value == "Subtotal: $ 10.000,00"
    assert pantalla.texto_descuentos.value == "Descuentos por edad: $ 10.000,00"
    assert pantalla.texto_total.value == "Total: $ 0,00"
