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
pip install python-dotenv
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
 python -m uv run flet run
```

Ejecutar como aplicación web:

```bash
python -m uv run flet run --web
```

### Ejecutar como Aplicación Mobile

Para probar la app en un celular durante el desarrollo:

1. Instalá la app **Flet** en el celular.
2. Conectá la computadora y el celular a la **misma red Wi-Fi**.
3. Ejecutá el comando según el sistema del dispositivo:

   Android:

   ```bash
   python -m uv run flet run --android
   ```

   iOS:

   ```bash
   python -m uv run flet run --ios
   ```

4. En la terminal se mostrará un **código QR** (y una URL). Escanealo desde la app Flet del celular para abrir la aplicación.

Los cambios en el código se recargan automáticamente en el dispositivo (hot reload).

>Si el celular no logra conectarse, verificá que el firewall de la computadora permita conexiones entrantes al puerto que muestra la terminal.

El punto de entrada de la aplicación es `main.py`, en la raíz del proyecto. Desde ahí se abre la pantalla de inicio (`boundaries/pantalla_inicio.py`).
También se puede ejecutar directamente con `python -m uv run python main.py`.

El proyecto está organizado en capas:

- `boundaries/`: pantallas de la aplicación (inicio, formulario de compra y resultado del pago).
- `controllers/`: `ControllerComprarEntrada`, que coordina la compra.
- `entities/`: entidades del dominio (`Usuario`, `Entrada`, `Parque`, `TipoPase`), la pasarela de Mercado Pago y el adaptador de mail.

### Ejecutar los tests

```bash
python -m pytest -q
```

Los tests se encuentran en la carpeta `tests/`.

#### Ejecutar el envio de mail real

Para correr los test de "envio mail" con el servidor de gmail real (y no un mockup) hay que crear un archivo ".env". Analizar el archivo ".env.example" para realizar la carga de datos correspondientes respecto al mail destino (creado especificamente para este trabajo practico). Luego hay que ejecutar el siguiente comando:

```bash
$env:ENVIAR_MAIL_REAL="1"; python -m pytest -q -k mail_real -s
```

#### Ejecutar el pago real con Mercado Pago

La compra con tarjeta usa `PasarelaMercadoPago` (`src/pasarela_mercado_pago.py`), que se integra con **Checkout Pro**: crea la preferencia de pago, abre el checkout en el navegador y consulta a Mercado Pago hasta que el pago se aprueba o se rechaza. Los tests de `tests/test_compra_mercado_pago.py` (6.1, 6.2 y 6.3) corren contra tres pasarelas: `falsa` (doble de prueba), `simulada` (`PasarelaMercadoPago` con un SDK simulado, sin conexión) y `real` (Mercado Pago de verdad, solo con `MP_PAGO_REAL=1`). Para probar contra Mercado Pago:

1. Entrar a [Tus integraciones](https://www.mercadopago.com.ar/developers/panel/app), crear una aplicación (producto *Checkout Pro*) y, en **Cuentas de prueba**, crear un usuario **vendedor** y uno **comprador**.
2. Copiar el *Access Token* de la cuenta vendedora de prueba en el `.env` como `MP_ACCESS_TOKEN` (ver `.env.example`).
3. Crear una preferencia real (no cobra nada):

   ```bash
   python -m pytest -q -k preferencia_real -s
   ```

4. Hacer el pago completo. Cada test imprime un link: abrirlo en incógnito, iniciar sesión con el **usuario comprador de prueba** y pagar con una [tarjeta de prueba](https://www.mercadopago.com.ar/developers/es/docs/checkout-pro/additional-content/your-integrations/test/cards). El nombre del titular define el resultado: `APRO` aprueba el pago y `FUND` lo rechaza por saldo insuficiente; el test indica cuál usar (6.1 usa `APRO`, 6.2 y 6.3 usan `FUND`).

   ```bash
   $env:MP_PAGO_REAL="1"; python -m pytest -q tests/test_compra_mercado_pago.py -k real -s
   ```
