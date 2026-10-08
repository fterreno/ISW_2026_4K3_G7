# Trabajo Practico 6: Test Driven Development

## Detalles Tecnicos

### Requisitos previos

- [Python](https://www.python.org/downloads/) 3.10 o superior.
- [uv](https://docs.astral.sh/uv/) como gestor de dependencias y entornos virtuales.

Si no tenés `uv` instalado:

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Linux / macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

También se puede instalar con pip: `pip install uv`.

Verificá la instalación con:

```bash
uv --version
```

### Dependencias

Para descargar las dependencias del proyecto, desde la carpeta del proyecto (`tp_6_tdd`), ejecutá:

```bash
uv sync
```

Este comando:

- Crea el entorno virtual en la carpeta `.venv` (si no existe).
- Instala las dependencias del proyecto (`flet`) y las de desarrollo (`flet-cli`, `flet-desktop`, `flet-web` y `flet[test]` con `pytest`), usando las versiones fijadas en `uv.lock`.

> Opcional: para activar el entorno virtual manualmente
>
> - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
> - Linux / macOS: `source .venv/bin/activate`
>
> No es necesario si usás `uv run`, que ejecuta los comandos dentro del entorno automáticamente.

### Inicializar el proyecto

Ejecutar como aplicación de escritorio:

```bash
uv run flet run
```

Ejecutar como aplicación web:

```bash
uv run flet run --web
```

### Ejecutar como Aplicación Mobile

Para probar la app en un celular durante el desarrollo:

1. Instalá la app **Flet** en el celular.
2. Conectá la computadora y el celular a la **misma red Wi-Fi**.
3. Ejecutá el comando según el sistema del dispositivo:

   Android:

   ```bash
   uv run flet run --android
   ```

   iOS:

   ```bash
   uv run flet run --ios
   ```

4. En la terminal se mostrará un **código QR** (y una URL). Escanealo desde la app Flet del celular para abrir la aplicación.

Los cambios en el código se recargan automáticamente en el dispositivo (hot reload).

>Si el celular no logra conectarse, verificá que el firewall de la computadora permita conexiones entrantes al puerto que muestra la terminal.

El punto de entrada de la aplicación es `src/main.py`.

### Ejecutar los tests

```bash
python -m pytest -q
```

Los tests se encuentran en la carpeta `tests/`.


## Registro de mi avance en TDD — 08/10/2026

Este registro corresponde a mi avance sobre la rama `trabajo-practico-tdd`. Lo dejé como base para el PDF del grupo. La User Story es: “Como visitante quiero comprar una entrada para asegurar mi visita al parque”.

### Alcance de este avance

Implementé la validación de VIP o Regular, la selección de Efectivo o Tarjeta y la comparación de una fecha de visita con la fecha actual. Usé Python y mantuve las funciones, enums y la excepción `ErrorValidacion` del módulo `src/formulario_entrada.py`.

Para pase y forma de pago usé las pruebas que ya había escrito el grupo. Para la comparación de fechas agregué tres pruebas independientes en `tests/test_fecha_visita.py`, con objetos `date` y una fecha actual fija. Así no dependen del día en que se ejecutan ni definen cómo será el ingreso en Flet.

La comparación de fechas todavía no está conectada con `validar_fecha` ni con `registrar_formulario`. Este avance no completa el flujo de compra.

### Pruebas de las reglas implementadas

| Regla | Pruebas | Resultado |
|---|---|---|
| Tipo de pase | VIP, Regular y valores inválidos: Premium, vacío y None | 5 pasan |
| Forma de pago, validación directa | Efectivo, Tarjeta y valores inválidos: transferencia y cripto | 4 pasan |
| Fecha de visita, comparación con hoy | Hoy, fecha futura y fecha pasada con mensaje de error | 3 pasan |

Las dos pruebas existentes de compra sin forma de pago siguen fallando porque llaman a `registrar_formulario`, que todavía no está implementado. La función directa ya rechaza valores vacíos; eso no demuestra que el formulario completo los valide.

### Evidencia RED y GREEN

| Paso | RED observado | Código mínimo en GREEN | Suite completa después del GREEN |
|---|---|---|---|
| Tipo de pase | 5 pruebas fallaron por `NotImplementedError` | Comparé el valor con VIP y Regular; devolví su enum o lancé `ErrorValidacion` | 41 pasan, 30 fallan |
| Forma de pago | 4 pruebas directas fallaron por `NotImplementedError` | Comparé el valor con Efectivo y Tarjeta; devolví su enum o lancé `ErrorValidacion` | 45 pasan, 26 fallan |
| Fecha actual | Primero hubo `ImportError` porque no existía la función. Con la firma y `NotImplementedError`, falló la prueba de hoy | Devolví la fecha recibida | 46 pasan, 26 fallan |
| Fecha pasada | La prueba falló con `DID NOT RAISE ErrorValidacion` | Agregué la comparación `fecha < hoy` y el error | 48 pasan, 26 fallan |

Después de aceptar hoy agregué la prueba de fecha futura: ya pasó con el código mínimo anterior. La suite quedó en 47 aprobadas y 26 fallidas. No registré un RED para ese caso porque no ocurrió.

El código final de la comparación es:

```python
def validar_fecha_visita(fecha: date, hoy: date) -> date:
    """Valida hoy o futuro; el formato de ingreso y la apertura se resuelven aparte."""
    if fecha < hoy:
        raise ErrorValidacion("La fecha de visita no puede ser anterior a la fecha actual.")
    return fecha
```

Revisé el diseño después de los GREEN y no encontré una mejora que justificara un refactor en estas funciones. No hice un commit Refactor solamente para completar una etiqueta.

### Commits para reconstruir el avance

| Commit | Contenido |
|---|---|
| `9ac3df2` | GREEN de tipo de pase sobre las pruebas existentes del grupo |
| `78e075c` | GREEN de forma de pago sobre las pruebas existentes del grupo |
| `5f5fbf2` | RED: publiqué las tres pruebas de comparación de fechas antes de publicar la función |
| `2c6ad51` | GREEN: publiqué la comparación de fechas y registré los pasos locales |

Los pasos intermedios de fecha actual, futura y pasada se ejecutaron localmente; el historial publicado contiene un commit de pruebas y uno de implementación. No contiene un commit por cada paso local.

### Verificación y límites

Ejecuté las pruebas con Python 3.12.14 y pytest 9.1.1. Al terminar este avance, sobre la revisión `2c6ad51`, la suite reunió 74 casos: **48 aprobados y 26 fallidos**. Los 26 fallos anteriores se mantuvieron; no hubo regresiones en las pruebas existentes.

Desde `tp_6_tdd`, para repetir las tres pruebas de comparación:

```bash
python -m pytest -q tests/test_fecha_visita.py
```

Para repetir toda la suite:

```bash
python -m pytest -q
```

El resultado de la suite es de lógica en Python. No acredita todavía el funcionamiento de la interfaz Flet, su adaptación a celular, el cobro real ni el envío real de mail.

### Pruebas unitarias e integración

Las validaciones anteriores son pruebas unitarias: comparan entradas y resultados sin conectarse a servicios externos.

La redirección a Mercado Pago y la verificación del pago real corresponden a integración. La fixture `PasarelaFalsa` existente no demuestra esa integración ni reemplaza la exigencia de usar Mercado Pago real.

El envío de mail también necesita verificación con el servicio real. Las pruebas de contenido y las que usan `ServicioMailFalso` pueden comprobar lógica, pero no acreditan una entrega real. La confirmación debe enviarse únicamente cuando la compra quede confirmada; un pago rechazado o pendiente no debe provocar ese envío.

No implementé Mercado Pago ni mail en este avance. El usuario registrado sigue siendo una precondición; no agregué login ni registro.

### Pendientes para completar la User Story

- Confirmar calendario o ingreso manual antes de conectar la fecha al formulario.
- Confirmar los días exactos de apertura y, si corresponde, los horarios. Los valores de la fixture `horario` están declarados como supuestos, no como reglas confirmadas.
- Confirmar edad mínima y máxima. No agregué un rango.
- Confirmar el contenido o formato específico del mail si lo define la cátedra. No agregué una validación de email vacío del usuario.
- Completar `registrar_formulario`, el flujo de compra, la integración real con Mercado Pago, el mail y el mensaje final de cantidad y fecha.
- Revisar con el grupo los casos de flotantes como `2.0` en cantidad y edad, y el conteo de edad `0` en `validar_edades`. Los señalé para coordinar; no modifiqué esas funciones en este avance.

Todavía no registré nuevas aclaraciones de la cátedra que resuelvan estos pendientes.
