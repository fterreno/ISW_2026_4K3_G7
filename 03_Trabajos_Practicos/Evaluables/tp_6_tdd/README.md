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

## Registro de las tres pruebas RED de cantidad y edades — 08/10/2026

Después del avance anterior revisé los casos de cantidad y edades. Agregué tres pruebas independientes en los archivos existentes, sin cambiar las pruebas del grupo ni la implementación de Caterina.

### Qué comprobé y por qué agregué las pruebas

| Prueba | Regla o antecedente | Comportamiento actual | RED observado |
|---|---|---|---|
| `test_cantidad_flotante_sin_decimales_es_invalida` | La cantidad debe ser entera; el grupo definió que los valores flotantes se rechazan | `validar_cantidad(2.0)` devuelve `2` | `DID NOT RAISE ErrorValidacion` |
| `test_edad_flotante_sin_decimales_es_invalida` | La edad debe ser entera; el grupo definió que los valores flotantes se rechazan | `validar_edad(8.0)` devuelve `8` | `DID NOT RAISE ErrorValidacion` |
| `test_edades_con_cero_cuenta_todos_los_visitantes` | Ya existe una prueba que acepta edad `0`; el conteo debe ser coherente con esa validación | `validar_edades([30, 0], cantidad=2)` informa que falta una edad | Lanza `ErrorValidacion` en vez de devolver `[30, 0]` |

Aunque `2.0` y `8.0` no tengan una parte decimal distinta de cero, en Python son valores de tipo `float`. Estas pruebas cubren ese caso que las pruebas de decimales anteriores no detectaban.

La prueba con cero no establece una edad mínima oficial. Comprueba la coherencia entre la validación individual existente y la validación de todas las edades. El rango de edad sigue pendiente de la cátedra.

### Resultado después de cada prueba

| Paso | Aprobadas | Fallidas | Total |
|---|---:|---:|---:|
| Antes de agregar estas pruebas | 48 | 26 | 74 |
| Agregué el rechazo de cantidad `2.0` | 48 | 27 | 75 |
| Agregué el rechazo de edad `8.0` | 48 | 28 | 76 |
| Agregué el conteo con edad `0` | 48 | 29 | 77 |

Ejecuté la suite completa después de cada prueba. El resultado final corresponde a la revisión `fbfbe85`: **48 aprobadas y 29 fallidas**. Las 29 fallidas son los 26 casos anteriores que fallan por funciones pendientes de implementación, más las tres pruebas nuevas en RED. Las 48 que pasaban siguen pasando.

Para repetir solamente las tres pruebas nuevas, desde `tp_6_tdd`:

```bash
python -m pytest -q tests/test_formulario_cantidad_entradas.py::test_cantidad_flotante_sin_decimales_es_invalida tests/test_formulario_edad.py::test_edad_flotante_sin_decimales_es_invalida tests/test_formulario_edad.py::test_edades_con_cero_cuenta_todos_los_visitantes
```

Para repetir toda la suite:

```bash
python -m pytest -q
```

### Evidencia publicada y siguiente paso

| Commit | Cambio |
|---|---|
| `2db0699` | Agregué la prueba RED de cantidad flotante `2.0` |
| `fbfbe85` | Agregué las pruebas RED de edad flotante `8.0` y conteo con edad `0` |

Dejé el GREEN pendiente de coordinar con Caterina, que está trabajando cantidad y edades. Todavía no agregué código mínimo ni hice un refactor para estas tres pruebas. El ciclo queda abierto en RED; no lo presento como terminado.

Cuando se haga el GREEN, corresponde registrar el cambio mínimo, ejecutar las tres pruebas y toda la suite, y comparar el resultado con esta revisión. Después se evaluará si hace falta un refactor y se volverán a ejecutar las pruebas si se modifica el diseño.

Este registro deja la evidencia disponible para el PDF del grupo. No cambia los criterios de aceptación ni resuelve los pendientes de la cátedra.

## Registro de mi revisión del GREEN del formulario — 09/10/2026

Revisé el commit `d59d844`, publicado por Ulises en `trabajo-practico-tdd-green-formulario`. Creé este registro en `docs-tp6-evidencia-green`, que parte de ese mismo commit, para documentar la revisión sin modificar su implementación. Los registros anteriores describen los resultados de sus respectivas revisiones y se conservan como evidencia histórica.

### Qué cambió Ulises

El commit modifica únicamente `src/formulario_entrada.py`. Además de implementar `registrar_formulario`, implementa `validar_fecha`, corrige el rechazo de flotantes en cantidad y edad, y cambia la validación de la lista de edades. No cambia los tests.

`registrar_formulario` valida primero la cantidad y luego construye `FormularioEntrada` con la fecha, las edades, el tipo de pase y la forma de pago validados. Mantiene las funciones, enums y `ErrorValidacion` existentes.

### De las tres pruebas RED al GREEN

| Prueba que agregué antes | RED observado en `fbfbe85` | Cambio de Ulises en `d59d844` | Resultado actual |
|---|---|---|---|
| `test_cantidad_flotante_sin_decimales_es_invalida` | No se lanzaba `ErrorValidacion` para `2.0` | Rechaza cualquier valor de tipo `float` en `validar_cantidad` | Pasa |
| `test_edad_flotante_sin_decimales_es_invalida` | No se lanzaba `ErrorValidacion` para `8.0` | Rechaza cualquier valor de tipo `float` en `validar_edad` | Pasa |
| `test_edades_con_cero_cuenta_todos_los_visitantes` | Se informaba que faltaba una edad para `[30, 0]` | Valida cada edad y compara la longitud de la lista con la cantidad | Pasa |

El cambio mínimo que permite rechazar los flotantes consiste en comprobar `isinstance(valor, float)`, sin aceptar un float por coincidir numéricamente con su conversión a entero.

Para las edades, Ulises reemplazó el conteo basado en el valor verdadero o falso de cada edad por:

```python
edades_validadas = [validar_edad(edad) for edad in edades]
if len(edades_validadas) != cantidad:
    raise ErrorValidacion("Las cantidades de edades y la cantidad de entradas no coincide.")
return edades_validadas
```

Así, cero cuenta como una edad cargada y la función devuelve los enteros que produjo `validar_edad`, en coherencia con `list[int]`. Esto mantiene la prueba existente que acepta cero; no establece una edad mínima oficial.

El GREEN de estos casos pertenece a Ulises. Mi aporte fue agregar las tres pruebas RED anteriores y registrar esta verificación. No hice un refactor ni registré como propio el código de otro integrante. Tampoco observé la ejecución intermedia del ciclo de Ulises: verifiqué la revisión publicada y la comparé con la evidencia RED previa.

### Resultado de la verificación

Ejecuté la suite del commit `d59d844` con Python 3.12.14 y pytest 9.1.1: **77 casos, 68 aprobados y 9 fallidos**. Frente a `fbfbe85`, pasaron 20 casos adicionales y se mantuvieron las 48 pruebas que ya pasaban.

| Revisión | Aprobadas | Fallidas | Total |
|---|---:|---:|---:|
| `fbfbe85`, después de las tres pruebas RED | 48 | 29 | 77 |
| `d59d844`, GREEN publicado por Ulises | 68 | 9 | 77 |

Los nueve fallos restantes se deben a `NotImplementedError` en `registrar_compra`, `generar_mail` o `enviar_mail`:

| Archivo | Casos fallidos |
|---|---:|
| `tests/test_compra_finalizacion.py` | 1 |
| `tests/test_compra_mail.py` | 5 |
| `tests/test_compra_pago.py` | 3 |

Desde `tp_6_tdd`, puedo repetir la suite con:

```bash
python -m pytest -q
```

Este resultado acredita las pruebas de Python ejecutadas. No demuestra la compra completa, la integración real con Mercado Pago, la entrega real de mail ni el funcionamiento responsive de Flet.

### Decisiones que todavía requieren confirmación

En `validar_fecha`, el commit recibe texto y lo interpreta con `dd/mm/aaaa`. El grupo tiene pruebas para esa entrada, pero sigue pendiente confirmar si la interfaz usará ingreso manual o calendario. No doy por aprobada la entrada manual como decisión final de la cátedra.

La función también impide comprar para hoy cuando la hora actual está fuera del horario configurado. Esa restricción no figura en los criterios oficiales que registramos. Tener una prueba que acepta comprar dentro del horario no alcanza para justificar el rechazo fuera de él. La dejo pendiente de consulta antes de considerarla una regla definitiva.

Los días y horarios se reciben mediante `HorarioParque`; no están fijados dentro de la función. La fixture usa martes a domingo de 9 a 18 como supuesto. Los días exactos, los horarios si corresponden y el rango de edades siguen pendientes de la cátedra.

En mail, revisé que `test_mail_vacio_no_se_envia` prueba asunto y cuerpo vacíos, no el email del usuario registrado. Debemos distinguir esos casos al explicarlos: no hay que presentarlo como una validación del registro del usuario.

### Qué sigue

- Coordinar con el grupo las decisiones pendientes de fecha y horario antes de modificar ese comportamiento.
- Coordinar con Flor el flujo de compra, Mercado Pago real y mail. Una pasarela falsa en los tests no acredita la integración real exigida.
- Completar la confirmación de compra y el mensaje final con cantidad y fecha; un pago no confirmado no debe provocar el envío del mail.
- Conectar la lógica al formulario Flet y probar el recorrido en web y celular.
- Seguir registrando RED, GREEN y refactors reales, con resultados y commits, para el PDF.

Este avance modifica solamente la documentación del TP6 en `docs-tp6-evidencia-green`. No modifica `main`, no hace merge y no reescribe el historial del grupo.
