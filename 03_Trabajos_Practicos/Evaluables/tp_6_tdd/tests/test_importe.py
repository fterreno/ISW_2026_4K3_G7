from datetime import date
from types import SimpleNamespace

import flet as ft
import pytest

from boundaries.pantalla_formulario_entrada import PantallaFormularioEntrada
from entities.entrada import Entrada
from entities.forma_pago import FormaPago
from entities.tipo_pase import TipoPase
from entities.usuario import Usuario


def monto_de_una_entrada(tipo_pase, edad):
    entrada = Entrada(date(2026, 10, 9), 1, [edad], tipo_pase, FormaPago.EFECTIVO)
    entrada.generar_monto_total()
    return entrada.monto_total


@pytest.fixture
def pantalla():
    pagina = SimpleNamespace(update=lambda: None)
    usuario = Usuario("Ana", "Pérez", "ana@example.com")
    return PantallaFormularioEntrada(pagina, usuario, al_volver=lambda: None)


def cargar_formulario(pantalla, pase, edades):
    """Carga los campos que usan los importes sin pasar por el carrusel de edades."""
    pantalla.campo_cantidad.value = str(len(edades))
    pantalla.campos_edad = [ft.TextField(value=edad) for edad in edades]
    pantalla.campo_tipo_pase.value = pase


def importes_visibles(pantalla):
    return pantalla.texto_subtotal.visible and pantalla.texto_total.visible and not pantalla.aviso_importes.visible


# 8.1 Probar una entrada VIP con una edad de 3 años o menor y el monto de la entrada es cero. PASA
def test_vip_hasta_3_anios_es_gratis():
    assert monto_de_una_entrada(TipoPase.VIP, 3) == 0


# 8.2 Probar una entrada Regular con una edad de 3 años o menor y el monto de la entrada es cero. PASA
def test_regular_hasta_3_anios_es_gratis():
    assert monto_de_una_entrada(TipoPase.REGULAR, 3) == 0


# 8.3 Probar una entrada VIP con edad menor o igual a 15 años y el monto de la entrada es 10000. PASA
def test_vip_hasta_15_anios_paga_10000():
    assert monto_de_una_entrada(TipoPase.VIP, 15) == 10000


# 8.4 Probar una entrada Regular con edad menor o igual a 15 años y el monto de la entrada es 5000. PASA
def test_regular_hasta_15_anios_paga_5000():
    assert monto_de_una_entrada(TipoPase.REGULAR, 15) == 5000


# 8.5 Probar una entrada VIP con edad mayor o igual a 60 años y el monto de la entrada es 10000. PASA
def test_vip_desde_60_anios_paga_10000():
    assert monto_de_una_entrada(TipoPase.VIP, 60) == 10000


# 8.6 Probar una entrada Regular con edad mayor o igual a 60 años y el monto de la entrada es 5000. PASA
def test_regular_desde_60_anios_paga_5000():
    assert monto_de_una_entrada(TipoPase.REGULAR, 60) == 5000


# 8.7 Probar la visualización del subtotal y el total antes de confirmar la compra. PASA
@pytest.mark.parametrize("pase, subtotal, total", [
    ("Regular", "Subtotal: $ 40.000,00", "Total: $ 20.000,00"),
    ("VIP", "Subtotal: $ 80.000,00", "Total: $ 40.000,00"),
])
def test_importes_se_muestran_antes_de_comprar(pantalla, pase, subtotal, total):
    cargar_formulario(pantalla, pase, ["3", "15", "30", "60"])
    pantalla.actualizar_importes()
    assert pantalla.texto_subtotal.value == subtotal
    assert pantalla.texto_total.value == total
    assert importes_visibles(pantalla)
    # se muestran sin confirmar la compra: el usuario todavía no tiene entradas
    assert pantalla.usuario.entradas == []


# 8.8 Probar que al cambiar el tipo de pase se actualicen los importes. PASA
def test_cambiar_pase_actualiza_importes(pantalla):
    cargar_formulario(pantalla, "Regular", ["30", "15"])
    pantalla.actualizar_importes()
    pantalla.campo_tipo_pase.value = "VIP"
    pantalla.campo_tipo_pase.on_select(None)
    assert pantalla.texto_subtotal.value == "Subtotal: $ 40.000,00"
    assert pantalla.texto_total.value == "Total: $ 30.000,00"


# 8.9 Probar que al cambiar la cantidad de entradas se actualicen los importes. PASA
def test_cambiar_cantidad_actualiza_importes(pantalla):
    cargar_formulario(pantalla, "Regular", ["30", "15"])
    pantalla.actualizar_importes()
    pantalla.campo_cantidad.value = "1"
    pantalla.campo_cantidad.on_change(None)
    assert pantalla.texto_subtotal.value == "Subtotal: $ 10.000,00"
    assert pantalla.texto_total.value == "Total: $ 10.000,00"


# 8.10 Probar que al cargar una edad inválida se quiten los importes anteriores. PASA
@pytest.mark.parametrize("edad", ["", "abc", "-1"])
def test_edad_invalida_quita_importes_anteriores(pantalla, edad):
    cargar_formulario(pantalla, "Regular", ["30"])
    pantalla.actualizar_importes()
    pantalla.campos_edad[0].value = edad
    pantalla.actualizar_importes()
    assert not pantalla.texto_subtotal.visible
    assert not pantalla.texto_total.visible
    assert pantalla.aviso_importes.visible


# 8.11 Probar que al cambiar una edad se actualice el total. PASA
async def test_cambiar_edad_actualiza_total(pantalla):
    cargar_formulario(pantalla, "Regular", ["30"])
    pantalla.actualizar_importes()
    pantalla.ESPERA_AVANCE = 0  # sin esperar a que se termine de escribir para pasar a la card siguiente
    campo = pantalla.campos_edad[0]
    campo.value = "3"
    await pantalla.avanzar_al_terminar_de_escribir(SimpleNamespace(control=campo))
    assert pantalla.texto_subtotal.value == "Subtotal: $ 10.000,00"
    assert pantalla.texto_descuentos.value == "Descuento: - $ 10.000,00"
    assert pantalla.texto_total.value == "Total: $ 0,00"
