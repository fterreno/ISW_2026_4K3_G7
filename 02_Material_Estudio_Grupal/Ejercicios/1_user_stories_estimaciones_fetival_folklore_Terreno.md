# User Story y Estimaciones: Festival Folklore

## Consigna

Aplicar los conceptos teóricos desarrollados en clase sobre user stories, MVP y estimaciones ágiles.

Para ello: Los docentes representarán a expertos del dominio que expresarán sus necesidades vinculadas al desarrollo un software para la gestión de ventas de entradas para festivales. Los estudiantes realizarán preguntas con el objetivo de acordar juntos el alcance del proyecto, y
determinar:

- Los roles principales
- El MVP, explicando el alcance propuesto para el MVP y justificando la inclusión de las user stories al MVP.
- Las user stories completas.
- La estimación de cada user, identificando la canónica

## Dominio

Anualmente la Dirección de Cultura de la Municipalidad de una localidad de la provincia, organiza un festival de folklore. Este festival tiene una duración de generalmente cinco noches, aunque esto puede variar de año en año. En cada una de las noches actúan distintos grupos folklóricos con reconocimiento regional, provincial y nacional.

El festival se prepara con mucha anticipación y se realiza la diagramación para determinar qué grupos actúan en cada noche y el orden en el que los mismos realizarán sus presentaciones, teniendo en cuenta que los horarios de presentación de los grupos no pueden superponerse y que no pueden quedar espacios sin ninguna presentación entre medio de dos grupos. Considerar que no puede incluirse la participación de un grupo más de una vez para un mismo festival, en una misma noche.

En cada noche se define la hora de inicio de esta, pero no se determina la hora de fin, ya que esta puede variar según si las presentaciones se extienden más de lo previsto.

El Festival se realiza en un único estadio, que está dividido en sectores (A, B, C, etc.), que se identifican con colores diferentes, y cada sector se compone de filas (1, 2, 3, etc.), cada fila, a su vez, está conformada por butacas, las cuales están numeradas.

La venta de entradas se realiza en cinco puntos de venta que se encuentran en funcionamiento simultáneamente: en el estadio donde se realizará el festival, en tres centros comerciales de la ciudad capital y en un centro comercial de la localidad dónde se realiza el festival. No se debe permitir que se venda una misma entrada (una misma butaca de un festival en una misma fecha) en dos puntos de venta diferentes.

Existen distintos tipos de entradas para el público (mayores, menores, jubilados, etc.). El precio de las entradas depende del tipo de entrada y del sector donde se encuentre la butaca, además puede variar de una noche a otra, dependiendo de los grupos musicales que actúan. Por ejemplo, una entrada para mayores en el sector A, que está cerca del escenario, será más costosa que una para mayores en el sector E que está más alejado del mismo y a su vez puede variar de noche en noche el precio de la entrada en la misma ubicación. Las butacas se venden para una noche en particular así es que una misma butaca puede estar disponible, por ejemplo, para la noche 1 y 3, y ocupada para la noche 2, 4 y 5.

También se habilita la venta anticipada de las entradas a un precio menor, un porcentaje de descuento que la Dirección de Cultura determina, al igual que la fecha de vencimiento de ese beneficio, por ejemplo, venta anticipada con un descuento del 10 % hasta un mes antes que empiece el festival. La forma de venta de entradas es únicamente de contado en efectivo. Si un cliente solicita la anulación de la entrada sólo se le reintegra el 50% del monto abonado. Esto se puede hacer hasta 10 días antes del inicio del festival.

La entrada tiene un código de barras para evitar falsificaciones. Además, hay que tener en cuenta que la misma entrada cumple la función de factura, por lo que debe tener los datos requeridos por la ley de facturación, y debe asegurarse de que el número de factura sea único.

La Dirección de Cultura de la Municipalidad ha solicitado a su Área de Sistemas el desarrollo de un sistema de información que le ayude con la administración de los festivales que organiza, la diagramación de la programación y la venta de entradas y brinde información que ayude a la organización de próximos festivales.La
Dirección de Cultura de la Municipalidad tiene licencias para realizar la aplicación con una base de datos Oracle.

Debido a que en las horas pico se suele generar cola en los puntos de venta, es necesario que el sistema genere una entrada en no más de 6 segundos

---

## Desarrollo

### Roles Principales

- Responsable de Diagramacion: Encargado de la planificacion del evento, que inlcuye el cronograma del evento y los grupos a participar.
- Responsable de Venta de Entradas: Encargado de dictar los precios de las entradas, la venta anticipada y la otrganizacion de lugares destinados como puntos de venta.
- Vendedor: Encargado de vender la entrada del festival al cliente.

<span style="color:red">

La cátedra define cuatro roles: Vendedor de Entradas, Responsable de Festival, Responsable de Predio y Director de Cultura de la Municipalidad. El Responsable de Diagramación y  Vendedor coinciden con Responsable de Festival y Vendedor de Entradas.

Responsable de Venta de Entradas no está en la solución. La cátedra le asigna los precios y los puntos de venta al Responsable de Festival. Te faltan dos roles: el Responsable de Predio, que registra el estadio y habilita las butacas, y el Director de Cultura, que es quien pide los reportes.

</span>

### User Stories


<span style="color:red"> Todas prueban reglas de negocio. No tiene pruebas de formato de campo como las tuyas (caracteres en campos numéricos, formato hh:mm). </span>

User stories completas, con la estimacion y la identificacion de la canonica.

    **como** <rol> **quiero** <feature> **para** <valor de negocio>
    Para que una user story sea canonica se debe tener en cuenta su complejidad, con menos insertidumbre y que no conlleve mucho esfuerzo.
    La estimacion se hace con la secuencia de Fibonacci.

#### US01: Registrar Planificacion de Grupos

Estimacion: 2 Story Point. El motivo por los dos puntos son las verificaciones de superposicion horaria y la restriccion de que una banda toque por noche algo que le da esfuerzo al desarrollo. Es una historia de usuario con poca insertidumbre y poca complejidad.

Como responsable de diagramacion quiero registrar los grupos que actuaran en cada noche para evitar superposisicones entre gurpos o espacios sin presentaciones.

Criterios de Aceptacion:

- Se debe poder seleccionar el nombre del grupo.
- Se debe poder registrar la fecha y horario en la que se presentaran.
- No se debe poder cargar un grupo más de una vez en la misma fecha.

Criterios de Prueba de Usuario:

- Probar cargar un grupo en dos noches diferentes. (pasa) <span style="color:red">(falla)</span>
- Probar cargar un grupo dos veces la misma noche. (falla)
- Probar cargar caracteres en la celda de fecha. (falla)
- Probar cargar el horario en un formato diferente de hh:mm. (falla)
- Probar cargar dos grupos cuyo horario se suerpone. (falla)

<span style="color:yellow">

Correcciones de la Historia de Usuario:

- La cátedra la estima en 5 y la considera compleja porque combina varias reglas. Vos la estimaste en 2 con "poca complejidad".
- Sus criterios son las reglas del enunciado: sin superposición, sin huecos entre grupos y cada grupo una sola vez. Además agrega que se puede guardar una diagramación incompleta, y en ese caso no se controlan los huecos. En tu US01 la regla de los huecos no está: la pusiste como advertencia en US02.
- Ojo: el criterio de la cátedra dice que un grupo no puede participar más de una vez "para un mismo festival", sin agregar "en una misma noche". Con ese criterio, tu prueba "cargar un grupo en dos noches diferentes (pasa)" debería fallar. El enunciado admite las dos lecturas, así que consultalo con el docente.

</span>

#### US02: Visualizar Planificacion de Grupos

Estimacion: 1 Story Point. Es una historia con poca complejdiad, insertidumbre y esfuerzo ya que la visualizacion solo consulta los datos ya existentes renderizando estos datos en el frontend como una ayuda visual para el responsable de diagramacion.

Como responsable de diagramacion quiero vizualizar el orden en el que los grupos se presentaran para poder tener un registro del orden de presentacion.

Criterios de Aceptacion:

- Se debe poder vizualizar los grupos ordenados por noche y horario.
- Se debe poder visualizar una advertencia si hay un periodo de tiempo sin presentaciones.

Criterios de Prueba de Usuario:

- Probar consultar la planificacion con datos cargados y aparece. (pasa)
- Probar consultar la planificacion donde hay un periodo de tiempo sin presentaciones y no aparece la advertencia. (falla)

#### US03: Registrar Grupos de Folklore

Estimacion: 1 Story Point. Es una historia con poca complejidad, esfuerzo e insertidumbre ya que actua como un tipico formulario para mantener registro de los grupos que se presentaran por noche.

Como reponsable de diagramacion quiero ser capaz de registrar los diferentes grupos de folklore elegidos a participar para tener un historial de los grupos participantes.

Criterios de Aceptacion:

- Se debe poder cargar el nombre del grupo de folklore.
- Se debe poder cargar un numero representante para contacter al grupo.
- Se debe poder cargar un mail representante para contactar al grupo.

Criterios de Prueba de Usuario:

- Probar cargar unicamente el nombre del grupo. (falla)
- Probar cargar el nombre del grupo y un numero telefonico. (pasa)
- Probar cargar el nombre del grupo y un mail. (pasa)
- Probar cargar un numero telefonico con más de 8 digitos. (falla)
- Probar cargar caracteres en el campo de numero telefonico. (falla)
- Probar cargar un mail con el siguiente patron nombre@dominio. (pasa)

<span style="color:yellow"> 

Correcciones de la Historia de Usuario:

- La cátedra modela a los integrantes: un grupo tiene uno o más artistas, un artista puede estar en varios grupos y el nombre del grupo es único. Vos modelaste datos de contacto que el enunciado no menciona.
- Tu argumento del MVP para evitar nombres de banda duplicados corresponde al criterio "nombre único" de la cátedra, y va en esta historia.

</span>

#### US04: Registrar Noches

Estimacion: 1 Story Point. Es la historia canonica, con poca complejidad, insertidumbre y esfuerzo ya que actua como un formulario para registrar la cantidad de noches en las que se realizara el festival y el horario de la misma.

Esta es la user story **canonica** ya que se considera que la complejidad de desarrollar un formulario con tres celdas para completar es minima y las validaciones de las mismas con sencillas de implementar. A su vez hay una insertidumbre y esfuerzo minimo puesto que se pide la generacion de un formulario.

Como responsable de diagramacion quiero definir la hora de inicio de cada noche para poder publicitar al publico en que momento inicia el festival.

Criterios de Aceptacion:

- Se debe poder elegir la cantidad de noches
- Se debe poder elegir la fecha de cada noche
- Se debe poder elegir el horario de inicio de cada noche

Criterio de Prueba de Usuario:

- Probar cargar un numero entero en la celda de cantidad de noches. (pasa)
- Probar cargar una fecha anterior a la actual. (falla)
- Porbar grabar una noche cargando unicamente la cantidad de noches. (falla)
- Porbar grabar una noche cargando sin cargar los horarios de todas las noches. (falla)
- Porbar grabar una noche cargando sin cargar las fechas de todas las noches. (falla)

<span style="color:red">La cátedra registra el festival, no las noches sueltas, y su criterio es que no haya festivales con fechas superpuestas.</span>

#### US05: Registrar Division Estadio

Estimacion: 3 Story Point. Es una historia con cierto esfuerzo ya que la relacion en cascada entre los sectores, filas y butacas requiere su tiempo para desarrollar. De otra forma, la complejidad e insertidumbre es minima.

Como responsable de diagramacion quiero registrar los distintos sectores, filas y butacas para poder diferenciar el precio de la butaca por sector.

Criterios de Aceptacion:

- Se debe poder cargar la cantidad de sectores y su identificacion.
- Se debe poder cargar la cantidad de filas por sector.
- Se debe poder cargar la cantidad de butacas por fila.
- Se debe numerar la butaca automaticamente.

Criterios de Prueba de Usuario:

- Probar cargar una butaca a una fila inexistente. (falla)
- Probar cargar una fila a un sector inexistente. (falla)
- Probar reigstrar un sector sin su identificacion. (falla)
- Probar registrar un sector sin filas. (falla)
- Probar registrar una fila sin butacas. (falla)
- Probar poder modificar el numero de una butaca. (falla)

<span style="color:red">Falta el criterio de que cada sector tenga un color distinto, con su prueba de dos sectores del mismo color (falla). Además, el rol es Responsable de Predio.</span>

#### US06: Vizualizar Division Estadio

Estimacion: 2 Story Point. Es una historia con cierto esfuerzo para desarrollar una ayuda visual sobre la division entre secores, filas y butacas. Como tal al ser simplemente una consulta de datos la complejidad e insertidumbre es minima.

Como vendedor quiero visualizar la division de sectores, filas, la cantidad de butacas y cuales estan disponibles para no vender una butaca a más de una persona.

Criterios de Aceptacion:

- Se debe poder consultar la cantidad de sectores, filas por sector y butacas por filas.
- Se debe poder vizualizar el identificador de los sectores y las butacas.

Criterios de Prueba de Usuario:

- Probar consultar los sectores y no aparece la identificacion. (falla)
- Probar consultar los secotres y no aparecen las filas ni butacas. (falla)
- Probar consutar los sectores y aparecen las filas y butacas. (pasa)

#### US07: Registrar Entrada

Estimacion: 8 Story Point. Es una historia porta cierta insertidumbre al generar en si un codigo de barras que contenga los datos de la entrada. Su esfuerzo es medio ya que el desarrollador debe tener en cuenta todas las restricciones de la historia y en la generacion de la factura siguiendo la ley de facturacion.

Como vendedor quiero registrar la entrada para poder generarle la entrada al fanatico que la pago.

Criterio de Aceptacion:

- Se debe seleccionar la fecha de la noche.
- Se debe seleccionar el tipo de entrada.
- Se debe seleccionar el identificador de butaca.
- Se debe visualizar las butacas libres.
- Se debe calcular el precio de la entrada a partir del tipo de entrada, identificador de butaca y noche.
- Se debe generar el precio automaticamente a partir del tipo de entrada y butaca.
- Se debe generar un codigo de barras unico por entrada el cual tendra el numero de factura.
- Se debe generar la factura por entrada.

Crierio de Prueba de Usuario

- Probar generar la factura y el numero de factura no es unico. (falla)
- probar generar el codigo de barras y no tiene el numero de factura. (falla)
- Probar seleccionar el tipo de entrada, la butaca y la fecha mostrandose automaticamente el precio de la entrada. (pasa)
- Probar seleccionar una butaca ya comprada para esa misma noche. (falla)
- Probar seleccionar una butaca para la noche 2 que en la noche 1 fue comprada y en la noche 2 esta disponible. (pasa)

<span style="color:red">

Correcciones de la Historia de Usuario:

- Te faltan cuatro criterios que pone la cátedra: cobro en efectivo, 6 segundos, control de concurrencia de la butaca y aplicar el descuento cuando corresponde.
- La prueba clave de la cátedra es "vender ubicaciones tomadas por otro punto de venta (falla)". La tuya ("butaca ya comprada") no menciona los puntos de venta.
- La cátedra la divide en Generar e Imprimir. Los 6 segundos van en Imprimir, y la incertidumbre de la historia (media) está en la comunicación con la impresora, algo que vos no contemplaste.
- Vos justificás los 8 SP con la incertidumbre del código de barras. Para la cátedra esa incertidumbre es nula, porque se resuelve con una librería.
- La factura y el número único no están en la solución, pero no está mal que los tengas, porque el enunciado los pide.

</span>

#### US08: Habilitar Venta Anticipada

Estimacion: 2 Story Point. Es una historia con minimo esfuerzo e incertidumbre, siendo la poca complejidad de la restriccion la fecha de vencimiento y el impaco de este procentaje en el precio total de la entrada lo que hace que se le sume un punto más que la canonica.

Como responsable de ventas de entradas quiero poder habilitar la venta anticipada para que quien no tenia planeado ir al festival por el precio de la entrada sea convencido de comprarla.

Criterios de Aceptacion

- Se debe registrar el porcentaje de descuento.
- Se debe seleccionar la fecha de vencimiento del beneficio.

Criterios de Prueba de Usuario

- Probar registrar un procentaje de descuento mayor al 100% (falla)
- Probar registrar caracteres en el procentaje de descuento. (falla)
- Probar seleccionar una fecha de vencimiento despues del inicio de la primera noche. (falla)

#### US09: Anular Entrada

Estimacion: 5 Story Point. En esta historia existe una insertidumbre respecto a como sincronizar los datos que el lector de barras obtiene con la pantalla del vendedor. Fuera de esto la complejidad de la historia radica en la visualizacion de los datos de la entrada y su esfuerzo en la anulacion de la butaca una vez anulada la entrada.

Como vendedor quiero anular una entrada para poder justificar el reintegro de la entrada a un fanatico.

Criterios de Aceptacion:

- Se debe poder cargar el numero de factura.
- Se deben poder mostrar los datos de la entrada: tipo de entrada, butaca, monto total, factura.
- Se debe liberar la butaca luego de generar la anulacion.
- Se debe poder leer el codigo de barras de la entrada y automaticamente aparecen los datos de la misma.

Criterios de Prueba de Usuario:

- Probar anular una entrada hasta diez días antes del inicio del festival. (pasa)
- Probar cargar un numero de factura invalido. (falla)
- Probar leer el codigo de barras de una entrada valida y aparecen los datos de la misma en pantalla. (pasa)
- Probar anular la entrada y automaticamente se libera la butaca de esa noche. (pasa)

#### US10: Registrar Puntos de Venta

Estimacion: 1 Story Point. Es una historia con minima complejidad, insertidumbre y esfuerzo ya que actua como la carga de un formulario.

Como responsable de ventas quiero registrar los puntos de venta para informar al publico donde pueden comprar las entradas.

Criterios de Aceptacion

- Se debe cargar la direccion del punto de venta
- Se debe cargar el horario de antencion del punto de venta.

Criterios de Prueba de Usuario

- Probar cargar dos puntos de venta en la misma direccion. (falla)
- Probar grabar un punto de venta sin horario de atencion. (falla)

<span style="color:yellow">El "para" de la cátedra es vender desde esos puntos, no informar al público. Sus criterios son que el punto de venta pertenece a un centro de venta y que su nombre no se repite dentro de ese centro.</span>

#### US11: Registrar Precio de Entradas

Esimacion: 5 Story Points. Es una historia con insertidumbre ya que no se conoce como se calcula el precio de las entradas a partir de el sector, tipo de entrada y noches elegidas, es un punto a consultar con el Product Owner. Fuera de eso la historia actua como la carga de un formulario y se guarda al funcion que calcula el monto total la cual sera consutlada por otros procesos, por lo que su esfuerzo y complejidad son minimos.

Como respondable de ventas quiero ser capaz de registrar el precio de las butacas, el tipo de entrada y la noche para poder variar el precio dependiendo de los grupos que tocan por noche, el sector de la persona y el tipo de entrada.

Criterios de Aceptacion:

- Se debe registrar el precio por sector.
- Se debe registrar precio por tipo de entrada
- Se debe registrar precio por noche.
- Se debe registrar la funcion para calcular el monto final.

Criterios de Prueba de Usuario

- Probar escribir decimales en el precio por sector. (pasa)
- Probar escribir caracteres en el precio por noche. (falla)
- Probar escrbir la funcion. (pasa)

<span style="color:red">

US11 y US08 frente a Definir precios

- La cátedra resuelve en una sola historia de 2 SP lo que vos repartiste en dos historias que suman 7 SP.
- El precio se define por combinación de noche, sector y tipo de entrada, y el descuento anticipado es un criterio de esa misma historia.
- Sus pruebas son registrar una combinación que ya tiene precio (falla) y registrar precios sin un festival vigente (falla). No hay nada parecido a "registrar la función".
- Para la cátedra la incertidumbre es baja, no alta.

</span>

### Minimum Viable Product

<span style="color:red">La venta anticipada no va en el MVP: la cátedra la excluye explícitamente.</span>

El MVP, explicando el alcance propuesto para el MVP y justificando la inclusión de las user stories al MVP.

Para el MVP buscamos validar si la aplicación aporta valor real a la direccion de cultura de la municipalidad para la organizacion, diagramacion del programa y venta de entradas de los festivales que se organizan.

Se proponen las siguientes user stories para la creacion del MVP:

- US01: Registrar Planificacion de Grupos
- US07: Registrar Entrada
- US08: Habilitar Venta Anticipada
- US09: Anular Entrada

Se reduce el alcance de US01 al registro de los nombres de grupos como un dato cargado en la base de datos a partir de las bandas seleccionadas. De esta forma al ingresar el campo del nombre de entrada se mantiene la validacion de que una banda no se presente dos veces un mismo dia y evitamos errores de usuario al registrar el nombre de una banda de forma diferente, como por ejemplo la banda "The Warning" o "THE W4ARNING".

User Stories que quedan fuera del MVP:

- US02: Visualizar Planificacion de Grupos
- US03: Registrar Grupos de Folklore
- US04: Registrar Noches
- US05: Registrar Division Estadio
- US06: Vizualizar Division Estadio
- US10: Registrar Puntos de Venta
- US11: Registrar Precio de Entradas

<span style="color:red">

Se con la cátedra en que la diagramación entra en el MVP y en que el estadio y los reportes quedan afuera. Las diferencias:

- Sobran US08 y US09. La cátedra excluye explícitamente los descuentos por venta anticipada, y la anulación directamente no aparece en su solución.
- Faltan las historias que permiten vender. La cátedra incluye Registrar Festival, Registrar grupo musical, Definir precios y Registrar punto de venta, que equivalen a tus US04, US03, US11 y US10. Tampoco precarga los grupos en la base: tiene una historia para registrarlos.
- El estadio queda afuera por un supuesto explícito: "único predio con estructura fija". Vos lo dejás afuera sin decir cómo se resuelve
- Estructura: la solución tiene descripción del MVP, lista de lo que no incluye, criterio de justificación y las US agrupadas por rol. En la descripción achica el alcance simplificando reglas dentro de las historias (solo efectivo, sin descuentos, un tipo de entrada general) en lugar de sacar historias enteras. Tu recorte de US01 va en esa línea, pero es el único que hiciste.

</span>