## ROLES:

- **Cliente:** usuario del dominio que se registra y usa el sistema para hacer un pedido.
- **administrador de producto:** usuario del dominio que se encarga de manejar el stock de productos y los datos de los mismos.
- **proveedor de envio:** usuario del domino que se encarga de todo lo relacionado al envío de un paquete
- **vendedor:** usuario del dominio que interactúa con las ventas, descuentos y reclamos en el sistema.

## Hipótesis:

Hay un grupo de usuarios que se benefician de un sistema que permita la administración de stock, venta y reporte de insumos y productos relacionados al body painting.

## Listado de User stories con su frase verbal:

### US 1: registrarse como cliente

Como cliente quiero registrar mis datos para poder realizar un pedido en el sistema

**criterios de aceptación:**

- se debe registrar datos personales, email, y dirección

**pruebas de aceptación:**

- probar realizar un pedido sin ser cliente (falla)
- probar realizar un pedido sin tener dirección (falla)
- probar cargar datos personales (pasa)
- probar elegir una dirección cargada anteriormente (pasa)
- Probar cargar una dirección sin piso y departamento (pasa)

### US2: Actualizar carro de compras agregando o quitando productos

como cliente quiero actualizar mi carrito de compras para que mi pedido tenga los productos que deseo.

**criterios de aceptación:**

- el cliente debe poder agregar y quitar productos del carrito
- el cliente debe visualizar el total de su carrito en todo momento

*agregar post corrección*

- se debe ingresar la cantidad de cada producto, poniendo 1 por defecto
- se puede modificar la cantidad de productos de cada uno

**pruebas de aceptación:**

- probar agregar un producto a un carrito (pasa)
- probar agregar un producto sin ser cliente (pasa)
- probar visualizar el total del carrito (pasa)
- probar armar un carrito con cantidad = 0 (falla)
- probar armar un carrito con productos sin stock (falla)
- probar armar un carrito con productos simples y kits informando cantidad de cada producto y viendo el total (pasa)

### US3: confirmar pedido

como cliente quiero confirmar mi pedido para continuar con el proceso de la compra de un producto

**criterios de aceptación:**

- el comprador debe estar registrado como cliente
- el cliente debe tener productos en su carrito
- el cliente debe seleccionar un domicilio de envío
- el cliente puede cargar un domicilio nuevo
- el cliente debe seleccionar una única forma de pago
  - consideración: si se elige pago en tarjeta o mercado pago, se lo redireccionará como corresponda
- el cliente puede agregar un cupón de descuento

**pruebas de aceptación:**

- probar confirmar un pedido sin ser cliente (falla)
- probar confirmar un pedido de cliente con productos en el carrito (pasa)
- probar agregar un domicilio nuevo (pasa)
- probar confirmar el pedido sin un domicilio(falla)
- probar seleccionar más de una forma de pago (falla)
- probar agregar un cupón de descuento superior al monto de la compra (falla)
- probar agregar un cupón de descuento que no corresponde al cliente elegido (falla)
- probar agregar un cupón de descuento inexistente (Falla)
- probar agregar un cupon de compra para el cliente elegido y cuyo monto no supere el total de la compra (pasa)

### US4: acceder a la información del perfil de cliente

como cliente quiero poder acceder a mi información para mantener los datos en el perfil actualizados siempre

**criterios de aceptación:**

- el cliente puede acceder a su perfil
- el cliente puede modificar sus datos

**pruebas de aceptación:**

- probar acceder a un perfil ajeno (falla)
- probar acceder a mi perfil propio (pasa)
- probar cambiar los datos de mi domicilio por defecto (pasa)

### US5: Registrar datos de pago con tarjeta

como usuario quiero agregar una nueva tarjeta como forma de pago registrando sus datos para tener accesibilidad a la hora del pago

**criterios de aceptación:**

- el cliente puede agregar una nueva forma de pago
- el cliente debe agregar los datos de esta nueva forma de pago
- los datos deben ser verificados por la entidad correspondiente

**pruebas de aceptación:**

- probar avanzar sin poner todos los datos solicitados (falla)
- probar avanzar agregando datos falsos (falla)
- probar conectar con la entidad bancaria (pasa )
- probar cargar una tarjeta de crédito verídica con todos los datos correspondientes (pasa)

---

- US6:Recibir notificación de confirmación de pedido
- US7: Visualizar producto (realizado por el cliente)
- US8: Acceder a información de producto (permiso de administrador)
- US9: recibir notificación sobre Stock para reposición
- US10: Modificar información de un producto (administrador)
- US11: Registrar un producto
- US12: Registrar una partida de productos recibidos.
- US13:Generar numero de Tracking del pedido
- US 14: Acceder al tracking del pedido
- US15: recibir notificación sobre actualización en el estado del pedido
- US 16: acceder a información sobre pedidos realizados
- US 17: Envía notificación de pedido listo para entregar
- US 17: Cancelar entrega
- US 18: Reclamar entrega o reembolso
- US 19: Registrar respuesta a reclamo
- US20: Generar cupón de descuento
- US21: Recibir notificación de descuento
- US 22: generar reportes de productos más vendidos
- US 23: Generar reporte de zonas con más pedidos
- US 24: Generar ranking de clientes con más compras
- US 25: registrar nuevo domicilio

### agregó luego de la corrección:

- us26: registrar pedido completado
- us 27: configurar stock mínimo de producto
- us28: armar kit de productos
- us 29: recargar imagen de producto
- us 30: dar de baja producto

## MVP:

se desarrollara un sistema que permita la prueba con el cliente sobre un registro de cliente, el uso de este perfil para visualizar los productos cargados, crear un carrito y realizar una compra, con forma de pago unicamente en efectivo y sin ningún descuento (elegida esta forma de pago por su simpleza). con un domicilio cargado en la compra; además le permitirá a los usuarios del lado del negocio (cuyos usuarios crearemos de manera rudimentaria y manualmente nosotros) cargar un nuevo producto individual.

**User stories elegidas:** 1, 2, 3, 7, 11

**Alcance:** NO se contempla, el módulo de reportaje, no se contemplan distintas formas de pago o descuentos creados por el administrador, no se contemplan las notificaciones automatizadas, ni creación de nuevas formas de pago o lugares de envío. Por considerar que con lo elegido tenemos suficientes utilidades para demostrar el valor del sistema confeccionado. tampoco contempla el manejo de reclamos

## User story canónica y justificación:

**US 25: Registrar nuevo domicilio:** elegida por considerarse de baja complejidad y bajo esfuerzo, además de baja incertidumbre. Se trata de la carga de datos estilo formulario, desde el lado del cliente.

se estima

## User stories con sus criterios y pruebas de aceptacion; estimación con SP:

> **notas:** reportería sobre kits y productos bajos en stock.
