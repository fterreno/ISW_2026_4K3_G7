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

#### Ejecutar el envio de mail real

Para correr los test de "envio mail" con el servidor de gmail real (y no un mockup) hay que crear un archivo ".env". Analizar el archivo ".env.example" para realizar la carga de datos correspondientes respecto al mail destino (creado especificamente para este trabajo practico). Luego hay que ejecutar el siguiente comando:

```bash
$env:ENVIAR_MAIL_REAL="1"; python -m pytest -q -k mail_real -s
```
