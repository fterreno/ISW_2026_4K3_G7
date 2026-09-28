# User Story y Estimaciones: Sistema GPS

## Consigna

Aplicar los conceptos teóricos desarrollados en clase sobre user stories y estimaciones ágiles. Para ello los estudiantes realizarán preguntas con el objetivo de acordar juntos el alcance del proyecto, y determinar:

- Los roles principales
- Las user stories completas.
- La estimación de cada user, identificando la canónica

## Domino

Objetivo: Desarrollar un sistema que permite a un conductor (entre otras funcionalidades), buscar un destino, obteniendo distintas alternativas para llegar hasta el punto marcado desde la ubicación actual.

A continuación, se transcribe parte de la entrevista realizada al experto en el dominio:

Product Owner (PO): ¿Cómo se puede buscar un destino deseado?

Experto en el Dominio (ED): La búsqueda puede realizarse en todos los mapas de las distintas ciudades, que serán cargados en el dispositivo, o bien en el mapa de una ciudad determinada.

PO: ¿Qué datos del destino son necesarios?

ED: Si desea buscar un destino por dirección, debería indicar primero el país y la ciudad, y luego ingresar el nombre de la calle y número.

PO: ¿Qué pasa si desconozco alguno de estos datos, ¿Puedo buscar el destino por otros parámetros?

ED: Si, también debe existir la posibilidad de buscar un destino mediante sus coordenadas, o indicando un cruce de calles. Las coordenadas se representan con tres números que indican longitud y tres números que indican latitud. Cada número representa los grados, minutos y segundos respectivamente. Además se debe indicar la orientación para la latitud (norte, sur) y para la longitud (este, oeste), de cada coordenada.

PO: ¿Me darías un ejemplo?

ED: Claro, por ejemplo 24° 45´ 45´´ Longitud Este – 45° 34´ 23´´ Latitud Sur.

PO: Gracias, está claro. ¿Mencionaste algo del cruce de calles?

ED: Sí, la búsqueda de un destino podría ser realizada por cruce de calles, primero debería ingresarse el nombre del país y de la ciudad de destino, y luego el nombre de las dos calles.

PO: Entendidos los parámetros de búsqueda, ¿Cómo se espera que se indique el camino?

ED: Se debe poder visualizar en el mapa el camino propuesto para dirigirse desde el punto actual (origen) hasta el destino señalado.

PO: Respecto del camino que debe visualizarse, ¿Alguna condición para las distintas alternativas?

ED: Cierto, antes de la visualización en el mapa, debería poder seleccionarse la ruta deseada: el camino más rápido, el camino más corto, el camino por caminos alternativos, el camino evitando peajes o el camino evitando controles. Además, una vez realizada la búsqueda, se debe permitir al conductor marcarla como favorita, ingresando si desea un nombre descriptivo, para que en caso de volver a necesitarla, evitar ingresar todos los datos nuevamente.

PO: ¿Para cualquier tipo de búsqueda?

ED: Así es, una vez encontrado el destino, se debe poder guardar el mismo en Favoritos, ya sea una dirección, un cruce de calles o coordenadas. Cuando el conductor desee dirigirse a un destino guardado con anterioridad, sólo debe consultar la opción Favoritos y buscar el destino deseado. Los destinos en Favoritos deberían visualizarse por orden alfabético según su nombre, y también deberían poder filtrarse deletreando el mismo. Para éste último se desea que a medida que el conductor ingrese el nombre, el sistema vaya mostrando las opciones que contiene con los dígitos ingresados, como cuando se utiliza un buscador web.

PO: ¿Alguna otra información al respecto?

ED: Sí, que el sistema muestre al Conductor la velocidad promedio durante el viaje y la hora de llegada aproximada, actualizando ésta última en función de la velocidad. Y que te permita buscar un destino, a partir de las últimas búsquedas realizadas, por lo menos las últimas 5.

---

## Desarrollo

### Roles Principales

- Conductor
- Responsable del sistema

<span style="color:red">La solución no tiene una sección de roles, pero todas sus historias son del Conductor. "Responsable del sistema" no aparece en ninguna de tus historias, así que sobra.</span>

### User Stories

Desarrollar un sistema que permite a un conductor (entre otras funcionalidades), buscar un destino,
obteniendo distintas alternativas para llegar hasta el punto marcado desde la ubicación actual.

    **como** <rol> **quiero** <feature> **para** <valor de negocio>
    Para que una user story sea canonica se debe tener en cuenta su complejidad, con menos insertidumbre y que no conlleve mucho esfuerzo.
    La estimacion se hace con la secuencia de Fibonacci.

<span style="color:red">

Correcciones de las historias:

- La historia US04: Visualizar Busqueda se podria dividir en dos historias, una de favoritos y otra de generar mapa interactivo.
- Se parecen sobreescribir la historia 1, 2 y 3 con la 6.
- Buscar Destino en Favoritos (2 SP). El destino se elige de una lista de guardados, y se prueba con un destino guardado (pasa) y uno no guardado (falla).
- Filtrar destino en favoritos: el filtro que se aplica mientras el conductor escribe, como en un buscador web.
- Ojo con el orden de favoritos: la cátedra los lista del más reciente al menos reciente, pero la entrevista dice orden alfabético por nombre. Seguí el enunciado o consultalo con el docente.

</span>


#### US01: Buscar Destino por Coordenada

Estimacion: 5 Story Points. La complejidad y esfuerzo de la historia es minima teniendo que unicamente permitir la carga de valores del formulario. La insertidumbre por otro lado es alta, ya que el equipo nunca ha trabajado con cordenadas y se desconoce como se pueden estas mismas al desarrollo de la funcionalidad.

Como conductor quiero buscar un destino por coordenada para conocer las distintas alternativas para llegar al destino.

Criterios de Aceptacion:

- Se deben indicar los grados, minutos y segundos.
- Se debe seleccionar la latitud
- Se debe seleccionar la longitud

Criterio de Prueba de Usuario

- Probar cargar numeros decimales en el campo de grados, minutos y segundos. (pasa)
- Probar seleccionar sur en latitud. (pasa)
- Probar seleccionar sur en longitud. (falla)

<span style="color:yellow">

- La cátedra tiene como criterio indicar la orientación (norte, sur, este, oeste). Tus criterios dicen "seleccionar la latitud/longitud" y la orientación aparece solo en las pruebas.
- Te faltan las pruebas de resultado: coordenada existente (pasa), coordenada inexistente (falla) y coordenada sin orientación (falla).

</span>

#### US02: Buscar Destino por Cruce de Calles

Estimacion: 3 Story Points. La complejidad e insertidumbre es minima, pero el esfuerzo es grande ya que se necesita formular una logica que permita encontrar la interseccion entre dos calles.

Como conductor quiero buscar un destino a traves de cruce de calles para conocer las distintas alternativas para llegar al destino.

Criterios de Aceptacion:

- Se debe selecionar el nombre del pais destino.
- Se debe selecionar el nombre de la ciudad destino a partir del nombre del pais destino.
- Se debe selecionar el nombre de las dos calles destino a partir de la ciudad destino.

Criterios de Prueba de Usuario:

- Probar seleccionar un pais destino y que automaticamente te aparezcan las ciudades del pais destino. (pasa)
- Probar seleccionar una ciudad destino y que automaticamente te aparezcan los nombres de las calles destino. (pasa)
- Probar seleccionar una calle destino. (falla)

<span style="color:red">

- Te falta la regla principal: la cátedra valida que las dos calles no sean paralelas y lo prueba con dos calles paralelas (falla).

</span>

<span style="color:yellow">

- El orden país → ciudad → calle coincide con la cátedra.
- La cátedra verifica que las calles existan y prueba con país, ciudad y calles inexistentes. Tus pruebas miden cómo se comportan las listas, no si se encuentra el destino.
- "Probar seleccionar una calle destino (falla)" es ambiguo. Si querés decir que falla al elegir una sola calle, escribilo así.

</span>

#### US03: Buscar Destino por Direccion

Estimacion: 2 Story Points. Con complejidad e insertidumbre minimas, el esfuerzo radica en encontrar la direccion destino y generar una logica para el desarrollo del mismo.

Como conductor quiero buscar un destino a traves de una direccion para conocer las distintas alternativas para llegar al destino.

Criterios de Aceptacion:

- Se debe selecionar el nombre del pais destino.
- Se debe selecionar el nombre de la ciudad destino a partir del nombre del pais destino.
- Se debe seleccionar el nombre de la calle destino a partir de la ciudad destino.
- Se debe cargar el numero.

Criterios de Prueba de Usuario

- Probar seleccionar primero la calle. (falla)
- Probar seleccionar el pais y que automaticamente aparezcan el listado de ciudades del pais. (pasa)
- Probar habiendo seleccionado calle, ciudad y pais, eliminar pais y se eliminan los datos en cascada. (pasa)
- Probar seleccionar la ciudad y automaticamente aparece un listado de calles. (pasa)

<span style="color:yellow">

- Te faltan los criterios del número de calle: la cátedra lo define como entero positivo de hasta 5 caracteres y verifica que la calle exista.
- También faltan las pruebas de calle inexistente y altura inexistente (ambas fallan).
- La prueba del borrado en cascada es de interfaz. La cátedra no tiene pruebas de ese tipo.

</span>

#### US04: Visualizar Busqueda

Estimacion: 8 Story Points. Es de alto esfuerzo ya que se pide la visualizacion de un mapa, resaltando el camino del viaje dependiendo del parametro elegido, teniedo que desarrollar una logica de calculo de ruta diferente por cada parametro presente. La insertidumbre radica en el uso del gps, algo que el equipo no esta familizarizado y no sabe como manejar. La complejidad es minima.

Como conductor quiero visualizar el mapa de la ciudad para saber por donde tengo que ir en el viaje.

Criterios de Aceptacion:

- Se debe seleccionar los tipos de viajes: el camino más rápido, el camino más corto, el camino por caminos alternativos, el camino evitando peajes o el camino evitando controles.
- Se debe poder etiquetar como favoritos la busqueda realizada.
- Se debe poder cargar un nombre descriptivo a la bsuqueda etiquetada como favorito.
- Se debe visualizar en un mapa el camino desde donde el conductor se encuentra hasta el destino.

Criterios de Prueba de Usuario:

- Probar realizar una busqueda con tipo de "camino evitando peajes" y el treyecto no pasa por ningun peaje. (pasa)
- Probar etiquetar como favoritos una busqueda con nombre "Casa". (pasa)
- Probar realizar una busqueda con tipo de "camino evitando controles" y el treyecto pasa por controles. (falla)
- Probar seleccionar más de un tipo de viaje. (falla)

<span style="color:yellow">

- Juntaste dos historias que la cátedra separa: Generar Mapa con Camino (5) y Guardar Destino en Favoritos (1).
- El "quiero" habla del mapa de la ciudad, pero lo que se visualiza es el camino hasta el destino.
- La cátedra aclara que "evitando peajes" aplica a destinos fuera de la ciudad de origen, y prueba qué pasa sin conexión (falla). Vos no contemplaste la conexión.
- En favoritos, la cátedra define que el nombre es opcional y lo prueba guardando sin nombre (pasa). Tu criterio no aclara si el nombre es obligatorio.

</span>

#### US05: Visualizar Datos de Viaje

Estimacion: 1 Story Points. La complejidad es minima, unicamente radicando en el calculo de la velocidad respecto al tiempo y distancia, con esfuerzo e insertidumbre minima.

Esta es la historia canonica.

Como conductor quiero conocer la velocidad promedio y la hora de llegada a destino para luego saber cuanto tiempo y a que velocidad tengo que ir para llegar a un destino proximamente.

Criterios de Aceptacion:

- Se debe vizualizar la velocidad promedio en km/hs del viaje.
- Se debe visualizar el tiempo promedio de la duracion del viaje en hh:mm.

<span style="color:yellow">

- La cátedra lo divide en dos historias: una para la velocidad promedio y otra para la hora de llegada.
- El enunciado pide la hora de llegada aproximada, actualizada según la velocidad. Vos pusiste la duración del viaje y no mencionás la actualización.
- El "para" habla de un viaje futuro, pero el valor de la historia está en el viaje actual.

</span>

#### US06: Buscar Destino

Estimacion: 1 Story Points. La complejidad y esfuerzo son minimos con una insertidumbre nula. La complejidad radica en mostrar automaticamente las busquedas realizadas y el esfuerzo en realizar el formulario para realizar la busqueda. 

Como conductor quiero ser capaz de buscar un destino para poder saber como llegar desde donde estoy hasta el punto destino.

Criterios de Aceptacion:

- Se debe mostrar automaticamente en la los ultimas 5 busquedas realizadas.
- Se debe seleccionar el parametro de busqueda de destino: coordenada, direccion y cruce de calles.

Criterios de Prueba de Usuario

- Probar realizar una busqueda y que aparezcan las ultimas cinco busquedas realizadas. (pasa)
- Probar seleccionar el parametro de coordenada y te carga el formulario de coordenadas. (pasa)
- Probar seleccionar el parametro de direccion y te carga el formulario de direccion. (pasa)
- Probar seleccionar el parametro de cruce de calles y te carga el formulario de cruce de calles. (pasa)
- Probar seleccionar la penultima busqueda realizada y carga los parametros de busqueda. (pasa)

<span style="color:yellow">

Mezcla dos cosas: elegir el tipo de búsqueda y mostrar las últimas búsquedas.
La cátedra no tiene una historia para elegir el tipo de búsqueda, porque eso ya forma parte de las tres búsquedas. Tu US06 se superpone con US01, US02 y US03.
Las últimas búsquedas son una historia propia en la cátedra. El enunciado pide "por lo menos las últimas 5".

</span>

### Minimum Viable Product

Se considera que las siguietes historias de usuario incluyen al MVP para lograr el objetivo de presentar un sistema que permite buscar un destino para consultar el camino al mismo.

- US01: Buscar Destino por Coordenada
- US02: Buscar Destino por Cruce de Calles
- US03: Buscar Destino por Direccion
- US04: Visualizar Busqueda
- US06: Buscar Destino

Para la historia de usuario 04 Visualizar Busqueda se restrige la historia a simplemente la busqueda del camino más corto a llegar al destino. Para la historia de usuario 06: Buscar Destino se restrige el alcance a unicamente realizar la busqueda, descartando la funcionalidad de "mostrar automaticamente las ultimas 5 busquedas realizadas".
