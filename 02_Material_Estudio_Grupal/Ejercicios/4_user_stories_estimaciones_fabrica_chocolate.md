# Caso Practico 4: Carlos y la Fabrica de Chocolate

## Consigna

Aplicar los conceptos teóricos desarrollados en clase sobre user stories y estimaciones ágiles. Para
ello los estudiantes realizarán preguntas con el objetivo de acordar juntos el alcance del
proyecto, y determinar:

- Los roles principales
- Las user stories completas.
- La estimación de cada user, identificando la canónica

## Domino

“El Buen Chocolate Argentino” es una empresa que se dedica a la fabricación masiva de chocolates en el sur de la Argentina. Carlos, su actual gerente de producción, ha decidido incorporar tecnología al proceso de fabricación con el objetivo de revolucionar la manera de hacer chocolate y hacerla más eficiente. Para ello desean desarrollar una aplicación iOS que dará soporte a las actividades más importantes del proceso de fabricación, y cuyos resultados serán enviados a una base de datos en la nube para que la información esté disponible y online para su consulta. Esto permitirá mayor fluidez y rapidez en la toma de decisiones de la fábrica.

Para producir chocolate es necesario contar con el ingrediente más importante: el cacao. Si bien el 70% de la producción mundial de cacao viene de África del Oeste, los más preciados y principales proveedores de la fábrica se encuentran en Ecuador y Venezuela. Las espinas se desgranan, partiéndolas por la mitad con ayuda de un machete, y luego los granos son enviados a los diversos campos que posee la fábrica. Éstos pasan por un proceso de fermentación en cajas o entre hojas de bananero cuyo objetivo es evitar que germine, eliminar la pulpa viscosa e iniciar el desarrollo del aroma. Este proceso dura entre 4 y 7 días y es realizado por agricultores especializados. Finalizada la fermentación y segmentación son enfriados y almacenados en sacos para ser transportados a las plantas de producción. Una vez llegadas a la fábrica, el proceso se divide en dos partes:

Tratamiento del Cacao

Los granos pasan por un proceso de limpieza y son triturados partiéndose en trocitos más pequeños. Finalmente pasarán a ser tostados en el proceso de torrefacción. La torrefacción es un delicado proceso que impacta el color, el aroma y el sabor del producto final, pues es en este proceso donde el grano desarrolla más de 400 aromas. Los granos se tuestan a una temperatura que oscila entre 120 y 150 grados centígrados durante un tiempo variable que puede llegar a 25 minutos con un mínimo de 10 minutos. La temperatura y tiempo de tostado son las variables claves a controlar para obtener un sabor específico del chocolate. El Responsable de Tratamiento podrá controlar la máquina de torrefacción desde su teléfono para regular la temperatura del proceso, cambiar la intensidad del sabor (suave, medio, intenso o muy intenso) y el tiempo de tostado. Una vez tostados, los granos son molidos nuevamente a mayor temperatura para obtener una masa líquida conocida como “pasta de cacao”. Luego sigue el mezclado; en él se vierten diversos ingredientes en función del tipo de chocolate:

- Chocolate negro: pasta de cacao, manteca de cacao, azúcar.
- Chocolate con leche: pasta de cacao, manteca de cacao, azúcar y leche.
- Chocolate blanco: manteca de cacao, azúcar y leche.

Las máquinas mezcladoras y sus correspondientes vertedores de ingredientes son controladas también mediante la aplicación, permitiendo así al Responsable de Tratamiento seleccionar el tipo de chocolate, sus ingredientes con sus respectivas cantidades indicadas en Kg o Litros según corresponda y regular la temperatura de la máquina, indicando los grados (entre 50 y 80). Luego viene la refinación, en donde se hace pasar la mezcla por unas máquinas con cinco rodillos. En ellos va avanzando la mezcla a la vez que disminuye el tamaño de las partículas hasta obtener un polvo fino y de calidad. El Responsable de Tratamiento podrá desde su aplicación regular la intensidad de la fuerza con la que actúan los rodillos (media, alta, muy alta) y, eventualmente, cambiar la cantidad de rodillos que se utilizarán que puede variar entre 2 rodillos a 5. En este mismo proceso también podrá determinar el tiempo de refinación en minutos. Para que la mezcla alcance toda su finura y untuosidad y acabe de desarrollar todos los aromas, el cacao se somete a las tareas de conchado, proceso en que la mezcla será amasada durante horas o incluso durante días, y donde perderá parte de los aromas amargos y ácidos, desarrollando todos los aromas más preciados en el chocolate. Durante el conchado se añade manteca de cacao y lecitina con el fin de incrementar la fluidez. También se incorpora aroma natural de vainilla que permitirá darle el gusto definitivo deseado. El Responsable de Tratamiento tendrá la posibilidad de iniciar desde la aplicación las tareas de conchado indicando el tiempo en horas, los ingredientes y sus cantidades en Kg, el nivel de acidez (bajo, medio, alto) y la intensidad también con 3 alternativas graduadas. Además, la máquina cuenta con un sensor que deberá notificar a la aplicación mediante PUSH cuando la mezcla haya obtenido el nivel de acidez y fluidez deseado, donde la acidez se indica al iniciar el conchado y la fluidez se encuentra parametrizada en el sensor.

Elaboración del Chocolate

Luego del tratamiento comienza la elaboración del chocolate. Lo primero que hay que hacer es el templado o atemperado, donde se realiza un enfriamiento controlado del chocolate para permitir una perfecta cristalización de la manteca de cacao. Es otro proceso esencial para que el chocolate tenga aspecto y textura adecuados. El Responsable de Elaboración le indicará a la máquina cuando iniciar el enfriamiento, el tiempo de este en minutos, seleccionar aspecto y textura deseados, y deberá emitir una alerta en caso de que la textura haya superado el nivel indicado. Si la máquina está a una temperatura superior a la indicada deberá notificarlo para que el Responsable de Elaboración esté en conocimiento y modifique los parámetros manualmente. En el caso de querer fabricar chocolate con otros ingredientes adicionales como maníes, pasas de uva, pistachos, se debe introducir a una máquina la mezcla junto con los ingredientes en los vertedores que serán distribuidos según la cantidad a elaborar. El Responsable de Elaboración le indicará a la máquina a través de la aplicación qué proporción de mezcla llevará cada ingrediente y cuánta cantidad de ese ingrediente incorporar. El proceso dura por defecto 30 minutos y el resultado final de la mezcla es depositada en una máquina de moldeo, en donde el Responsable de Elaboración deberá recibir en su aplicación el estado final de cada mezcla: color, sabor, olor, temperatura, textura, acidez, tipo de chocolate e ingredientes adicionales. Finalmente, durante el moldeo y embalaje se da al chocolate la forma deseada vertiéndolo en moldes desde la máquina. El Responsable de Elaboración indicará en la aplicación cuánta cantidad de cada molde debe ser fabricado y cuánta cantidad de mezcla por molde introducir. El nivel de temperatura de la máquina deberá ser indicado ya que diferentes tipos de moldes (por su fabricación o material), soportan diferentes temperaturas. Finalmente se hace pasar a todos los moldes por un tubo de enfriado en donde por 120 minutos los chocolates adquieren la temperatura necesaria para ser embalados. El resultado del proceso debe ser notificado al Responsable de Elaboración indicando la cantidad de moldes y unidades disponibles por cada uno. Finalmente se realiza el embalaje y se cargan los chocolates en transportes preparados para mantener la temperatura entre 15 y 17 grados, finalizando con la distribución de los mismos a comercios y supermercados de todo el país.

---

## Desarrollo

## Roles Principales

- Gerente de Produccion ??
- Responsable de Tratamiento
- Responsable de Elaboracion

## User Story

### US01: Registrar Torrefaccion

estimacion: no sabemos como comunicarnos con la maquina para pasarle los poarametros a la maquina

Como responsable de tratamiento quiero controlar la intensidad en la torrefaccion a producir para que el grano de cafe desarrolle el sabor especifico del chocolate.

Criterios de Aceptacion:

- Se debe seleccionar la intensidad del sabor.

Criterios de Prueba de Usuario:

- Probar seleccionar la intensidad del sabor y automaticamente te aparecen las opciones de: suave, medio, intenso o muy intenso. (pasa).
- Probar registrar una intensidad de sabor. (falla)
- Probar seleccionar una intensidad de sabor y automaticamente te aparecen el tiempo que tarda el proceso. (pasa)
- Probar seleccionar una intensidad de sabor y automaticamente te aparecen temperatura del proceso. (pasa)

### US02: Registrar Intensidad de Sabor

Como genernte de produccion quiero estandarizar la intensidad del sabor en mis productos para que la marca de mis productos sea homogenea.

Criterios de Aceptacion:

- Se debe cargar el nombre de la intensidad de sabor.
- Se debe registrar la temperatura del proceso entre 120 y 150 grados
- Se debe registrar el tiempo de tostado entre 10 a 25 minutos

Crierios de Prueba de Usuario:

- Probar grabar un registro que tenga nombre, temperatura y tiempo. (pasa)
- Probar grabar un registro que tenga nombre y tiempo. (falla)
- Probar grabar un registro que tenga nombre y temperatura. (falla)
- Probar grabar un registro que tenga tiempo y temperatura. (falla)
- Probar registar una temepratura de 200 grados. (falla)
- Probar registrar caracteres en el campo de temperatura. (falla)
- Probar registrar el tiempo de tostado de 20 minutos. (pasa)
- Probar registrar el tiempo de tostado con un formato de hh:mm:ss. (pasa)

### US03: Registar Tipos de Chocolate

Como generte de produccion quiero estandarizar los diferentes tipos de chocolate para que mis clientes sepan que esperar del chocolate cuando ven el nombre en la etiqueta.

Criterios de Aceptacion:

- Se debe cargar el nombre de la mezcla especifica.
- Se debe seleccionar que ingredientes se incluyen en la mezcla especifica.
- Se debe cargar la cantidad del ingrediente especificado en gramos o litros.
- Se debe cargar la temperatura en grados para la mezcla especifica.

Criterios de Prueba de Usuario:

- Probar cargar la temperatura en Farenheith. (falla)
- Probar cargar la cantidad de ingredientes en kilogramos. (falla)
- Probar cargar un caracter en la cantidad del ingrediente especificado. (falla)
- Probar grabar nombre, temperatura y los ingredientes donde cada ingrediente tiene especificada la cantidad. (pasa)
- Probar seleccionar un tipo de chocolate donde no hay stock de un ingrediente. (falla)

### US04: Registrar Stock Ingredientes de Mezcla

Como generte de produccion quiero tener un registro de que ingredientes tengo en stock para asi no produccir un tipo de chocolate donde tengo ingredientes faltantes.

Crierios de Aceptacion:

- Se debe seleccionar el nombre del ingrediente.
- Se debe generar un numero identificador por lote ingresado. ??
- Se debe cargar la cantidad del lote ingresado en litros o gramos.
- Se debe cargar la fecha de vencimiento del lote ingresado.

Criterios de Pruebas de Usuario:

- Probar cargar el nombre del ingrediete sin cantidad disponible y el registro se graba con cantidad disponible cero. (pasa)
- Probar cargar la cantidad disponible con caracteres. (falla)
- Probar modificar la cantidad disponible de un registro ya creado. (pasa)
- Probar modificar el numero identificador del lote. (falla)

### US05: Registrar Ingrediente de Mezcla

Como gerente de produccion quiero tener un registro de que ingredientes son necesarios para saber que tipos de chocolate puedo producir.

Criterios de Aceptacion:

- Se debe cargar el nombre del ingrediente
- Se debe seleccionar la unidad del ingrediente.

Criterios de Prueba de Usuario:

- Probar seleccionar litros o gramos. (pasa)
- Probar registrar unicamente el nombre del ingrediente. (falla)

### US06: Manipular Refinacion

estimacion: no sabemos como comunicarnos con la maquina para pasarle los poarametros

Como responsable de tratamiento quiero regular la fuerza de la maquina de rodillos y la cantidad del mismo para evitar tener que manipular la maquina manualmente. 

Criterios de Aceptacion:

- Se debe seleccionar la fuerza del rodillo.
- Se debe cargar la cantidad de rodillos en un intervalo de 2 a 5 incluido.
- Se debe cargra el tiempo de refinacion.

Criterios de Aceptacion:

- Probar seleccionar la fuerza de rodillo y aparecen las opciones: media, alta y muy alta. (pasa)
- Probar cargar la cantidad de rodillos de 2,5. (falla)
- Probar cambiar la cantidad de rodillo de 2 a 3 y la maquina agrega un rodillo al proceso de refinacion. (pasa)
- Probar cargar el tiempo en minutos. (pasa)

### US07: Registrar Conchado

Estimacion: Media insertidumbre ya no se conoce que es una alternativa graduada. no sabemos como comunicarnos con la maquina para pasarle los poarametros

Como responsable de tratamiento quiero indicar el periodo de conchado, con sus ingredientes y nivel de acides para que se desarrollen adecuadamente los aromas del chocolate.

Criterio de Aceptacion:

- Se debe generar automaticamente un identificador del conchado.
- Se debe seleccionar los ingredientes.
- Se debe cargar la cantidad de los ingredientes en kilogramos.
- Se debe cargar el tiempo de conchado en horas.
- Se debe seleccionar el nivel de acidez.
- Se debe seleccionar una de las tres alternativas graduadas.

Criterio de Prueba de Usuario:

- Probar modificar el indentificador del conchado. (falla)
- Probar selecionar un ingrediente y automaticamente te aparece el listado. (pasa)
- Probar cargar la cantidad del ingrediente seleccionado en kilogramos. (pasa)
- Probar cargar el timepo en hh:mm. (pasa)
- Probar seleccionar el nivel de acidez y automaticamente aparece: bajo, mediano, alto. (pasa)
- Probar grabar sin seleccionar una alternativa graduada. (falla)

### US08: Notificacion Conchado

Estimacion: insertidumbre alta, no se sabe como hacer que la maquina realice la notificacion. A su vez no se sabe como acceder a la fluidez del sensor ni que unidades puede poseer.

Como responsable de tratamiento quiero tener una notificacion cuando la mezcla alcanza el nivel de acidez deseado para que este mismo no se pase de acidez.

Criterio de Aceptacion

- Se debe vizualizar los datos del conchado.
- Se debe vizualizar la maquina de la que proviene la notificacion.
- Se debe vizualizar el nivel de acidez y fluidez actual.

Criterios de Prueba de Usuario:

- Probar registrar un conchado con nivel de acidez bajo y en la notificacion aparece nivel de acidez bajo. (pasa)
- Probar registrar la fluidez en 5 y en la notificacion la fluidez actual aparece en 7. (falla)

### US09: Registrar Templado

Estimacion: Insertidumbre baja: no se conocen los aspectos o texturas que se pueden seleccionar. no sabemos como comunicarnos con la maquina para pasarle los poarametros

Como responsable de elaboracion quiero tener control del tiempo de enfriamente para que el chocolate tenga aspecto y textura adecuados.

Criterios de Aceptacion:

- Se debe generar automaticamente un identificador del registro.
- Se debe cargar la hora de inicio de enfriamiento.
- Se debe seleccionar el aspecto deseado.
- Se debe seleccionar la textura deseada.
- Se debe cargar la temperatura en que debe estar la mezcla.
- Se debe cargar los ingredientes adicionales.
- Se debe cargar la cantidad por ingrediente adicional.
- Se debe cargar el tiempo del proceso en hh:mm.

Criterios de Prueba de Usuario:

- Probar modificar el registro. (falla)
- Probar cargar 15:00 como la hora de inicio. (pasa)
- Probar cargar el aspecto deseado y aparecen listados los aspectos deseados a elegir. (pasa)
- Probar cargar la textura deseada y aparecen listados las texturas deseadas a elegir. (pasa)
- Probar cargar la temperatrua en celcius. (pasa)
- Probar grabar el registro sin ingedientes adicionales. (pasa)
- Probar garbar el registro con ingredientes adicionales pero sin su cantidad especificada. (falla)
- Probar modificar el tiempo de duracion del proceso. (pasa)
- Probar cargar un registro y el tiempo del proceso aparece automaticamente de 30 minutos. (pasa)

### US10: Notificacion Templado

Como responsable de elaboracion quiero ser alertado cuando la temperatura supera la indicada para poder modificar los parametros manualmente.

Criterio de Aceptacion:

- Se debe notificar cuando la temperatura actual supera la temperatura cargada.
- Se debe visualizar los datos del templado que se notifica y la maquina que envia la notificacion.
- Se debe visualizar la temperatura actual en contraposicion con la temperatura ingresada.

Criterio de Pruebas de Usuario

- Probar registrar un templado que termine superando la temepratura indicada. (pasa)
- Probar enviar una notificacion y que aparezcan los datos del templado y se visualice la temperatura practica con la teorica. (pasa)

### US11: Notificar Estado Final

Como responsable de elaboracion quiero ser notificado cuando termine el proceso de templado para conocer el estado final de la mezcla y los datos de la misma.

Criterios de Aceptacion

- Se debe visualizar en la notificacion el  color, sabor, olor, temperatura, textura, acidez, tipo de chocolate e ingredientes adicionales.

Criterio de Prubea de Usuario:

- Probar modificar los datos de la mezcla. (falla)
- Probar eliminar los datos de la mezcla. (falla)

### US12: Registrar Moldeo

Como responsable de elaboracion quiero indicar la cantidad de moldes que deseo tener para poder generar la cantidad adecuada que se nos pide.

Criterios de Aceptacion:



### US13: Registrar Tipos de Moldeo

### US14: Generar Reporte Embalaje

## Minimum Viable Product

