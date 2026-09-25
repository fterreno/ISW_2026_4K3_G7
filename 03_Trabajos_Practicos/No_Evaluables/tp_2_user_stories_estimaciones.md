# TP2: REQUERIMIENTOS ÁGILES – User Stories y Estimaciones

Identificar y escribir las US identificadas en el Dominio presentado para el práctico

Salidas

- Identificación de los roles principales
- El MVP explicando el alcance propuesto y justificando la inclusión de las User Stories seleccionadas y el porqué de aquellas excluidas en el mismo
- US identificadas con sus tarjetas completas
- User Story canónica
- User Stories estimadas

## Dominio

Los dueños del bioparque “EcoHarmony Park” están evaluando el desarrollo de una aplicación móvil (Android, iOs) ya que la cantidad de visitantes anuales aumentaron significativamente al igual que los avances tecnológicos. La misma tiene como objetivo mejorar la experiencia de los visitantes al proporcionar información útil y enriquecedora sobre las exhibiciones, los horarios de alimentación de los animales, los senderos para caminar y otros aspectos del parque como la autogestión al momento de realizar la compra de entradas.

Hemos tenido el privilegio de entablar una conversación con Miguel Rodríguez, uno de los propietarios de
EcoHarmony Park, y a continuación, compartimos los detalles de la interacción:

El Doce: ¡Hola! Estoy aquí en el hermoso bioparque "EcoHarmony Park" con el Sr. Rodríguez, para hablar sobre una emocionante novedad: ¡una nueva aplicación móvil que mejorará la experiencia de los visitantes aquí en el parque! ¿Me podrías contar brevemente en qué consiste la aplicación?

Miguel: ¡Hola! Gracias por tomarte el tiempo para hablar conmigo. Estoy encantado de compartir más detalles sobre la idea de nuestra aplicación. En primer lugar, ofrecerá a los visitantes mapas interactivos que les ayudarán a explorar el parque de manera más eficiente. Asimismo, proporcionará información detallada sobre cada exhibición y horario de alimentación de cada especie que cuidamos. También se podrá autogestionar la compra de entradas al parque, pudiendo realizar directamente el pago a través de la pasarela de Mercado Pago, lo que permitirá agilizar el ingreso. Por último, los visitantes pueden inscribirse a las diferentes actividades diarias que posee el parque.

El Doce: Wow! Que interesante ¿Podrías explicarme cómo puede un visitante acceder a los horarios de alimentación a través de la aplicación?

Miguel: ¡Claro! Una vez que descarguen la aplicación y la abran, encontrarán una sección dedicada a "Horarios de Alimentación disponibles". Cada horario estará detallado de manera clara, indicando la especie, nombre del animal, edad, hora programada, sector del parque (terrestres, acuáticos o aéreos) y cuidador encargado (nombre y apellido). Por otra parte, aquellos que estén próximos a comenzar (faltando una hora) los mostraremos con un mensaje que diga: ¡Apúrate que ya comienza! Es importante considerar que los horarios se mostrarán en orden, comenzando con los más próximos a la fecha actual y extendiéndose hasta una semana en el futuro. Para que sea más amigable la interfaz pensamos en proporcionar la posibilidad de filtrar por la fecha en la que el visitante estará en el parque y que se visualicen únicamente los horarios correspondientes a la misma. Además, en una versión posterior, los visitantes podrán configurar notificaciones para recibir recordatorios de los horarios de alimentación que deseen seguir de cerca.

El Doce: ¡Eso suena muy útil! ¡Al igual que el mapa interactivo! ¿Podrías comentarme cuáles serán los elementos y características del parque que estarán disponibles para visualizar en él? ¿Qué acciones podrán llevar a cabo los visitantes a través de esta herramienta?

Miguel: Este mapa ofrece una vista panorámica de todo el parque, dividido en sectores diferenciados por colores.Asimismo, el mapa contiene íconos informativos: “Inodoro” para identificar los baños distribuidos en el parque, una “Bolsa” para indicar los puntos de venta, y un “Micrófono” para el show especial del día. Los visitantes pueden hacer click en este último icono para obtener el nombre del show y su horario, en caso de que haya un show programado. En una futura mejora pensamos incluir en este mapa la ubicación del visitante en tiempo real.

El Doce: Para alguien como yo, con un sentido de la orientación no muy desarrollado, suena como una herramienta imprescindible, ¡jaja! ¿Hay otros aspectos del parque que también planean ofrecer a través de la aplicación? ¿Habías mencionado la inscripción a las actividades, no es cierto?

Miguel: Si! me estaba olvidando de comentarlo. El parque ofrece la posibilidad de realizar actividades de una hora sumamente enriquecedoras para los visitantes, entre las que se encuentran “Tirolesa”, “Safari”, “Palestra” y “Jardinería”. Para poder realizar la inscripción deben seleccionar del conjunto de actividades la que desean realizar, eligiendo en primer lugar el horario y completando luego los datos del visitante: nombre, DNI, edad y talla de vestimenta si la actividad lo demanda. Finalmente, para concluir el proceso de inscripción, pedimos a los visitantes que acepten los términos y condiciones específicos de la actividad en la que participarán, enviando el resumen de la inscripción con un QR al mail del visitante. Nos interesa gestionar la inscripción de las actividades porque tienen cupos limitados y es muy útil para planificarlas con anterioridad según los inscriptos que tengamos.

El Doce: Para finalizar esta pequeña entrevista, ¿Podrías explicarme el proceso de compra de entradas a través de la app?

Miguel: !Pero claro! Para realizar la compra de entradas el visitante debe registrarse en la aplicación, ingresando un mail y una contraseña. A continuación, debe ingresar a la sección “Comprar entradas” y allí indicar la fecha de visita deseada, la cantidad de entradas requeridas (que no puede superar las 10) y la edad de cada visitante. Finalmente, el sistema mostrará el monto total y se debe seleccionar la forma de pago: efectivo en caso de querer pagar en boletería o con tarjeta, donde se redirigirá al usuario a la página de Mercado Pago para completar el proceso de forma segura. Finalmente, recibirán un mensaje de confirmación vía mail y sus entradas serán verificadas al momento de ingresar al parque. La posibilidad de comprar las entradas mediante la aplicación nos parece fundamental para comenzar a probar la recepción de la aplicación, incluyendo el pago electrónico ya que creemos que será el más usado.

El Doce: ¡Muy claro! Parece que la aplicación requiere mucha atención. ¿Tienen previsto contratar personal adicional para mantener actualizados los horarios, las actividades y todo lo que implica?

Miguel: No, no hay problema en ese aspecto. Planeamos gestionar esa tarea por fuera de la aplicación, a través de nuestro equipo de administradores, que se encargará de mantener todo actualizado.

El Doce: Ah, entiendo. ¡Gracias por compartir todos estos emocionantes detalles! Más adelante coordinamos otra nota para ver esta aplicación en funcionamiento.

---

### Roles

Visitante: persona que utiliza la aplicación antes o durante su visita al parque para consultar información, ubicarse, inscribirse a actividades y comprar entradas.

    No se toma al administrador como rol de esta aplicación porque el enunciado aclara que la actualización de horarios, actividades y demás información se gestionará por fuera de la aplicación.

### User Stories

**US01** - Consultar mapa del parque

Como visitante quiero consultar el mapa del parque para ubicarme y reconocer los principales puntos de interés.

Criterios de aceptación:

- El mapa debe mostrar una vista panorámica del parque y diferenciar sus sectores por colores.
- Debe mostrar los baños mediante un ícono de inodoro.
- Debe mostrar los puntos de venta mediante un ícono de bolsa.
- Debe mostrar el show especial del día mediante un ícono de micrófono.
- Si existe un show programado, al seleccionar el ícono se debe mostrar su nombre y horario.

Pruebas de usuario:

- Probar visualizar el mapa con sus sectores, baños y puntos de venta. (pasa)
- Probar seleccionar el ícono del show cuando existe un show programado. (pasa)
- Probar seleccionar el ícono del show cuando no existe un show programado. (no debe mostrar información de un show inexistente)

Estimación: 5 Story Points
Justificación: Complejidad media. Requiere representar el parque, sus sectores y distintos puntos de interés. La incertidumbre es baja porque el comportamiento esperado está bastante claro.

**US02** - Consultar horarios de alimentación

Como visitante quiero consultar los horarios de alimentación de los animales para organizar mejor mi recorrido por el parque.

Criterios de aceptación:

- Cada horario debe mostrar especie, nombre del animal, edad, hora programada, sector y cuidador encargado.
- Los horarios deben mostrarse ordenados comenzando por los más próximos a la fecha actual y hasta una semana en el futuro.
- Se debe poder filtrar por la fecha en la que el visitante estará en el parque.
- Cuando falte una hora para comenzar un horario se debe mostrar el mensaje “¡Apúrate que ya comienza!”.

Pruebas de usuario:

- Probar consultar los horarios disponibles y verificar el orden desde los más próximos. (pasa)
- Probar filtrar los horarios por una fecha con actividades disponibles. (pasa)
- Probar visualizar un horario al que le falta una hora para comenzar. (pasa)

Estimación: 3 Story Points

Justificación: Complejidad baja a media. Principalmente requiere consulta, ordenamiento y filtro de información ya disponible.

**US03** - Consultar actividades

Como visitante quiero consultar las actividades disponibles para elegir cuál me interesa realizar durante mi visita.

Criterios de aceptación:

- Se deben mostrar las actividades disponibles: Tirolesa, Safari, Palestra y Jardinería.
- Se deben mostrar los horarios disponibles de cada actividad.
- La disponibilidad debe considerar los cupos de cada actividad.

Pruebas de usuario:

- Probar consultar una actividad que posee horarios y cupos disponibles. (pasa)
- Probar consultar una actividad sin cupos disponibles para un horario. (se informa que no hay cupo)

Estimación: 2 Story Points

Justificación: Complejidad baja. Es principalmente una consulta de actividades, horarios y disponibilidad.

**US04** - Inscribirse a una actividad

Como visitante quiero inscribirme a una actividad para reservar mi lugar en la misma.

Criterios de aceptación:

- Se debe seleccionar una actividad entre Tirolesa, Safari, Palestra y Jardinería, siempre que tenga cupo disponible para el horario elegido.
- Se debe seleccionar un horario disponible.
- Se debe indicar la cantidad de personas que participarán.
- Para cada participante se deben ingresar nombre, DNI, edad y talla de vestimenta si la actividad lo requiere.
- Se deben aceptar los términos y condiciones específicos de la actividad.
- Al finalizar la inscripción se debe enviar un correo electrónico con el resumen de la inscripción y un código QR.

Pruebas de usuario:

- Probar inscribirse a una actividad con cupo, completando los datos requeridos y aceptando los términos y condiciones. (pasa)
- Probar inscribirse a una actividad sin cupo para el horario seleccionado. (falla)
- Probar inscribirse sin ingresar talle cuando la actividad no lo requiere. (pasa)
- Probar inscribirse sin aceptar los términos y condiciones. (falla)
- Probar inscribirse sin talle cuando la actividad lo requiere. (falla)

Estimación: 5 Story Points

Justificación: Complejidad media. Además de registrar datos debe validar cupos, requisitos de la actividad y generar la confirmación con QR.

**US05** - Registrar visitante

Como visitante quiero registrarme en la aplicación para poder acceder a las funcionalidades que requieren identificación.

Criterios de aceptación:

- El registro debe solicitar mail y contraseña.

Pruebas de usuario:

- Probar registrar un visitante ingresando mail y contraseña. (pasa)
- Probar continuar el registro sin alguno de los datos requeridos. (falla)

Estimación: 2 Story Points

Justificación: Complejidad y esfuerzo bajos. La funcionalidad requiere pocos datos y no presenta dudas importantes según lo definido en el enunciado.

**US06** - Comprar entradas

Como visitante quiero comprar una entrada para asegurar mi visita al parque.

Criterios de aceptación:

- Solo se debe permitir la compra a visitantes registrados.
- Se debe indicar la fecha de visita, la cantidad de entradas, la edad de cada visitante y el tipo de pase (VIP o regular).
- La fecha de visita puede ser del día actual o futura y debe corresponder a un día en que el parque esté abierto.
- La cantidad de entradas no puede superar las 10.
- Se debe mostrar el monto total de la compra.
- Se debe permitir seleccionar la forma de pago. Si se paga con tarjeta, se debe redirigir a Mercado Pago.
- Al finalizar la compra se debe informar la cantidad de entradas compradas y la fecha de visita.
- Se debe enviar un mensaje de confirmación por mail.

Pruebas de usuario:

- Probar comprar entradas con fecha válida, hasta 10 entradas, datos completos y pago con tarjeta mediante Mercado Pago. (pasa)
- Probar comprar entradas sin seleccionar forma de pago. (falla)
- Probar comprar entradas para una fecha en la que el parque está cerrado. (falla)
- Probar comprar más de 10 entradas. (falla)
- Probar comprar entradas sin estar registrado. (falla)

Estimación: 8 Story Points

Justificación: Complejidad alta. Requiere varias validaciones y además integración con una pasarela de pago, por lo que tiene mayor esfuerzo e incertidumbre que las demás historias.

### User Story canónica

Se toma como User Story canónica la US05 - Registrar visitante, con 2 Story Points. La elegimos porque es una funcionalidad simple, con pocos datos, bajo esfuerzo y poca incertidumbre. Se utiliza como referencia para comparar el tamaño relativo de las demás historias.

### MVP propuesto

Para el MVP buscamos validar si la aplicación aporta valor real al visitante antes y durante la visita. Tomando el criterio trabajado en clase, se priorizan las funcionalidades que permiten autogestionar acciones importantes y mejorar directamente la experiencia dentro del parque.

User Stories incluidas en el MVP:

- US01 - Consultar mapa del parque.
- US04 - Inscribirse a una actividad.
- US06 - Comprar entradas.

El registro del visitante se considera una dependencia necesaria para realizar la compra de entradas, ya que el enunciado indica que solo los visitantes registrados pueden comprar.

La compra de entradas es especialmente importante para validar la recepción de la aplicación, incluyendo el pago electrónico. La inscripción a actividades permite validar una necesidad con cupos limitados y organización previa. El mapa aporta valor directo durante la visita al facilitar la orientación dentro del parque.

User Stories que quedan fuera del MVP inicial:

- US02 - Consultar horarios de alimentación.
- US03 - Consultar actividades.

Estas funcionalidades aportan valor, pero no son las principales para comprobar la primera versión del producto. Pueden incorporarse en iteraciones posteriores.

También quedan fuera del MVP las mejoras que el propio enunciado plantea para versiones futuras, como las notificaciones de recordatorio de horarios de alimentación y la ubicación del visitante en tiempo real. La gestión administrativa del parque se realiza por fuera de la aplicación.