# Trabajo Practico 6: Test Driven Development

## Detalles Tecnicos

### Requisitos previos

- [Python](https://www.python.org/downloads/) 3.10 o superior.
- [uv](https://docs.astral.sh/uv/) como gestor de dependencias y entornos virtuales.

### Dependencias

Para descargar las dependencias del proyecto, desde la carpeta del proyecto (`tp_6_tdd`), ejecutá:

```bash
uv sync
pip install python-dotenv
```

### Inicializar el proyecto

Ejecutar como aplicación de escritorio:

```bash
 python -m uv run flet run
```

### Ejecutar como Aplicación Mobile

Para probar la app en un celular durante el desarrollo:

1. Instalá la app Flet en el celular.
2. Conectá la computadora y el celular a la misma red Wi-Fi.
3. Ejecutá el comando según el sistema del dispositivo:

   Android:

   ```bash
   python -m uv run flet run --android
   ```

   iOS:

   ```bash
   python -m uv run flet run --ios
   ```

4. En la terminal se mostrará un código QR (y una URL). Escanealo desde la app Flet del celular para abrir la aplicación.

>Si el celular no logra conectarse, verificá que el firewall de la computadora permita conexiones entrantes al puerto que muestra la terminal.

### Ejecutar los tests

Con el siguiente comando, teniendo instalado pytest:

```bash
python -m uv run pytest -v -rs
```

#### Ejecutar el envio de mail real

Para correr los test de "envio mail" con el servidor de gmail real (y no un mockup) hay que crear un archivo ".env". Analizar el archivo ".env.example" para realizar la carga de datos correspondientes respecto al mail destino (creado especificamente para este trabajo practico). Luego hay que ejecutar el siguiente comando:

```bash
$env:ENVIAR_MAIL_REAL="1"; python -m uv run pytest -v -k mail_real -s
```

#### Ejecutar el pago real con Mercado Pago

La compra con tarjeta usa `PasarelaMercadoPago`, que se integra con Checkout Pro y crea la preferencia de pago, abre el checkout en el navegador y consulta a Mercado Pago hasta que el pago se aprueba o se rechaza. Es un singleton: toda la aplicación usa la misma instancia, y los tests la reinician con `PasarelaMercadoPago.reiniciar()` para crearla con otra configuración. Los tests de `tests/test_mercado_pago.py` (6.1, 6.2 y 6.3) corren contra tres pasarelas: `falsa` (doble de prueba), `simulada` (`PasarelaMercadoPago` con un SDK simulado, sin conexión) y `real` (Mercado Pago de verdad, solo con `MP_PAGO_REAL=1`). Para probar contra Mercado Pago:

1. Entrar a [tus integraciones](https://www.mercadopago.com.ar/developers/panel/app), crear una aplicación (producto Checkout Pro) y, en cuentas de prueba, crear un usuario vendedor y uno comprador.
2. Copiar el access token de la cuenta vendedora de prueba en el `.env` como `MP_ACCESS_TOKEN` (ver `.env.example`).
3. Crear una preferencia real (no cobra nada):

   ```bash
   python -m uv run pytest -v -k preferencia_real -s
   ```

4. Hacer el pago completo. Cada test imprime un link: abrirlo en incógnito, iniciar sesión con el usuario comprador de prueba y pagar con una [tarjeta de prueba](https://www.mercadopago.com.ar/developers/es/docs/checkout-pro/additional-content/your-integrations/test/cards). El nombre del titular define el resultado: `APRO` aprueba el pago y `FUND` lo rechaza por saldo insuficiente; el test indica cuál usar (6.1 usa `APRO`, 6.2 y 6.3 usan `FUND`).

   ```bash
   $env:MP_PAGO_REAL="1"; python -m uv run pytest -v tests/test_mercado_pago.py -k real -s
   ```
