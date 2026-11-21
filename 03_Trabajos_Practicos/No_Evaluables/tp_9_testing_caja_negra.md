# Práctico 9: Testing - Métodos de Caja Negra

Unidad Nro. 4: Aseguramiento de Calidad de Proceso y de Producto

Curso 4K3 - Grupo 7

Consigna: diseñar las pruebas de caja negra de la user story que nos toca usando partición de equivalencias y análisis de valores límite (donde se pueda), y definir la cantidad mínima de casos de prueba que cubran todas las clases y todas las pruebas que pide el PO.

Como somos un grupo impar, trabajamos con la user story "Comprar entradas" de EcoHarmony Park.

## User story

**Comprar entradas** (8 puntos)

COMO visitante QUIERO comprar una entrada PARA asegurar mi visita al parque.

Criterios de aceptación:

- Debe indicar la fecha de visita deseada, la cantidad de entradas requeridas, la edad de cada visitante y tipo de pase (VIP o regular).
- La fecha de visita puede ser del día actual o futuro.
- Debe enviar un mensaje de confirmación vía mail.
- Debe redirigir a Mercado Pago al confirmar la compra si el pago es con tarjeta de crédito.
- La fecha de la visita debe estar dentro de los días en que el parque está abierto.
- Debe seleccionar la forma de pago: efectivo en caso de querer pagar en boletería o con tarjeta.
- La cantidad de entradas requeridas no debe ser mayor a 10.
- Al finalizar la compra se debe informar la cantidad de entradas compradas y la fecha.
- Se debe permitir la compra de entradas solo a usuarios registrados.

Pruebas de usuario del PO:

1. Probar comprar una entrada indicando la fecha de visita dentro de los días disponibles, una cantidad de entradas menor a 10, la edad de todos los visitantes, el tipo de pase, la forma de pago con tarjeta mediante Mercado Pago y recepción del mail de confirmación (pasa).
2. Probar comprar entradas sin seleccionar forma de pago (falla).
3. Probar comprar entradas ingresando una fecha de visita en la cual el parque se encuentra cerrado (falla).
4. Probar comprar entradas ingresando una cantidad de entradas mayor a 10 (falla).

## Supuestos

La user story no dice qué días está abierto el parque ni qué edades son válidas, así que usamos lo mismo que definimos cuando la implementamos en el TP6:

- El parque abre de martes a domingo, y cierra los lunes, el 25/12 y el 1/1.
- Se pueden comprar entre 1 y 10 entradas.
- La edad de cada visitante va de 0 a 100 años, y se carga una edad por cada entrada.

Para que las pruebas se puedan repetir, tomamos como fecha actual el jueves 19/11/2026 a las 10:00. El usuario registrado que usamos es Lucía Gómez (`lucia.gomez@mail.com`), que ya tiene la sesión iniciada. Para los pagos con tarjeta usamos una cuenta compradora de prueba de Mercado Pago con una tarjeta que aprueba el pago. Todos los datos son inventados.

En el TP6 también pusimos que solo se puede comprar con un mes de anticipación y que para el mismo día se puede comprar hasta las 17:30. Como eso no está en la user story no lo tomamos como clases, lo dejamos para preguntarle al PO (está al final).

## Clases de equivalencia de entrada

Numeramos las clases para después poder indicar cuáles cubre cada caso de prueba.

### Usuario

- Válida: (1) usuario registrado con sesión iniciada.
- Inválida: (2) usuario no registrado.

### Fecha de visita

- Válidas: (3) la fecha actual, con el parque abierto; (4) una fecha futura en la que el parque está abierto, o sea de martes a domingo y que no sea 25/12 ni 1/1.
- Inválidas: (5) una fecha anterior a la actual; (6) una fecha futura que cae lunes; (7) una fecha futura que es 25/12 o 1/1; (8) no se ingresa la fecha; (9) una fecha que no existe o con formato inválido, por ejemplo 31/11/2026.

### Cantidad de entradas

- Válida: (10) un número entero entre 1 y 10.
- Inválidas: (11) un entero menor a 1; (12) un entero mayor a 10; (13) un valor que no es entero, como letras o decimales; (14) no se ingresa la cantidad.

### Edad de cada visitante

- Válida: (15) un número entero entre 0 y 100.
- Inválidas: (16) un entero menor a 0; (17) un entero mayor a 100; (18) un valor que no es entero; (19) se deja vacía la edad de algún visitante.

### Edades cargadas respecto de la cantidad de entradas

- Válida: (20) hay una edad por cada entrada.
- Inválida: (21) la cantidad de edades no coincide con la cantidad de entradas.

### Tipo de pase

- Válidas: (22) VIP; (23) Regular.
- Inválida: (24) no se selecciona tipo de pase.

### Forma de pago

- Válidas: (25) efectivo, para pagar en boletería; (26) tarjeta.
- Inválida: (27) no se selecciona forma de pago.

## Clases de equivalencia de salida

- (28) Si paga con tarjeta, la app lo redirige a Mercado Pago.
- (29) Si paga en efectivo, la compra se confirma sin redirigir y se paga en boletería.
- (30) Al terminar se informa la cantidad de entradas compradas y la fecha de la visita.
- (31) Se envía el mail de confirmación.
- (32) Cuando algún dato es inválido, la compra no se confirma, se avisa cuál es el dato con error y no se redirige a Mercado Pago.
- (33) Cuando la compra no se confirma, no se envía el mail.

## Valores límite

Aplicamos valores límite en las condiciones que tienen un rango: la cantidad de entradas, la edad y la fecha.

En la cantidad de entradas el rango es de 1 a 10, así que probamos 0 y 1 en el límite de abajo, y 10 y 11 en el de arriba. El 1 va en el CP01, el 10 en el CP02, el 11 en el CP05 y el 0 en el CP07.

En la edad el rango es de 0 a 100. Probamos -1 y 0 abajo, y 100 y 101 arriba. El 0 está en el CP01, el 100 en el CP02, el -1 en el CP11 y el 101 en el CP12.

Para la fecha, el límite de abajo es el día actual: el 19/11/2026 tiene que andar (CP01) y el 18/11/2026 no (CP08). También tomamos como borde el lunes en que cierra el parque: el lunes 23/11/2026 tiene que fallar (CP04) y el martes 24/11/2026 tiene que andar (CP02). Para el feriado probamos el viernes 25/12/2026 (CP06). El 24/12 y el 26/12 son de la misma clase válida que el 24/11, así que no agregamos casos para esas fechas.

## Casos de prueba

En todos los casos el visitante entra a "Comprar entradas", carga la fecha, la cantidad, las edades, elige el pase y la forma de pago, y confirma. Salvo el CP09, siempre es Lucía con la sesión iniciada. En los casos que tienen que fallar cambiamos un solo dato por vez y dejamos el resto bien, así sabemos qué es lo que hizo fallar la compra.

### CP01 - Comprar una entrada para hoy con tarjeta (prueba 1 del PO)

Prioridad alta. Cubre las clases 1, 3, 10, 15, 20, 22, 26, 28, 30 y 31.

Lucía carga la fecha 19/11/2026, 1 entrada, edad 0, pase VIP y pago con tarjeta. Confirma, la app la manda a Mercado Pago y paga con la tarjeta de prueba.

Resultado esperado: el pago se aprueba, la app le informa que compró 1 entrada para el 19/11/2026 y le llega el mail de confirmación a `lucia.gomez@mail.com`.

### CP02 - Comprar 10 entradas para otro día pagando en efectivo

Prioridad alta. Cubre las clases 1, 4, 10, 15, 20, 23, 25, 29, 30 y 31.

Lucía carga la fecha 24/11/2026 (un martes, el día después del cierre), 10 entradas, las edades 100, 65, 40, 38, 15, 12, 8, 5, 3 y 1, pase Regular y pago en efectivo.

Resultado esperado: la compra se confirma sin pasar por Mercado Pago, se informa que compró 10 entradas para el 24/11/2026 y le llega el mail.

### CP03 - Comprar sin elegir forma de pago (prueba 2 del PO)

Prioridad alta. Cubre las clases 27, 32 y 33.

Fecha 24/11/2026, 2 entradas con edades 30 y 28, pase Regular, y no elige forma de pago.

Resultado esperado: no se confirma la compra, la app pide que seleccione una forma de pago y no se envía mail.

### CP04 - Comprar para un lunes (prueba 3 del PO)

Prioridad alta. Cubre las clases 6, 32 y 33.

Igual que el anterior pero con fecha 23/11/2026 y pago en efectivo.

Resultado esperado: no se confirma la compra, se avisa que el parque está cerrado ese día y no se envía mail.

### CP05 - Comprar 11 entradas (prueba 4 del PO)

Prioridad alta. Cubre las clases 12, 32 y 33.

Fecha 24/11/2026, 11 entradas, todas con edad 30, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se avisa que el máximo es de 10 entradas y no se envía mail.

### CP06 - Comprar para Navidad

Prioridad alta. Cubre las clases 7, 32 y 33.

Fecha 25/12/2026, 2 entradas con edades 30 y 28, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se avisa que el parque está cerrado ese día y no se envía mail.

### CP07 - Comprar 0 entradas

Prioridad media. Cubre las clases 11, 32 y 33.

Fecha 24/11/2026, cantidad 0, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se avisa que tiene que comprar al menos una entrada y no se envía mail.

### CP08 - Comprar para ayer

Prioridad alta. Cubre las clases 5, 32 y 33.

Fecha 18/11/2026, 2 entradas con edades 30 y 28, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se avisa que la fecha no puede ser anterior a hoy y no se envía mail.

### CP09 - Comprar sin estar registrado

Prioridad alta. Cubre las clases 2, 32 y 33.

Un visitante que no tiene cuenta entra a "Comprar entradas" e intenta comprar 2 entradas para el 24/11/2026, edades 30 y 28, pase Regular, efectivo.

Resultado esperado: la app no lo deja comprar y le pide que se registre o inicie sesión. No se envía mail.

### CP10 - Comprar sin elegir el tipo de pase

Prioridad media. Cubre las clases 24, 32 y 33.

Fecha 24/11/2026, 2 entradas con edades 30 y 28, no elige pase, efectivo.

Resultado esperado: no se confirma la compra, se pide que elija el tipo de pase y no se envía mail.

### CP11 - Cargar una edad negativa

Prioridad media. Cubre las clases 16, 32 y 33.

Fecha 24/11/2026, 2 entradas con edades 30 y -1, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se marca como inválida la edad del segundo visitante y no se envía mail.

### CP12 - Cargar una edad mayor a 100

Prioridad media. Cubre las clases 17, 32 y 33.

Lo mismo que el CP11 pero con edades 30 y 101.

Resultado esperado: no se confirma la compra, se marca como inválida la edad del segundo visitante y no se envía mail.

### CP13 - Cargar menos edades que entradas

Prioridad media. Cubre las clases 21, 32 y 33.

Fecha 24/11/2026, 3 entradas pero solo dos edades (30 y 28), pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se avisa que falta la edad de un visitante y no se envía mail.

### CP14 - Escribir la cantidad con letras

Prioridad baja. Cubre las clases 13, 32 y 33.

Fecha 24/11/2026, en cantidad escribe "dos", edades 30 y 28, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se avisa que la cantidad tiene que ser un número entero y no se envía mail.

### CP15 - Dejar vacía la cantidad

Prioridad baja. Cubre las clases 14, 32 y 33.

Fecha 24/11/2026, no carga la cantidad, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se pide que cargue la cantidad de entradas y no se envía mail.

### CP16 - Escribir una edad con letras

Prioridad baja. Cubre las clases 18, 32 y 33.

Fecha 24/11/2026, 2 entradas con edades 30 y "abc", pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se avisa que la edad tiene que ser un número entero y no se envía mail.

### CP17 - Dejar vacía la edad de un visitante

Prioridad baja. Cubre las clases 19, 32 y 33.

Fecha 24/11/2026, 2 entradas, carga 30 en el primero y deja vacío el segundo, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se pide la edad del segundo visitante y no se envía mail.

### CP18 - Comprar sin cargar la fecha

Prioridad media. Cubre las clases 8, 32 y 33.

No carga la fecha, 2 entradas con edades 30 y 28, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se pide la fecha de visita y no se envía mail.

### CP19 - Cargar una fecha que no existe

Prioridad baja. Cubre las clases 9, 32 y 33.

Fecha 31/11/2026, 2 entradas con edades 30 y 28, pase Regular, efectivo.

Resultado esperado: no se confirma la compra, se avisa que la fecha no es válida y no se envía mail.

## Cobertura

Las cuatro pruebas del PO quedan cubiertas: la compra completa con tarjeta es el CP01, la compra sin forma de pago es el CP03, la del parque cerrado es el CP04 (y también el CP06, con el feriado) y la de más de 10 entradas es el CP05.

Con el CP01 y el CP02 cubrimos todas las clases válidas de entrada y las salidas 28 a 31. Hacen falta los dos porque VIP y Regular, y tarjeta y efectivo, no pueden ir en la misma compra. Del CP03 al CP19 hay un caso para cada una de las 17 clases inválidas, y todos verifican las salidas 32 y 33.

En total la cantidad mínima es de 19 casos de prueba: 2 válidos y 17 inválidos.

## Otros escenarios para probar

Hay situaciones que no salen de aplicar los métodos pero que nos parece importante probar, o por lo menos preguntarle al PO cómo tienen que funcionar:

- Qué pasa si Mercado Pago rechaza el pago. ¿Se anula la compra? ¿Le llega algún mail?
- Qué pasa si el usuario cancela o vuelve atrás estando en Mercado Pago.
- Si falla el envío del mail, ¿la compra queda registrada igual?
- Si el usuario cambia la cantidad de entradas después de cargar las edades, los campos de edad se tienen que actualizar.
- Si toca dos veces "Confirmar", no se tiene que registrar ni cobrar la compra dos veces.
- ¿El límite de 10 entradas es por compra o por usuario y por día? Hoy alguien podría hacer dos compras de 10 para la misma fecha.
- Las reglas que pusimos en el TP6 de comprar como mucho con un mes de anticipación y, para el día actual, hasta las 17:30.
- En la entrevista se dice que la app muestra el monto total, pero la user story no dice nada de precios ni descuentos por edad. Si el PO lo define, se podrían agregar clases de salida para el monto.
