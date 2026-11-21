# Caso: festival de folclore

## definir:

- roles
- hipótesis
- MVP: alcance y justificación de las us elegidas
- us completas
- estimación de cada uso, y definición de la canónica

**objetivos:** admin de festivales, diagramación de la programación, venta de entradas, información para futuros festivales

---

## roles:

- **vendedor de entradas:** persona en uno de los cinco puntos de ventas que interactúa con el sistema para la venta de una entrada
- **coordinador del evento:** persona que trabaja en la dirección de cultura, que utilizara el programa para coordinar el festival con su diagramación y ver la información provista por el sistema.
- **administrador de sistema:** persona del equipo de desarrollo que puede interactuar con el sistema para carga de datos o pruebas de aceptación.

## hipótesis:

Hay un grupo de usuarios pertenecientes o aledaños a la dirección de cultura de la municipalidad de la provincia que se benefician de un sistema que los ayude con la organización, venta y análisis futuro del festival de folclore anual.

## listado de USs con solo su frase verbal:

### US1:Registrar grupo musical

como coordinador de evento quiero poder registrar a cada grupo musical del lineup para tener trazabilidad sobre los artistas

### US2:Generar diagramación de la noche

> (criterio de aceptación que los grupos no se superpongan, que no haya espacios y que es una vez por noche)

como administrador del sistema quiero poder crear la diagramación efectuando los cálculos necesarios, para poder organizar las presentaciones

### US3:registrar división de estadio

> (con sectores con su colorcito, filas con sus numeritos y butacas con sus numeritos)

como coordinador del evento quiero registrar la división natural del estadio para tener una visión clara de la cantidad y diferencia de butacas para vender

### US4: Registrar punto de venta de entradas

> (uno de los 5 puntos)

como coordinador del evento quiero registrar los punto de ventas de las entradas para aumentar la seguridad, prevenir estafas y centralizar la distribución de las mismas

### US5: Registrar venta de la entrada

> (considerar que se deben separar por noche en la bd para que no se superpongan, se debe además mantener el sistema en tiempo real porque están en paralelo)

como vendedor quiero registrar la venta de una entrada para mantener un registro de las entradas vendidas y cuales siguen disponibles para la noche

### US6: registrar TYC de entradas

> (tipos precios butacas descuentos vigencias anulaciones)

como coordinador del evento quiero registrar los TYC de las entradas para mantener la mayor transparencia posible con nuestros clientes y equipo de desarrollo respecto a las mismas

### US8: Registrar la cancelación de una entrada

> (y volver a ponerla como disponible para la venta, realizar además el cálculo para saber si se puede cancelar un)

como vendedor quiero registrar la cancelación de la compra de una entrada para poder registrar la devolución del dinero, la baja del registro de compras, la disponibilidad de la butaca, y mantener un registro de las entradas disponibles

### US9: generar entrada

> (utilizando los tyc, y los datos por ley, generar el voucher de entrada con su código de líneas)

como administrador del sistema quiero poder generar la entrada al evento con todas las características que solicite el cliente para poder venderlas y mantener la trazabilidad de las mismas

### US10: Registrar usuario del sistema

> (y darle distintos permisos)

Como administrador del sistema quiero poder registrar un nuevo usuario con su rol y permisos para mantener la seguridad del sistema.

### US que agrego post corrección

- US11: Registrar festival
- us12: Imprimir entrada
- US 13: registrar grupo musical solista
- US 14: registrar grupo musical de más de un artista
- US 15: registrar butacas para venta
- US 16:reporte de asistencia
- US 17:Reporte de ventas

## MVP

**USs1,2,5,9**

agregó post corrección, 4 y 11

No se contempla en el MVP la división del estadio, por considerarse que son datos que se obtendrán de bases de datos previstas. No se contempla tampoco el registro de usuarios del sistema por considerarse que se lo hará antes de comenzar el uso de los clientes del mismo.Los puntos de venta y los TYC de las entradas tampoco se contemplan en el MVP por ser innecesarios para la demostración del funcionamiento del sistema, quedan en el backlog con prioridades altas
