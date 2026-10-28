# Ingeniería y Calidad de Software — Resumen integral del segundo parcial

**UTN — Facultad Regional Córdoba · Apunte de estudio integrado**

Este documento reúne y desarrolla los contenidos de los archivos de la carpeta, siguiendo el temario del segundo parcial. Incluye definiciones, relaciones, comparaciones, ejemplos resueltos y preguntas de repaso. Se excluye el tema de escalamiento de Scrum indicado como fuera del examen.

El núcleo evaluable comprende **Lean y Kanban; métricas tradicionales, ágiles y Lean; prácticas continuas; calidad de proceso y producto; modelos de calidad; auditorías; testing; revisiones técnicas y testing ágil**. Se conserva una base de Scrum y gestión de productos para entender sus relaciones con esos temas.

**Criterio de elaboración.** La base es el material de la cátedra. Las ampliaciones sobre CI/CD, SPICE, algunas normas ISO y auditoría al grupo de calidad se identifican como complementos porque los originales las desarrollan poco. Los ejemplos son didácticos, no preguntas oficiales. Cuando los apuntes mezclan versiones o usan términos de formas diferentes, se explica la diferencia. Las cifras históricas ilustrativas de las diapositivas no se presentan como estadísticas universales vigentes.

## Índice

1. [Mapa general de la materia](#mapa-general)
2. [Base ágil y Scrum](#base-agil)
3. [Filosofía Lean](#lean)
4. [Método Kanban](#kanban)
5. [Métricas en los tres enfoques](#metricas)
6. [Gestión de software como producto](#producto)
7. [Prácticas continuas y gestión de builds](#continuas)
8. [TDD, ATDD y refactoring](#tdd)
9. [Conceptos generales de calidad](#calidad)
10. [Aseguramiento y planificación de la calidad](#sqa)
11. [Modelos de calidad de producto e ISO](#iso-producto)
12. [Mejora de procesos, CMMI, SPICE e IDEAL](#modelos-proceso)
13. [Verificación y validación](#vv)
14. [Testing: fundamentos, proceso y planificación](#testing)
15. [Niveles, tipos y ambientes de prueba](#niveles)
16. [Técnicas de diseño de pruebas y ejercicios](#tecnicas)
17. [Herramientas y automatización](#herramientas)
18. [Revisiones técnicas](#revisiones)
19. [Auditorías de software](#auditorias)
20. [Testing en ambientes ágiles](#testing-agil)
21. [Caso integrador](#caso)
22. [Comparaciones y errores frecuentes](#comparaciones)
23. [Preguntas de parcial con respuestas guía](#preguntas)
24. [Lista de control de estudio y fuentes](#fuentes)

---

<a id="mapa-general"></a>
## 1. Mapa general de la materia

La materia conecta tres problemas: **construir lo que aporta valor**, **organizar el trabajo para entregarlo** y **lograr que el producto y el proceso tengan la calidad necesaria**.

| Pregunta | Conceptos que ayudan a responderla |
|---|---|
| ¿Qué problema vale la pena resolver? | Gestión de producto, propuesta de valor, hipótesis, MVP, feedback. |
| ¿Cómo organizar el trabajo ante la incertidumbre? | Agilidad, Scrum, Lean, Kanban. |
| ¿Cómo conocer el estado real y mejorar? | Métricas, inspección, adaptación, mejora de procesos. |
| ¿Cómo integrar y entregar cambios con confianza? | SCM, builds, integración continua, pruebas automatizadas, TDD. |
| ¿Qué significa que el software sea de calidad? | Necesidades de interesados, atributos de producto, calidad en uso. |
| ¿Cómo prevenir y detectar problemas? | SQA, planificación, revisiones, testing y auditorías. |
| ¿Cómo sostener la mejora organizacional? | CMMI, SPICE, normas ISO, IDEAL. |

Un producto puede estar técnicamente bien construido y resolver un problema que nadie tiene. También puede ser deseado por los usuarios y fallar por defectos graves. Por eso hay que atender **valor, calidad técnica y capacidad del proceso** al mismo tiempo.

Tres niveles de análisis que aparecen durante todo el apunte:

- **Producto:** lo que se construye y mantiene, incluyendo código, datos, documentación y comportamiento.
- **Proyecto:** el esfuerzo organizado con objetivos, alcance, recursos, costos y tiempos.
- **Proceso:** la forma de trabajar que transforma entradas en resultados y puede repetirse, medirse y mejorarse.

Un defecto en producción puede llevar a corregir el producto, ajustar el plan del proyecto e investigar qué cambio en el proceso evitaría su repetición.

<a id="base-agil"></a>
## 2. Base ágil y Scrum

### 2.1. Control empírico del proceso

En desarrollo de software existen incertidumbres sobre requisitos, soluciones técnicas, esfuerzo y uso real. El control empírico utiliza la experiencia y la evidencia para ajustar decisiones.

Sus pilares son:

1. **Transparencia:** hacer visible el estado real del trabajo y usar criterios compartidos. Si alguien dice «terminado» pero falta probar e integrar, no hay transparencia.
2. **Inspección:** examinar con frecuencia el producto, el trabajo y el avance hacia los objetivos.
3. **Adaptación:** cambiar el plan o la forma de trabajo cuando lo observado muestra una desviación o una oportunidad.

La inspección pierde utilidad si no produce acciones. La adaptación se vuelve arbitraria si no se basa en información confiable.

### 2.2. Valores y principios ágiles

El Manifiesto Ágil prioriza individuos e interacciones, software funcionando, colaboración con el cliente y respuesta al cambio. Esto no elimina el valor de procesos, herramientas, documentación, contratos y planes: establece qué debe pesar más cuando entran en tensión.

Los principios del material pueden organizarse así:

- Satisfacer al cliente mediante entregas tempranas y frecuentes de software valioso.
- Aceptar cambios y aprovecharlos para mejorar el resultado.
- Favorecer la colaboración cotidiana entre negocio y desarrollo.
- Trabajar con personas motivadas, confianza y comunicación efectiva.
- Medir el progreso principalmente por software funcionando.
- Mantener un ritmo sostenible y cuidar la excelencia técnica y el buen diseño.
- Buscar simplicidad: evitar trabajo que no sea necesario.
- Permitir que el equipo se organice y reflexione periódicamente para mejorar.

**Consecuencia para calidad:** la rapidez no consiste en omitir pruebas, sino en obtener feedback temprano y evitar grandes cantidades de retrabajo.

### 2.3. Scrum como marco de trabajo

Scrum organiza el trabajo en Sprints y permite producir incrementos, inspeccionarlos y adaptar el rumbo. Sus valores son compromiso, foco, apertura, respeto y coraje.

| Responsabilidad | Función central |
|---|---|
| Product Owner | Maximizar el valor del producto, comunicar el objetivo y gestionar eficazmente el Product Backlog. |
| Developers | Crear un incremento utilizable, planificar el trabajo técnico y sostener la calidad. Incluye las capacidades necesarias para construir el producto, no solamente programar. |
| Scrum Master | Ayudar a comprender y aplicar Scrum, mejorar la efectividad y promover la eliminación de impedimentos. |

El equipo necesita autogestión y capacidades suficientes para completar el trabajo. Un especialista en testing puede formar parte del equipo; la responsabilidad por la calidad sigue siendo compartida.

### 2.4. Eventos, artefactos y compromisos

| Evento | Propósito | Timebox de referencia |
|---|---|---|
| Sprint | Contener el trabajo para alcanzar un objetivo y producir valor. | Un mes o menos. |
| Sprint Planning | Definir por qué el Sprint es valioso, qué se abordará y cómo se trabajará. | Hasta 8 horas para un Sprint de un mes. |
| Daily Scrum | Inspeccionar el avance hacia el Sprint Goal y adaptar el plan. | 15 minutos. |
| Sprint Review | Inspeccionar el resultado con interesados y ajustar decisiones sobre el producto. | Hasta 4 horas para un Sprint de un mes. |
| Sprint Retrospective | Mejorar calidad y efectividad del trabajo del equipo. | Hasta 3 horas para un Sprint de un mes. |

Los eventos más largos suelen acortarse cuando el Sprint es menor. La Daily no es un reporte al jefe; la Review no es solamente una demostración; la Retrospective necesita acciones concretas.

| Artefacto | Qué representa | Compromiso asociado |
|---|---|---|
| Product Backlog | Lista emergente y ordenada del trabajo necesario para mejorar el producto. | Product Goal. |
| Sprint Backlog | Objetivo del Sprint, elementos seleccionados y plan para entregarlos. | Sprint Goal. |
| Incremento | Resultado utilizable que se integra con lo anterior. | Definition of Done. |

**Definition of Done (DoD):** entendimiento compartido del estado de calidad que debe alcanzar un incremento. Puede exigir revisión, pruebas, integración y documentación pertinente. Un ítem con código terminado pero pruebas pendientes no está Done si la DoD exige esas pruebas.

**Criterios de aceptación:** condiciones específicas de una historia o funcionalidad. Por ejemplo, «un socio suspendido no puede reservar». La DoD es transversal; los criterios de aceptación describen lo que debe cumplir ese comportamiento particular.

**Refinamiento:** actividad continua para descomponer y aclarar elementos del backlog. La Definition of Ready puede ayudar a acordar cuándo un ítem está suficientemente entendido.

**Aclaración del material de Scrum:** las diapositivas mezclan la guía 2020 con una propuesta expandida. OODA, Supporters y la distinción Output/Outcome Done se pueden estudiar como ideas complementarias de ese material, sin confundirlas con responsabilidades o compromisos formales de la guía 2020. Tampoco el 10% para refinamiento es un timebox obligatorio en esa guía. [Referencia de contraste: Scrum Guide 2020](https://scrumguides.org/scrum-guide.html).

### 2.5. Planificación de producto, release y Sprint

La planificación tiene distintos horizontes: estrategia, portfolio, producto, release, iteración y día. Cuanto más cercano es el trabajo, mayor puede ser el detalle.

- La **visión** explica qué se busca y para quién.
- El **roadmap** comunica una dirección de evolución y resultados esperados.
- El **release** agrupa una entrega a usuarios; puede ocurrir después de varios Sprints, en cada Sprint o con mayor frecuencia.
- El **Sprint** organiza un horizonte corto de trabajo.
- Las **tareas** concretan cómo se realizarán los elementos elegidos.

El plan se actualiza con evidencia sobre capacidad, velocidad, cambios de alcance, dependencias y riesgos. Una estimación sirve para decidir; no garantiza que no habrá variaciones.

<a id="lean"></a>
## 3. Filosofía Lean

### 3.1. Qué busca Lean

Lean busca entregar valor al cliente utilizando los recursos de manera razonable y reduciendo desperdicios. El valor se juzga por el beneficio para quien recibe el producto o servicio.

En software, escribir más líneas, iniciar muchas tareas o mantener a todas las personas ocupadas no demuestra por sí mismo que se esté entregando valor. Puede haber mucho trabajo en marcha y pocas funcionalidades utilizables.

### 3.2. Los siete principios del material

| Principio | Explicación | Ejemplo en software |
|---|---|---|
| Eliminar desperdicios | Identificar y reducir actividades o resultados que no aportan valor. | Dejar de desarrollar una funcionalidad que nadie necesita. |
| Amplificar el aprendizaje | Acortar el tiempo entre una decisión y la evidencia sobre su resultado. | Probar un prototipo con usuarios antes de construir toda la solución. |
| Embeber la integridad conceptual | Construir coherencia y calidad desde el diseño y durante todo el desarrollo. | Mantener reglas de negocio consistentes entre interfaz, servicios y datos. |
| Diferir compromisos | Conservar opciones hasta contar con información suficiente, sin perder la oportunidad de decidir. | Experimentar antes de comprometer una arquitectura difícil de cambiar. |
| Dar poder al equipo | Permitir que quienes conocen el trabajo decidan cómo mejorarlo. | Que el equipo ajuste su flujo y proponga automatización. |
| Ver el todo | Optimizar el resultado global y las relaciones entre etapas. | Mejorar el cuello de botella de pruebas, aunque programación ya sea rápida. |
| Entregar lo antes posible | Reducir el tiempo hasta que el cliente recibe valor y se obtiene feedback. | Liberar una porción pequeña, completa y utilizable. |

**Diferir compromisos** no significa postergar por indecisión. Se trata de reconocer qué información falta, cuánto cuesta esperar y cuál es el último momento responsable para resolver.

**Integridad conceptual** significa que el producto se percibe y funciona como un conjunto coherente. Reducir alcance puede ser razonable; romper la consistencia del producto genera problemas de comprensión, mantenimiento y uso.

### 3.3. Desperdicio necesario y puro desperdicio

- **Tipo 1: necesario en las condiciones actuales.** No aporta valor directo, pero alguna restricción exige realizarlo. Se intenta minimizarlo o eliminar la causa que lo vuelve necesario.
- **Tipo 2: puro desperdicio.** Puede evitarse sin perjudicar la entrega de valor ni incumplir obligaciones.

Ejemplo: registrar una aprobación exigida puede ser necesario; transcribir manualmente esa misma aprobación en cuatro sistemas agrega trabajo evitable.

### 3.4. Los 7 + 1 desperdicios aplicados a software

| Desperdicio | Cómo se manifiesta | Qué problema produce |
|---|---|---|
| Inventario | Código sin integrar, historias a medio terminar, grandes colas de trabajo. | Se invierte esfuerzo sin obtener valor utilizable; aparecen riesgos ocultos. |
| Sobreproducción | Funcionalidades no solicitadas o construidas demasiado temprano. | Se gasta en supuestos que pueden ser incorrectos. |
| Sobreprocesamiento | Revisiones redundantes, documentación sin uso, soluciones excesivamente complejas. | Aumenta costo y demora sin beneficio proporcional. |
| Transporte o transferencias | Pases constantes entre áreas, pérdida de contexto y conocimiento. | Aparecen errores de comunicación y esperas. |
| Esperas | Bloqueos por decisiones, ambientes, aprobaciones o dependencias. | Aumenta el tiempo de entrega aunque nadie esté trabajando sobre el ítem. |
| Movimiento o cambio de contexto | Alternar continuamente entre tareas y buscar información dispersa. | Se pierde concentración y se repite esfuerzo de comprensión. |
| Defectos | Requisitos incorrectos, errores de código, datos erróneos. | Generan correcciones, nuevas pruebas y posibles fallas al cliente. |
| Talento no utilizado | Ignorar conocimiento, creatividad y propuestas del equipo. | Se desaprovechan oportunidades de aprendizaje y mejora. |

Las categorías pueden superponerse: una transferencia puede provocar una espera y también pérdida de información. Lo importante es identificar la causa y su impacto.

### 3.5. Optimización local frente a optimización global

Supongamos que desarrollo termina diez historias por semana y pruebas puede procesar cinco. Aumentar desarrollo a quince no aumenta las entregas: agranda la cola frente a pruebas. La mejora debe atender la restricción del sistema, por ejemplo colaborando con automatización, aclarando criterios antes o reduciendo defectos de entrada.

La ocupación extrema deja poco margen para absorber variaciones y resolver bloqueos. La frase de las diapositivas sobre el problema de trabajar al 100% se interpreta como una advertencia contra saturar el sistema, no como una ley que afirme que toda utilización alta siempre produce rendimiento nulo.

<a id="kanban"></a>
## 4. Método Kanban

### 4.1. Definición y enfoque

Kanban es un método para definir, gestionar y mejorar servicios que entregan trabajo del conocimiento. Hace visible el trabajo, limita lo que está en curso y utiliza datos para mejorar el flujo.

Un tablero es una herramienta del método. Pegar tarjetas en columnas sin límites, políticas ni revisión del flujo no equivale a aplicar todas sus prácticas.

El origen de las señales Kanban se relaciona con la reposición según consumo en producción Just in Time. En software la idea central es **incorporar trabajo cuando existe capacidad**, evitando acumulaciones innecesarias.

### 4.2. Valores y principios

Los valores presentados son transparencia, equilibrio, colaboración, foco en el cliente, flujo, liderazgo, entendimiento, acuerdo y respeto.

Los principios de gestión del cambio son:

1. Comenzar con la forma actual de trabajar, comprendiendo procesos, roles y responsabilidades.
2. Acordar una mejora evolutiva, mediante cambios que puedan observarse y ajustarse.
3. Fomentar liderazgo en todos los niveles.

Los principios de entrega de servicios son comprender las necesidades del cliente, gestionar el trabajo permitiendo la autoorganización y revisar periódicamente servicios y políticas para mejorar resultados.

### 4.3. Las seis prácticas generales

**1. Visualizar.** Representar estados, colas, bloqueos, tipos de trabajo y riesgos. El tablero debe reflejar cómo se trabaja realmente. Un ejemplo es: Pendiente → Análisis → Desarrollo → Pruebas → Listo para desplegar → Entregado.

**2. Limitar el WIP.** WIP es Work in Progress: trabajo iniciado que aún no llegó al punto de finalización definido. Los límites pueden aplicarse a etapas o a todo el sistema. Ayudan a terminar antes de comenzar más.

**3. Gestionar el flujo.** Observar cómo se mueven los ítems, dónde esperan y qué impide completarlos. Usar tiempos y comportamiento histórico para mejorar previsibilidad.

**4. Hacer explícitas las políticas.** Acordar criterios de ingreso y salida, límites, tratamiento de bloqueos, prioridades y clases de servicio. Las reglas deben ser visibles, simples y revisables.

**5. Establecer ciclos de feedback.** Reunirse con una cadencia útil para revisar trabajo, reposición y mejoras.

**6. Mejorar colaborativamente y experimentar.** Formular una hipótesis, cambiar algo, observar el efecto y decidir si se conserva. Ejemplo: «Si reducimos el WIP de desarrollo de seis a cuatro, disminuirá la cola de pruebas sin reducir las entregas».

### 4.4. Push, pull y límites de WIP

En un sistema **push**, una etapa envía trabajo a la siguiente aunque esté saturada. En un sistema **pull**, se toma trabajo cuando hay capacidad y se cumplen las políticas.

Ejemplo: Pruebas tiene límite WIP = 3 y ya hay tres historias en ese estado. Antes de pasar una cuarta, el equipo analiza cómo terminar o desbloquear las actuales. Puede colaborar con datos de prueba, corregir un defecto o resolver una dependencia.

El límite hace visible el problema. Saltarlo sistemáticamente para que cada persona siga iniciando tareas elimina esa señal. Un bloqueo tampoco justifica ocultar la tarjeta o retirarla del conteo sin una política que lo contemple.

**WIP no es cantidad de personas.** Una persona puede participar de varios ítems y varias personas pueden colaborar sobre uno. El límite se refiere al trabajo en el sistema.

### 4.5. Políticas y clases de servicio

Una política podría indicar: «Una historia puede entrar en pruebas si está integrada, tiene criterios de aceptación claros y sus pruebas unitarias pasan».

Las clases de servicio permiten tratar trabajos con distinto costo de demora:

| Clase | Sentido | Ejemplo |
|---|---|---|
| Expreso | Atención excepcional por urgencia; necesita límites y reglas para no desplazar permanentemente todo lo demás. | Incidente que impide operar a los clientes. |
| Fecha fija | El valor o costo depende de una fecha; se planifica su ingreso. | Adaptación requerida para una fecha acordada. |
| Estándar | Trabajo habitual, ordenado según valor y políticas de selección. | Nueva consulta solicitada por usuarios. |
| Intangible | Su demora no tiene un impacto inmediato muy visible, pero puede aumentar riesgos futuros. | Reducir deuda técnica o renovar infraestructura. |

Los colores y la regla del expreso con WIP = 1 son ejemplos de las diapositivas. Cada servicio debe acordar sus políticas; no son colores universales obligatorios.

### 4.6. Cadencias

- **Kanban Meeting:** observar el flujo y los bloqueos, habitualmente a diario. Conviene revisar el trabajo cercano a terminar.
- **Replenishment Meeting:** seleccionar qué trabajo se incorporará cuando haya capacidad, semanalmente o según demanda.
- **Retrospectiva:** revisar cómo funciona el sistema y proponer mejoras, por ejemplo quincenal o mensualmente.

Estas frecuencias son orientativas. Lo central es que el feedback sirva para decidir.

### 4.7. Scrum y Kanban

| Aspecto | Scrum | Kanban |
|---|---|---|
| Organización principal | Sprints con objetivo y eventos definidos. | Flujo de trabajo y gestión del servicio. |
| Cambio inicial | Introduce un marco con responsabilidades, eventos y artefactos. | Parte del proceso existente y promueve evolución. |
| Regulación del trabajo | Plan del Sprint, objetivo y adaptación continua. | Límites WIP y políticas de pull. |
| Métricas destacadas en los apuntes | Velocidad, capacidad, RTF. | Lead time, cycle time, touch time, eficiencia. |
| Mejora | Inspección y adaptación, especialmente retrospectiva. | Feedback y experimentos sobre el flujo. |

Pueden combinarse: un equipo Scrum puede visualizar su flujo y limitar el WIP. No hay que confundir el tablero de tareas de un Sprint con la totalidad del método Kanban.

<a id="metricas"></a>
## 5. Métricas en los tres enfoques

### 5.1. Para qué medir

Una métrica debe responder una pregunta y apoyar una decisión. Medir por acumulación puede generar costos, ruido e incentivos contraproducentes.

Antes de elegirla, preguntar: ¿qué queremos conocer?, ¿cómo se obtiene?, ¿qué unidad y alcance tiene?, ¿cómo se interpreta?, ¿qué acción podríamos tomar?

El material diferencia métricas de proceso, proyecto y producto. Las de distintos proyectos pueden consolidarse para aprender sobre el proceso organizacional, siempre que sus definiciones permitan compararlas.

### 5.2. Enfoque tradicional

Las métricas permiten comparar planificación y ejecución, controlar desviaciones y mejorar estimaciones.

| Métrica | Qué informa | Precaución |
|---|---|---|
| Tamaño | Magnitud del producto: líneas, funciones, casos de uso u otra unidad definida. | Tamaño no equivale a valor. |
| Esfuerzo | Trabajo humano invertido, por ejemplo horas-persona. | No confundir con tiempo calendario. |
| Duración | Tiempo transcurrido entre hitos. | Incluye esperas; puede disminuir con paralelismo sin bajar el esfuerzo. |
| Costo | Recursos económicos consumidos. | Requiere aclarar qué costos se incluyen. |
| Defectos | Cantidad, severidad, origen y distribución. | Un número aislado depende del alcance y del esfuerzo de detección. |
| Avance | Tareas o hitos completados frente a lo planificado. | Tareas cerradas no garantizan funcionalidades utilizables. |
| Volatilidad de requisitos | Cambios del alcance a lo largo del tiempo. | Puede reflejar aprendizaje legítimo, además de inestabilidad. |

Ejemplo: dos personas trabajan cinco días, cuatro horas diarias cada una. El esfuerzo es `2 × 5 × 4 = 40 horas-persona`; la duración es cinco días. Si luego el resultado espera aprobación tres días, el plazo hasta la aprobación aumenta aunque no haya más esfuerzo productivo.

Las diapositivas proponen observar estimado frente a real, distribución del esfuerzo, presupuesto, cobertura, defectos en revisiones y pruebas, y defectos que llegan a la release.

### 5.3. Enfoque ágil

La prioridad es conocer el avance hacia software funcionando y valor. La expresión «la medición es una salida, no una actividad» propone obtener información del trabajo y evitar una burocracia de medición desproporcionada.

**Velocidad:** suma de puntos de historias completamente terminadas en una iteración, según el criterio de terminado acordado.

Ejemplo: se seleccionaron historias de 3, 5, 8 y 5 puntos. Solo las de 3, 5 y 5 están Done. La velocidad es `13 puntos`, aunque la de 8 esté «casi terminada».

La velocidad histórica puede orientar pronósticos del mismo equipo. Si quedan 60 puntos y el equipo termina aproximadamente 20 por Sprint, tres Sprints es una primera aproximación, condicionada por cambios, incertidumbre y estabilidad del contexto. No debe usarse para comparar personas o equipos con escalas diferentes ni para prometer una fecha exacta.

**Capacidad:** disponibilidad real para trabajar en el período. Se consideran ausencias, reuniones, soporte y otros compromisos.

```text
Capacidad del equipo = suma de la disponibilidad efectiva de sus integrantes

Ejemplo: 4 personas × 8 días × 5 horas efectivas = 160 horas
```

Capacidad y velocidad se relacionan, pero no son equivalentes: una representa disponibilidad; la otra, trabajo terminado medido con una escala de estimación. No existe una conversión universal de puntos a horas.

**RTF — Running Tested Features:** funcionalidades que están funcionando y probadas. Ayuda a evitar que el progreso se exprese solo en documentos, código aislado o porcentajes subjetivos.

**Burndown:** muestra trabajo restante. **Burnup:** muestra trabajo completado; si incluye la línea de alcance permite ver sus cambios. Una curva debe interpretarse junto con el contexto: un aumento de trabajo restante puede provenir de descubrir alcance, no necesariamente de falta de avance.

### 5.4. Enfoque Lean/Kanban

Para los apuntes se adopta esta convención:

- **Lead time:** desde que se solicita un ítem hasta que se entrega.
- **Cycle time:** desde que comienza su trabajo hasta que termina.
- **Touch time:** tiempo en el que se trabaja efectivamente sobre el ítem, excluyendo esperas y colas.

```text
Touch time ≤ Cycle time ≤ Lead time
```

La relación requiere medir el mismo ítem, con límites de proceso y unidades compatibles. No se deben sumar horas-persona de trabajo paralelo y compararlas sin más con horas de reloj.

**Ejemplo resuelto:** una solicitud llega en el día 0, se empieza en el día 3 y se entrega en el día 10. Durante ese recorrido recibe dos días equivalentes de trabajo efectivo.

| Medida | Cálculo | Resultado |
|---|---|---|
| Lead time | 10 − 0 | 10 días. |
| Cycle time | 10 − 3 | 7 días. |
| Touch time | Tiempo efectivo registrado | 2 días. |
| Espera antes del inicio | 3 − 0 | 3 días. |
| Tiempo sin trabajo efectivo dentro del ciclo | 7 − 2 | 5 días. |

**Eficiencia de flujo o de ciclo del proceso:**

```text
Eficiencia (%) = Touch time / Tiempo transcurrido del alcance elegido × 100
```

Si el alcance es solicitud a entrega: `2 / 10 × 100 = 20%`. Si es inicio a finalización: `2 / 7 × 100 ≈ 28,6%`. Hay que declarar el denominador; no son porcentajes contradictorios, sino alcances distintos. La fórmula abreviada de las diapositivas necesita multiplicarse por 100 para expresar un porcentaje.

**Lectura del resultado:** mejorar el tiempo efectivo de programación puede tener menos impacto que reducir los ocho días sin trabajo efectivo dentro del lead time. El dato orienta a buscar esperas, bloqueos o transferencias.

Como complemento de vocabulario, **throughput** es cantidad de ítems terminados por unidad de tiempo. Lead time y cycle time son duraciones; no son, por sí solos, cantidades de entregas por semana.

### 5.5. Métricas orientadas al servicio

| Concepto | Significado | Ejemplo didáctico |
|---|---|---|
| Expectativa de servicio | Lo que el cliente espera recibir. | Una respuesta en dos días. |
| Capacidad de servicio | Lo que el sistema puede entregar de acuerdo con datos. | La mayoría de solicitudes tarda entre tres y cinco días. |
| Acuerdo de servicio | Compromiso negociado con el cliente. | Plazo acordado de cinco días para una clase de solicitud. |
| Umbral de adecuación | Límite a partir del cual el servicio deja de ser aceptable. | Más de diez días hace inútil la respuesta. |

No alcanza con prometer: hay que comparar expectativa, capacidad y acuerdo. Si hay una brecha, se cambia el sistema o se renegocia de forma explícita.

### 5.6. Métricas de producto y calidad

- **Densidad de defectos:** defectos / tamaño. Aclarar unidad, versión, alcance y momento de detección.
- **Cobertura de requisitos:** requisitos cubiertos por pruebas / requisitos considerados × 100.
- **Cobertura de código:** elementos ejecutados / elementos considerados × 100; especificar sentencias, decisiones u otro criterio.
- **Distribución por severidad:** permite distinguir muchos detalles cosméticos de pocos problemas críticos.
- **Defectos escapados:** defectos descubiertos después de la etapa en que se esperaba detectarlos, por ejemplo en producción.

Una cobertura alta no demuestra que las comprobaciones sean correctas ni que se hayan probado todos los comportamientos importantes. La cobertura de requisitos y la de código responden preguntas diferentes.

### 5.7. Comparación para el parcial

| Enfoque | Pregunta predominante | Métricas destacadas |
|---|---|---|
| Tradicional | ¿Cómo estamos respecto del plan y de los recursos previstos? | Esfuerzo, tiempo, costo, tamaño, defectos. |
| Ágil | ¿Cuánto software utilizable estamos completando y cómo planificar lo próximo? | Velocidad, capacidad, RTF, gráficos de avance. |
| Lean | ¿Cómo fluye el trabajo y cuánto tarda en llegar el valor? | Lead time, cycle time, touch time, eficiencia. |

La clasificación refleja el énfasis de la cátedra. Un equipo ágil también controla costos y un equipo tradicional puede medir tiempos de flujo. Una buena combinación responde al contexto.

**Error frecuente:** recompensar cantidad de defectos encontrados o líneas escritas como si midieran productividad directa. Puede incentivar conductas que empeoren el producto. Las métricas deben apoyar comprensión y mejora, no reemplazar el juicio.

<a id="producto"></a>
## 6. Gestión de software como producto

### 6.1. Construcción, valor y aprendizaje

Gestionar un producto implica sostenerlo durante su vida: descubrir necesidades, construir, entregar, observar uso, mantener y evolucionar. Terminar un proyecto no demuestra que el producto haya logrado el resultado buscado.

Conviene distinguir:

- **Output:** algo producido, como una pantalla o una funcionalidad.
- **Outcome:** cambio logrado en usuarios o negocio, como reducir abandonos al reservar.

Un equipo puede aumentar sus outputs sin mejorar outcomes. Por eso debe formular hipótesis y contrastarlas.

### 6.2. Ciclo Lean Startup

**Construir → Medir → Aprender.** Se crea un experimento o una versión pequeña, se recoge evidencia y se decide qué hacer a continuación.

La hipótesis de valor pregunta si la solución beneficia a los usuarios. La hipótesis de crecimiento pregunta cómo se incorporan y permanecen nuevos usuarios. Retención, uso y referencias pueden aportar evidencia, siempre que correspondan a la hipótesis.

El material usa Dropbox y Facebook como casos didácticos de validación temprana. La idea relevante es aprender sobre demanda y comportamiento antes de comprometer una gran inversión. Un video que demuestra interés no valida por sí mismo toda la factibilidad técnica.

### 6.3. MVP, propuesta de valor y pivote

La **propuesta de valor única (UVP)** expresa qué beneficio diferencial se ofrece y para quién. El **MVP** es el experimento mínimo adecuado para obtener aprendizaje sobre una hipótesis importante.

«Mínimo» se refiere a reducir el esfuerzo y alcance necesarios para aprender. No autoriza a ignorar seguridad, fiabilidad o usabilidad cuando esas condiciones son necesarias para el experimento o para los usuarios involucrados.

Ejemplo: para explorar si se necesita reservar canchas desde el celular, se puede validar interés con una prueba acotada. Si se entregará un producto real de reservas, debe evitar reservas duplicadas aunque tenga pocas funciones.

Un **pivote** es un cambio de dirección basado en aprendizaje: segmento, problema, propuesta o solución. Una solicitud aislada no obliga a pivotar; se buscan patrones y evidencia.

### 6.4. Los distintos «mínimos»

| Concepto | Objetivo central | Ejemplo |
|---|---|---|
| MVP | Validar una hipótesis con el mínimo experimento útil. | Probar si usuarios quieren reservar sin llamar. |
| MMF — Minimum Marketable Feature | Entregar la menor funcionalidad con valor comercial identificable. | Cancelación de reservas con reintegro según política. |
| MVF — Minimum Viable Feature | Explorar una función en un área de incertidumbre. | Probar recordatorios personalizados en un grupo reducido. |
| MMP — Minimum Marketable Product | Formar un producto mínimo suficientemente completo para comercializar. | Primera versión utilizable del sistema de reservas. |
| MMR — Minimum Marketable Release | Agrupar el incremento mínimo de valor para una nueva liberación. | Versión que incorpora lista de espera y avisos. |
| MLP — Minimum Lovable Product | Buscar una experiencia que genere preferencia y vínculo positivo. | Reserva simple, clara, confiable y agradable en el contexto del usuario. |

El material relaciona MLP con utilidad, satisfacción y cuidado, y enumera esperanza, confianza personal, confianza en el sistema, escala, sostenibilidad, crecimiento, motivación, diversión, inspiración y efecto halo. Para estudiar, interesa entender que una experiencia apreciada puede depender de simplicidad y fiabilidad, no solamente de efectos visuales.

### 6.5. Historias, priorización y roadmap

Una funcionalidad valiosa puede requerir varias historias pequeñas. La división debe facilitar aprendizaje, prueba e integración. Es preferible una porción vertical que atraviese las capas necesarias para observar un comportamiento, en lugar de dejar todas las bases de datos terminadas pero ningún flujo utilizable.

El material propone priorizar según importancia y urgencia: hacer lo esencial, planear lo importante no urgente, considerar delegación o integración externa y eliminar lo irrelevante. La matriz es una ayuda; no reemplaza el análisis de valor, dependencias y riesgo.

El roadmap conecta aprendizaje inicial, primer producto comercializable e incrementos posteriores. Puede cambiar cuando se conoce mejor el mercado.

**Relación con el resto de la materia:** las prácticas continuas permiten entregar y aprender frecuentemente; las métricas muestran si el trabajo fluye; la calidad hace que ese aprendizaje se apoye en un producto confiable.

<a id="continuas"></a>
## 7. Prácticas continuas y gestión de builds

### 7.1. Qué significa trabajar de manera continua

Consiste en realizar actividades clave con frecuencia y en pequeños lotes: integrar, construir, probar, revisar y obtener feedback. Se busca detectar diferencias y defectos cuando son pequeños y recientes.

«Continuo» no significa ejecutar todo sin pausa ni publicar cualquier cambio incompleto. Significa incorporar estas prácticas al trabajo habitual y sostener un resultado verificable.

### 7.2. SCM: gestión de configuración del software

SCM permite identificar y controlar versiones de los elementos que componen el producto, conocer sus cambios y reproducir una configuración determinada. Abarca más que guardar código: también intervienen pruebas, scripts, configuraciones, dependencias y documentación pertinente.

Conceptos útiles para leer el PDF de SCM:

- **Repositorio:** lugar donde se conserva el historial y los elementos versionados.
- **Línea de código o codeline:** evolución relacionada de versiones sobre la que trabaja el equipo.
- **Workspace:** espacio de trabajo del desarrollador o del proceso de construcción.
- **Commit:** registro de un conjunto de cambios.
- **Etiqueta o tag:** identificación de una revisión, por ejemplo la usada para una release.
- **Configuración identificada:** conjunto conocido de versiones, dependencias y opciones que permite explicar qué se construyó.

Sin identificación de versiones, un reporte de prueba o una auditoría pierde precisión: no se puede asegurar a qué producto corresponden sus evidencias.

### 7.3. Qué es un build

Un build transforma componentes fuente en un resultado utilizable. Puede incluir recuperar versiones, resolver dependencias, generar archivos, compilar y empaquetar. El proceso automatizado también puede ejecutar pruebas y producir informes.

El PDF distingue:

- **Build completo o clean:** comienza sin reutilizar artefactos derivados de construcciones previas. Ayuda a detectar dependencias ocultas y problemas del ambiente.
- **Build incremental:** reconstruye lo que cambió o depende de lo modificado. Reduce tiempos si el manejo de dependencias es correcto.

Un build exitoso que solo compiló no demuestra corrección funcional. Hay que conocer qué verificaciones incluyó.

### 7.4. Los tres patrones de build del material

| Build | Destinatario principal | Momento | Propósito |
|---|---|---|---|
| Private System Build | Desarrollador individual. | Durante una tarea y antes de compartir cambios. | Verificar que sus modificaciones construyen y funcionan con la versión integrada reciente. |
| Integration Build | Equipo de desarrollo. | Al integrar cambios o con alta frecuencia. | Comprobar el conjunto en un ambiente controlado y detectar conflictos e incompatibilidades. |
| Release Build | Equipo de pruebas y destinatarios de la entrega. | Cuando se prepara una versión distribuible. | Identificar, construir y empaquetar lo que se entregará. |

**Private System Build:** actualizar el workspace, integrar cambios recientes, resolver conflictos, construir y ejecutar las pruebas pertinentes. Reduce la posibilidad de interrumpir a otros con un cambio inconsistente.

**Integration Build:** integra el trabajo de distintos desarrolladores y verifica que el conjunto sea consistente. Puede combinar una ejecución rápida por cambio con verificaciones más extensas en otra cadencia. El resultado ofrece una referencia compartida y evita una integración masiva al final.

**Release Build:** identifica la versión, obtiene los componentes correctos, construye, verifica según la política, empaqueta y registra resultados. La diferencia principal es que el resultado debe estar preparado e identificado para distribución.

Los tres deben compartir, en lo posible, el mismo mecanismo de construcción parametrizado. Mantener procedimientos totalmente diferentes favorece el problema «en mi máquina funciona».

### 7.5. Automatización, reproducibilidad y equilibrio

Los scripts hacen explícitos y repetibles los pasos. Reducen olvidos y pueden actuar como documentación ejecutable. Deben mantenerse junto con el producto.

Para mejorar el proceso de build, el PDF propone cuidar dependencias, modularidad, estructura de construcción, herramientas y recursos de hardware. Un build demasiado lento desalienta su ejecución frecuente. Uno rápido pero insuficiente deja pasar problemas. Por eso se combinan comprobaciones rápidas y otras de mayor alcance.

El proceso de release debe ejercitarse temprano. Descubrir al final que no se sabe empaquetar o instalar el producto introduce un riesgo que podría haberse detectado antes.

### 7.6. Integración continua — CI

**Complemento conceptual:** CI es integrar cambios pequeños y frecuentes en una línea compartida y verificar cada integración mediante construcción y pruebas automatizadas. Un servidor de automatización ayuda, pero no basta si cada persona mantiene su código aislado durante semanas.

Se requiere versionado, feedback visible y rápido, un build automatizado y atención inmediata a sus fallas. Ante una integración rota, se identifica el cambio y se corrige o revierte de manera controlada para recuperar una base confiable.

La ventaja principal es detectar incompatibilidades pronto, cuando hay menos cambios que investigar. [Referencia: Martin Fowler, Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html).

### 7.7. Entrega continua y despliegue continuo

**Complemento conceptual:**

| Práctica | Qué sostiene | Paso a producción |
|---|---|---|
| Integración continua | Cambios integrados y comprobados frecuentemente. | No implica por sí sola desplegar. |
| Entrega continua — Continuous Delivery | Software preparado para poder desplegarse de manera confiable cuando se decida. | Puede requerir una decisión o aprobación. |
| Despliegue continuo — Continuous Deployment | Paso automático a producción de los cambios que superan los controles definidos. | Se automatiza también esa decisión operativa por cambio. |

La entrega continua amplía el trabajo desde integración hacia preparación y verificación para producción. El despliegue continuo presupone esa capacidad. [Referencia: Martin Fowler, Continuous Delivery](https://martinfowler.com/bliki/ContinuousDelivery.html).

**Ejemplo didáctico de pipeline:** cambio versionado → build → pruebas rápidas → integración → pruebas de mayor alcance → artefacto identificado → ambiente de preproducción → producción según la política. Es una secuencia posible, no un estándar obligatorio de la cátedra.

### 7.8. Pruebas continuas, colaboración y límites

Las pruebas automatizadas repetibles aportan confianza a cada cambio. Las revisiones detectan problemas antes de ejecutar y las exploratorias aportan preguntas nuevas. Ninguna práctica reemplaza a todas las demás.

La colaboración entre desarrollo, pruebas y operación ayuda a que construir, instalar y mantener no sean problemas aislados. Como ampliación, este enfoque suele asociarse con DevOps; no hay un desarrollo autónomo extenso de DevOps en los archivos base.

Beneficios: feedback temprano, menor integración acumulada, mejor trazabilidad, menor esfuerzo manual repetitivo y entregas más previsibles. Costos: preparar ambientes, escribir y mantener pruebas, cuidar scripts y atender fallas. Una automatización mal mantenida puede producir resultados engañosos o frecuentes falsas alarmas.

<a id="tdd"></a>
## 8. TDD, ATDD y refactoring

### 8.1. Qué es TDD

Test-Driven Development combina **escribir primero una prueba** y **refactorizar**. Las pruebas, generalmente unitarias, orientan el desarrollo en ciclos pequeños.

Escribir pruebas después del código puede ser útil, pero no constituye por sí mismo TDD. La diferencia es que la prueba expresa primero el comportamiento esperado y guía lo que se implementa.

### 8.2. Red → Green → Refactor

1. **Red:** escribir una prueba pequeña que falla por el comportamiento todavía ausente. Verificar el motivo de la falla.
2. **Green:** escribir el código mínimo suficiente para pasar esa prueba y mantener pasando las anteriores.
3. **Refactor:** mejorar el diseño interno conservando el comportamiento observable y las pruebas en verde.

El material detalla escribir la prueba, hacerla compilar, observar el fallo, implementar el cambio, ejecutar y eliminar duplicaciones. Ver fallar primero la prueba ayuda a comprobar que efectivamente detecta la ausencia del comportamiento.

Las tres reglas presentadas son no escribir código de producción sin una prueba que falle, no escribir más prueba de la necesaria para obtener ese fallo y no escribir más código de producción del necesario para superarlo.

### 8.3. Ejemplo paso a paso

Queremos una función que calcule el precio de una reserva según horas y tarifa.

```text
Prueba 1: precio(2, 100) debe devolver 200.
Red: no existe el comportamiento o el resultado es incorrecto.
Green: implementación mínima que satisface la prueba.

Prueba 2: precio(3, 100) debe devolver 300.
Red: una solución que devolviera siempre 200 falla.
Green: generalizar mediante horas × tarifa.

Prueba 3: horas negativas deben rechazarse, si así lo define el requisito.
Red: el código actual devuelve un importe negativo.
Green: incorporar la validación.

Refactor: mejorar nombres, extraer una regla si hace falta y eliminar duplicación.
Volver a ejecutar las pruebas.
```

La regla para horas negativas se obtiene de requisitos o acuerdos. TDD no decide las reglas del negocio por sí mismo.

### 8.4. Patrones del material

| Patrón | Utilidad |
|---|---|
| One Step Test | Probar una porción mínima de comportamiento. |
| Starter Test | Elegir un primer caso que permita comenzar a explorar el diseño. |
| Explanation Test | Aclarar mediante un ejemplo la intención o una duda sobre el comportamiento. |
| Learning Test | Aprender y documentar cómo responde una API externa. |
| Another Test | Incorporar una variación relevante que aún no está cubierta. |
| Regression Test | Reproducir un defecto conocido para evitar que reaparezca. |
| Fake It | Usar temporalmente una solución mínima, incluso constante, para pasar una prueba. |
| Triangulación | Agregar ejemplos que obliguen a generalizar correctamente. |
| Obvious Implementation | Implementar directamente cuando la solución es clara. |
| One to Many | Extender del caso de un elemento al de varios. |
| Isolated Test | Evitar dependencia entre pruebas y su orden de ejecución. |
| Test List | Registrar los casos que falta desarrollar. |
| Test Data / Evident Data | Usar entradas y expectativas simples cuya relación sea comprensible. |

**AAA — Arrange, Act, Assert:** preparar contexto, ejecutar el comportamiento y comprobar el resultado. Ayuda a que la prueba sea legible y tenga una intención clara.

### 8.5. Refactoring

Refactorizar es transformar la estructura interna del software sin cambiar su comportamiento observable. Permite mejorar legibilidad, eliminar duplicación, reducir complejidad y facilitar futuras modificaciones.

Ejemplo: extraer una validación duplicada a una función común manteniendo las mismas entradas, salidas y efectos. Cambiar una regla de cancelación de 24 a 48 horas es una modificación funcional, aunque también se mejore el diseño.

Proceso sugerido: comenzar con pruebas pasando, identificar un problema de estructura, realizar un cambio pequeño y volver a ejecutar pruebas. Repetir gradualmente.

Las pruebas reducen el riesgo, pero no garantizan que todo cambio incorrecto sea detectado: esa capacidad depende de qué comportamientos comprueban.

### 8.6. Beneficios y límites de TDD

TDD favorece feedback rápido, diseño de interfaces desde su uso, componentes más cohesionados, menor acoplamiento, ejemplos ejecutables y refactorización con respaldo. Puede reducir costos de mantenimiento y facilitar integración frecuente.

Requiere práctica y mantenimiento de pruebas. No garantiza seguridad, ausencia de defectos ni cobertura total. Tampoco reemplaza pruebas de integración, aceptación, rendimiento o exploración.

### 8.7. ATDD y relación con BDD

**ATDD — Acceptance Test-Driven Development:** negocio, desarrollo y testing acuerdan ejemplos y pruebas de aceptación antes de implementar. Se aclara qué significa satisfacer una necesidad.

Ejemplo de escenario:

```text
Dado un socio habilitado y un turno disponible,
cuando confirma la reserva,
entonces el turno queda asignado a ese socio
y no puede reservarlo otro usuario para el mismo horario.
```

Luego se construye, se automatiza donde aporta valor y se verifica el comportamiento. TDD puede guiar el diseño de las unidades internas necesarias para cumplir ese escenario.

El material también menciona BDD: una forma de expresar comportamientos mediante ejemplos comprensibles para negocio y tecnología. Conviene distinguir el foco: TDD orienta el diseño mediante pruebas; ATDD acuerda aceptación colaborativamente; los escenarios de comportamiento facilitan un lenguaje compartido.

---

<a id="calidad"></a>
## 9. Conceptos generales de calidad

### 9.1. Definición y relatividad

La calidad reúne las características de un producto o servicio que le permiten satisfacer necesidades manifiestas e implícitas. Las manifiestas se expresan; las implícitas pueden darse por supuestas, como conservar datos correctamente o no mostrar información de otro usuario.

La calidad depende del contexto, de los interesados y del momento. Un producto adecuado para aprender a programar puede ser insuficiente para operar un servicio crítico. Un usuario puede priorizar facilidad de uso y el equipo de mantenimiento, capacidad de comprender y modificar el sistema.

Se deben considerar expectativas del cliente y del usuario, necesidades de la gerencia, desarrollo, mantenimiento y otros interesados. Si sus objetivos entran en conflicto, hay que acordar prioridades explícitas.

### 9.2. Perspectivas de calidad

- **Del usuario:** adecuación a sus necesidades y facilidad para alcanzar sus objetivos.
- **Del producto:** propiedades que pueden describirse y evaluarse, como fiabilidad o eficiencia.
- **De conformidad o manufactura:** cumplimiento de requisitos, especificaciones y estándares.
- **Basada en valor:** relación entre beneficios, costos y recursos necesarios.
- **Trascendental:** apreciación general de excelencia, más difícil de convertir en un criterio operativo.

Estas perspectivas explican por qué «es de calidad» necesita un contexto y evidencia. Para gestionar se deben traducir las expectativas relevantes a criterios evaluables.

### 9.3. Calidad necesaria, programada y realizada

El material presenta tres conjuntos:

- **Necesaria:** lo que el usuario y el negocio requieren.
- **Programada:** lo que se decide especificar y construir.
- **Realizada:** lo que efectivamente se obtiene.

La meta es que coincidan. Si se programa algo innecesario, hay riesgo de desperdicio. Si se necesita algo no programado, hay una omisión. Si se programa pero no se realiza, hay incumplimiento. Si se realiza una capacidad que nadie necesita, el esfuerzo puede no aportar valor.

Ejemplo: el usuario necesita impedir reservas duplicadas; el requisito no lo expresa; el código cumple esa especificación incompleta. Puede haber conformidad con lo programado y, al mismo tiempo, insatisfacción con la calidad necesaria.

### 9.4. Calidad de proceso, proyecto y producto

**Calidad de producto** se refiere a propiedades del resultado. **Calidad de proceso** se refiere a cómo se trabaja: claridad de actividades, responsabilidades, controles, medición y capacidad de mejora. La gestión del proyecto organiza recursos y compromisos para producir esos resultados.

Un proceso adecuado reduce variabilidad, hace visibles problemas y favorece mejores productos, pero no garantiza automáticamente que todos sean correctos. Hay que evaluar el producto además del proceso.

El apunte presenta al proceso como factor controlable de mejora. La idea útil es que la organización puede definir y mejorar su forma de trabajo. No debe interpretarse como si capacitación, tecnología o herramientas no pudieran modificarse.

### 9.5. Principios de calidad

1. La calidad se construye durante todo el ciclo de vida.
2. Es responsabilidad de todas las personas involucradas.
3. La capacitación y el compromiso gerencial sostienen las prácticas.
4. El liderazgo debe mostrar con hechos qué se prioriza.
5. La medición ayuda a controlar y mejorar, siempre que sea significativa.
6. Conviene comenzar por prácticas simples y apropiadas al negocio.
7. El aseguramiento debe planificarse y contar con recursos.
8. Probar más no mejora automáticamente el producto: hay que usar los resultados para corregir y prevenir.

### 9.6. Ventajas, costos y dificultades

| Trabajar con calidad permite… | Exige o puede presentar… |
|---|---|
| Detectar problemas antes de que se propaguen. | Inversión inicial en planificación, formación y herramientas. |
| Reducir retrabajo y fallas en producción. | Tiempo para revisar, probar y mantener automatización. |
| Mejorar confianza y satisfacción. | Cambios culturales y resistencia a nuevas prácticas. |
| Facilitar mantenimiento y evolución. | Acuerdos sobre criterios y responsabilidades. |
| Producir evidencia y trazabilidad. | Disciplina para conservar registros útiles. |
| Hacer más previsible la entrega. | Riesgo de burocracia si se agregan controles sin evaluar su utilidad. |

Las «desventajas» suelen ser costos de implementación o de una aplicación inadecuada. No justifican eliminar controles necesarios; invitan a diseñarlos de manera proporcional.

Como explicación complementaria, puede pensarse el costo de calidad en prevención, evaluación y fallas. La prevención incluye capacitación y diseño de prácticas; la evaluación, revisiones y pruebas; las fallas internas, correcciones antes de entregar; las externas, incidentes, reclamos y daños posteriores. Ahorrar en prevención puede aumentar mucho el costo de fallas.

<a id="sqa"></a>
## 10. Aseguramiento y planificación de la calidad

### 10.1. SQA y PPQA

**SQA — Software Quality Assurance:** conjunto de actividades planificadas para dar confianza en que procesos y productos cumplen los requisitos y estándares de calidad aplicables. Incluye definir prácticas, evaluar su aplicación, informar problemas y verificar que se atiendan.

**PPQA — Process and Product Quality Assurance:** enfatiza la evaluación objetiva de procesos y productos de trabajo. En el contexto CMMI de las diapositivas, es un área de proceso que da visibilidad sobre cumplimiento y no conformidades.

El aseguramiento se ocupa de prevenir y detectar problemas de forma sistemática. No equivale a un departamento que prueba el software al final.

### 10.2. Aseguramiento, planificación y control

| Actividad | Pregunta | Ejemplo |
|---|---|---|
| Aseguramiento | ¿Qué prácticas y estándares sostienen la calidad y cómo verificamos su aplicación? | Definir un proceso de revisión y auditar su cumplimiento. |
| Planificación de calidad | ¿Qué calidad necesitamos en este proyecto y cómo la evaluaremos? | Elegir atributos, revisiones, pruebas, responsables y criterios. |
| Control de calidad | ¿El proceso o producto evaluado cumple los criterios establecidos? | Ejecutar pruebas, revisar un documento, analizar mediciones. |

Los archivos usan «control de calidad» de manera amplia para incluir control del proceso y del producto. La diferencia útil para estudiar es **establecer y sostener el sistema de calidad** frente a **evaluar resultados concretos**, sin tratar sus actividades como compartimentos aislados.

### 10.3. Funciones de SQA

El material incluye evaluación de planificación del proyecto, requisitos, diseño, programación, integración y pruebas, planificación y control del proyecto, y adaptación de procedimientos al contexto.

Esto supone:

- Facilitar técnicas, herramientas, métodos y estándares.
- Evaluar si los planes contemplan actividades de calidad suficientes.
- Verificar aplicación de procedimientos y consistencia de productos.
- Identificar y registrar no conformidades.
- Comunicar resultados a las personas responsables y a la gerencia.
- Hacer seguimiento de las acciones hasta su resolución.

No todos los proyectos necesitan la misma formalidad. Adaptar debe ser una decisión explícita y razonada, no omitir actividades por presión sin evaluar sus consecuencias.

### 10.4. Grupo de Aseguramiento de Calidad — GAC

El material recomienda independencia de la administración del proyecto y acceso cercano a la gerencia. Su propósito es poder informar problemas aunque haya presión por cumplir fechas.

El GAC aporta una evaluación objetiva, pero no concentra toda la responsabilidad por la calidad. Desarrollo corrige productos; responsables del proceso mejoran prácticas; gerencia asigna recursos y resuelve conflictos; SQA verifica y comunica.

**Independencia** tampoco significa aislamiento: necesita colaboración y conocimiento del trabajo para evaluar de manera pertinente.

### 10.5. Estándares de producto y de proceso

- **De producto:** describen propiedades esperadas de los resultados. Ejemplos: estructura de documentación, convenciones de código o criterios de identificación de requisitos.
- **De proceso:** describen cómo realizar actividades. Ejemplos: procedimiento de revisión, control de cambios o gestión de defectos.

Pueden provenir de normas internacionales, acuerdos nacionales, políticas de la organización o decisiones del proyecto. Un estándar debe servir al objetivo de calidad y mantenerse actualizado.

### 10.6. Plan de calidad y PACS

Un plan de calidad establece los atributos importantes, criterios y métodos de evaluación. El **PACS**, Plan de Aseguramiento de Calidad de Software, concreta las actividades de aseguramiento del proyecto.

Como esquema de estudio, debería poder explicar:

1. Alcance del producto y del proceso al que se aplica.
2. Objetivos y atributos de calidad prioritarios.
3. Estándares, procedimientos y adaptaciones acordadas.
4. Responsables, independencia y canales de comunicación.
5. Revisiones, auditorías y relación con el plan de pruebas.
6. Recursos, herramientas y momentos de ejecución.
7. Evidencias y métricas que se conservarán.
8. Tratamiento, escalamiento y seguimiento de no conformidades.

El plan de pruebas desarrolla el trabajo específico de testing; el PACS tiene un alcance más amplio. No deben confundirse.

### 10.7. Mejora basada en resultados

Definir proceso → desarrollar producto → evaluar → analizar problemas → mejorar → volver a evaluar. Cuando una práctica demuestra utilidad, se incorpora al estándar de trabajo.

La corrección de un defecto elimina ese problema particular. Analizar por qué se introdujo y por qué no se detectó permite prevenir otros semejantes.

<a id="iso-producto"></a>
## 11. Modelos de calidad de producto e ISO

### 11.1. Para qué sirve un modelo

Un modelo organiza atributos de calidad para describirlos, priorizarlos y evaluarlos. Evita reducir «calidad» a que las funciones principales parezcan funcionar.

Permite transformar expresiones vagas como «debe ser rápido» en requisitos evaluables: qué operación, bajo qué carga, en qué ambiente y con qué tiempo máximo o percentil esperado.

### 11.2. ISO/IEC 25000 y distinción de modelos

Las diapositivas mencionan la familia **SQuaRE — ISO/IEC 25000**, el modelo de producto y calidad en uso de **ISO/IEC 25010:2011**, y calidad de datos en **ISO/IEC 25012:2008**.

**Aclaración importante:** el título «Modelo de Calidad de Producto (En uso)» del apunte mezcla conceptos. Las ocho características que enumera pertenecen al modelo de **calidad de producto** de 2011. La **calidad en uso** evalúa resultados de la interacción de usuarios con el sistema en un contexto.

Este resumen conserva la edición 2011 porque es la usada en clase. El catálogo ISO indica que fue reemplazada por normas posteriores; no se la presenta como edición vigente. [Fuente de la aclaración: ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html).

### 11.3. Las ocho características de producto del material

| Característica | Qué evalúa | Subcaracterísticas del apunte | Ejemplo |
|---|---|---|---|
| Adecuación funcional | Si ofrece las funciones necesarias, correctas y apropiadas. | Completitud, corrección, pertinencia funcional. | Reservar, cancelar y consultar de acuerdo con las reglas. |
| Eficiencia de desempeño | Relación entre rendimiento y recursos bajo ciertas condiciones. | Comportamiento temporal, utilización de recursos, capacidad. | Responder dentro del objetivo con la carga prevista. |
| Compatibilidad | Capacidad de convivir e intercambiar información. | Coexistencia, interoperabilidad. | Intercambiar correctamente datos con el sistema de pagos. |
| Usabilidad | Facilidad para reconocer su utilidad, aprender y operar. | Reconocimiento de adecuación, aprendizaje, operabilidad, protección frente a errores, estética, accesibilidad. | Un usuario entiende cómo cancelar y recibe una confirmación clara. |
| Fiabilidad | Capacidad de cumplir funciones de manera consistente. | Madurez, disponibilidad, tolerancia a fallos, recuperación. | Recuperarse de una interrupción sin perder reservas confirmadas. |
| Seguridad | Protección de información y acceso. | Confidencialidad, integridad, no repudio, autenticidad, responsabilidad o trazabilidad de acciones. | Un socio solo puede consultar sus propios datos. |
| Mantenibilidad | Facilidad y eficacia para analizar, modificar y probar. | Modularidad, reusabilidad, analizabilidad, modificabilidad, testabilidad. | Cambiar una regla sin afectar múltiples módulos innecesariamente. |
| Portabilidad | Capacidad de trasladarse entre entornos. | Adaptabilidad, instalabilidad, reemplazabilidad. | Instalar la aplicación en los ambientes previstos con pasos controlados. |

**Relaciones:** mejorar un atributo puede afectar otro. Ciertas medidas de seguridad agregan pasos de interacción; optimizaciones extremas pueden dificultar mantenimiento. La decisión debe considerar el contexto y el conjunto de atributos, no maximizar uno aisladamente.

### 11.4. Calidad en uso

Como complemento para distinguirla, el modelo de 2011 considera **efectividad, eficiencia, satisfacción, ausencia de riesgo y cobertura del contexto**. La efectividad se relaciona con lograr los objetivos; la eficiencia, con recursos usados para lograrlos; la satisfacción, con la experiencia; la ausencia de riesgo, con consecuencias adversas; la cobertura del contexto, con los entornos de uso considerados. [Fuente: definiciones ISO/IEC 25010:2011](https://www.iso.org/obp/ui/?_escaped_fragment_=iso%3Astd%3Aiso-iec%3A25010%3Aed-1%3Av1%3Aen).

Ejemplo propio: una operación puede responder rápidamente y, aun así, resultar incomprensible para usuarios nuevos. La medición técnica y el resultado de uso aportan evidencia diferente.

### 11.5. McCall y Barbacci/SEI

El modelo de **McCall** del material agrupa atributos según:

- **Operación:** corrección, fiabilidad, usabilidad, integridad y eficiencia.
- **Revisión:** mantenibilidad, flexibilidad y facilidad de prueba.
- **Transición:** portabilidad, reusabilidad e interoperabilidad.

La referencia a **Barbacci/SEI** enfatiza atributos como desempeño, seguridad y confiabilidad, y la diferencia entre optimización local y global. Un diseño debe considerar compromisos entre atributos: el mejor valor de uno no garantiza el mejor sistema completo.

### 11.6. Qué representa cada norma ISO mencionada

**Ampliación de los originales:** ISO es una organización que publica normas; «tener ISO» es una expresión imprecisa si no se identifica cuál y con qué alcance.

| Referencia | Enfoque |
|---|---|
| ISO 9000 | Fundamentos y vocabulario de gestión de la calidad. |
| ISO 9001 | Requisitos para un sistema de gestión de la calidad. |
| ISO/IEC/IEEE 90003 | Orientación para aplicar ISO 9001 al software. |
| ISO/IEC/IEEE 12207 | Procesos del ciclo de vida del software. |
| ISO/IEC 15504 — SPICE | Evaluación y mejora de capacidad de procesos en la familia histórica mencionada por el material. |
| ISO/IEC 25000 — SQuaRE | Requisitos y evaluación de calidad de sistemas y software. |
| ISO/IEC 25010:2011 | Modelos de calidad de producto y calidad en uso estudiados aquí. |
| ISO/IEC 25012:2008 | Modelo de calidad de datos citado en clase. |

ISO 9001 se aplica a un sistema de gestión dentro de un alcance; no equivale a certificar que cada aplicación no tiene defectos. ISO/IEC/IEEE 90003 orienta su aplicación a software sin agregar requisitos a ISO 9001. ISO/IEC/IEEE 12207 organiza procesos sin imponer por sí misma un ciclo de vida único. [Referencias: familia ISO 9000](https://www.iso.org/iso/es/selection_and_use_of_iso_9000_family_of_standards_2016_en.pdf), [ISO 90003](https://www.iso.org/standard/74348.html) e [ISO 12207](https://www.iso.org/standard/90219.html).

<a id="modelos-proceso"></a>
## 12. Mejora de procesos, CMMI, SPICE e IDEAL

### 12.1. Definir y mejorar un proceso

Un proceso es un conjunto organizado de actividades, métodos, prácticas y transformaciones que las personas usan para alcanzar un propósito. Para definirlo se deben aclarar entradas, salidas, participantes, responsabilidades, tareas, secuencia, criterios y recursos.

Un proceso indefinido depende excesivamente de memoria, interpretaciones individuales y acciones improvisadas. Definirlo permite repetir lo que funciona y aprender de lo que no.

La mejora requiere comprender el estado actual, establecer objetivos, elegir cambios, ensayarlos y medir resultados. Agregar documentos sin cambiar resultados no demuestra mejora.

### 12.2. CMMI: propósito y alcance del apunte

**Capability Maturity Model Integration** es un modelo de prácticas para evaluar y mejorar procesos. El material desarrolla principalmente la estructura histórica **CMMI-DEV v1.3** y también menciona otras versiones. Aquí se utiliza esa estructura para mantener coherencia con las áreas de proceso de clase.

CMMI no es una norma ISO. En el sentido usado en el curso, una organización es evaluada y obtiene un resultado para un alcance; esto no certifica la ausencia de defectos de sus productos.

En la estructura histórica aparecen:

- **CMMI-DEV:** desarrollo de productos y servicios.
- **CMMI-SVC:** prestación de servicios.
- **CMMI-ACQ:** adquisición y gestión de productos y servicios de proveedores.

Comparten prácticas, pero no tienen idéntico alcance. Que una organización cubra una no significa que todas sus actividades estén evaluadas bajo las otras.

### 12.3. Madurez y capacidad

| Representación | Unidad de atención | Utilidad |
|---|---|---|
| Por etapas | Conjunto de áreas en una unidad organizacional evaluada. | Establecer un nivel de madurez y una secuencia de mejora. |
| Continua | Cada área de proceso seleccionada. | Elegir prioridades y conocer perfiles de capacidad diferentes. |

**Madurez:** grado de institucionalización y gestión del conjunto de procesos dentro del alcance evaluado. **Capacidad:** grado en que un proceso particular se ejecuta y gestiona de manera adecuada.

Ejemplo: una organización puede elegir mejorar primero gestión de configuración y medición. En una representación continua importa el nivel de cada área, no una única calificación indiferenciada de todo el trabajo.

**Corrección de versión:** las diapositivas muestran seis niveles continuos de 0 a 5, pero también dicen trabajar con v1.3. El documento CMMI-DEV v1.3 define cuatro niveles de capacidad: **0 incompleto, 1 realizado, 2 administrado y 3 definido**. Los niveles de madurez por etapas permanecen del 1 al 5. No conviene memorizar ambas escalas como si fueran de la misma edición. [Fuente primaria: CMMI-DEV v1.3, sección Understanding Capability Levels](https://insights.sei.cmu.edu/documents/853/2010_005_001_15287.pdf).

### 12.4. Los cinco niveles de madurez

| Nivel | Nombre | Qué caracteriza el trabajo | Ejemplo explicativo |
|---|---|---|---|
| 1 | Inicial | Resultados impredecibles, reacción a problemas y dependencia de esfuerzos individuales. | Se llega a las fechas gracias a horas extra y personas clave, sin una forma estable de repetirlo. |
| 2 | Administrado | Planificación, seguimiento y control en los proyectos. | Cada proyecto gestiona compromisos, cambios, configuración y calidad. |
| 3 | Definido | Procesos organizacionales compartidos que los proyectos adaptan de manera controlada. | Los proyectos parten de un proceso estándar y aportan aprendizaje. |
| 4 | Cuantitativamente administrado | Uso de objetivos y técnicas cuantitativas para comprender y controlar variación. | Se analiza el comportamiento del proceso para prever si cumplirá sus objetivos. |
| 5 | Optimizado | Mejora sostenida, análisis causal e innovación alineada al negocio. | Se identifican causas comunes de defectos y se prueban mejoras con resultados medidos. |

**Distinciones claves:** nivel 2 gestiona proyectos; nivel 3 institucionaliza procesos a escala organizacional. Nivel 4 no es simplemente «tener números»: supone gestión cuantitativa del comportamiento. Nivel 5 utiliza esa base para mejorar continuamente.

### 12.5. Áreas de proceso CMMI-DEV v1.3 de las diapositivas

| Nivel | Áreas |
|---|---|
| 2 — Administrado | Gestión de requisitos; planificación del proyecto; monitoreo y control; acuerdos con proveedores; medición y análisis; PPQA; gestión de configuración. |
| 3 — Definido | Desarrollo de requisitos; solución técnica; integración del producto; verificación; validación; foco en procesos organizacionales; definición de procesos; capacitación; gestión integrada de proyectos; gestión de riesgos; análisis y resolución de decisiones. |
| 4 — Cuantitativamente administrado | Desempeño del proceso organizacional; gestión cuantitativa del proyecto. |
| 5 — Optimizado | Gestión del desempeño organizacional; análisis causal y resolución. |

Las áreas se agrupan también en gestión de proyectos, soporte, ingeniería y gestión de procesos. Lo importante es relacionarlas con actividades concretas, no solo reconocer siglas.

Ejemplo: identificar una versión pertenece a gestión de configuración; evaluar objetivamente cumplimiento se relaciona con PPQA; comprobar el producto contra la especificación se relaciona con verificación; comprobar que satisface el uso previsto, con validación.

### 12.6. CMMI y agilidad

El material contrapone un énfasis organizacional en procesos, predictibilidad y conocimiento explícito con un énfasis ágil en colaboración, adaptación y software funcionando. Son contrastes didácticos, no descripciones universales de las personas que trabajan en cada enfoque.

Ambos pueden planificar, medir, gestionar riesgos, mejorar y buscar alto desempeño. Es posible aportar evidencia de prácticas mediante backlogs, controles de versiones, resultados de pruebas, políticas, retrospectivas y registros de decisiones, siempre que cumplan el propósito requerido.

El problema aparece cuando se convierte CMMI en documentación sin utilidad o se interpreta agilidad como ausencia de disciplina. La compatibilidad exige diseñar prácticas apropiadas, no cambiarles solamente el nombre.

### 12.7. SPICE

**Complemento:** en los originales SPICE está apenas mencionado. Se relaciona con evaluación y mejora de procesos y con la familia histórica ISO/IEC 15504. El nombre se conoce como Software Process Improvement and Capability Determination; el apunte utiliza otra expansión de la sigla.

La evaluación considera dos dimensiones: **qué proceso se evalúa** y **qué capacidad demuestra**. Se obtiene un perfil basado en evidencias que puede orientar mejoras y comparaciones de alcance equivalente. La ficha de ISO/IEC 15504-2 indica seis niveles y señala su sustitución por normas de la familia ISO/IEC 33000. [Referencia: ISO/IEC 15504-2](https://www.iso.org/standard/37458.html).

En la escala histórica de SPICE, los niveles se estudian como:

| Nivel | Denominación | Idea para recordarlo |
|---|---|---|
| 0 | Incompleto | No logra adecuadamente su propósito. |
| 1 | Realizado | Logra el propósito del proceso. |
| 2 | Gestionado | Se planifica y controla su ejecución y sus productos. |
| 3 | Establecido | Se aplica un proceso definido. |
| 4 | Predecible | Se controla cuantitativamente su comportamiento. |
| 5 | En optimización | Se mejora de forma continua. |

Esta escala no debe confundirse con los cuatro niveles continuos de CMMI v1.3. El punto común es evaluar capacidad mediante evidencia; los modelos, requisitos y esquemas concretos no son intercambiables. [Referencia adicional de la escala histórica: estudio empírico sobre niveles SPICE](https://www.sciencedirect.com/science/article/abs/pii/S0950584904000825).

### 12.8. Modelo IDEAL

IDEAL organiza una iniciativa de mejora. Los apuntes presentan la última letra como Learning o Leveraging; el sentido de estudio es aprender de la experiencia y aprovecharla para continuar mejorando.

| Fase | Actividades | Ejemplo |
|---|---|---|
| Initiating — Iniciar | Reconocer necesidad, establecer contexto, patrocinio y responsables. | La gerencia acuerda reducir incidentes de las releases. |
| Diagnosing — Diagnosticar | Evaluar prácticas actuales, problemas y oportunidades. | Se detecta que faltan pruebas de integración y builds reproducibles. |
| Establishing — Establecer | Fijar prioridades, estrategia, objetivos y plan de acción. | Elegir un proyecto piloto y asignar tiempo para automatizar. |
| Acting — Actuar | Implementar, ensayar, medir y ajustar. | Ejecutar el nuevo proceso en varias iteraciones. |
| Learning — Aprender | Analizar resultados y lecciones, revisar el enfoque. | Comparar incidentes y tiempos, ajustar y extender lo que funciona. |

IDEAL es un ciclo de mejora; no es un nivel de madurez ni una técnica de testing.

### 12.9. Comparación de modelos y normas

| Referencia | Pregunta orientadora |
|---|---|
| CMMI | ¿Qué prácticas conviene institucionalizar y qué madurez o capacidad muestran nuestros procesos? |
| SPICE / ISO 15504 | ¿Qué capacidad demuestra cada proceso evaluado? |
| ISO 9001 | ¿El sistema de gestión cumple los requisitos aplicables de gestión de la calidad? |
| ISO 12207 | ¿Qué procesos del ciclo de vida necesitamos organizar? |
| ISO 25010:2011 | ¿Qué atributos de producto y resultados de uso debemos evaluar? |
| IDEAL | ¿Cómo organizar y aprender de una iniciativa de mejora? |

<a id="vv"></a>
## 13. Verificación y validación

### 13.1. Distinción esencial

**Verificación:** comprobar que un producto de trabajo satisface sus requisitos o especificaciones. Pregunta de estudio: «¿Estamos construyendo el producto correctamente?».

**Validación:** comprobar que responde a las necesidades y al uso previsto. Pregunta de estudio: «¿Estamos construyendo el producto correcto?».

Ejemplo: la especificación permite cancelar hasta una hora antes y el código lo cumple. Eso aporta evidencia de verificación. Si el club necesita 24 horas para reasignar el turno, el sistema puede no ser válido para su operación aunque cumpla la especificación escrita.

Ambas atraviesan el ciclo de vida. No conviene asociar automáticamente verificación solo con documentos y validación solo con ejecución: los objetivos de la evaluación determinan la distinción.

### 13.2. Productos de trabajo y actividades estáticas/dinámicas

Un producto de trabajo es la salida de una actividad: requisitos, diseños, código, planes, casos de prueba o documentación.

- **Evaluación estática:** examina un artefacto sin ejecutar el software. Revisiones, inspecciones y análisis estático pueden detectar omisiones, ambigüedades, inconsistencias y defectos de código.
- **Evaluación dinámica:** observa el comportamiento al ejecutar. Permite evaluar resultados reales en condiciones seleccionadas.

Las revisiones técnicas y las pruebas dinámicas son complementarias. Se puede revisar una especificación incompleta antes de disponer de código y luego probar el producto integrado.

### 13.3. Prevención y detección temprana

Un requisito ambiguo puede producir un diseño incorrecto, código consistente con ese diseño y pruebas que repiten el mismo supuesto. Detectarlo temprano evita corregir todos esos productos posteriores.

Las curvas de costo de las diapositivas ilustran que el impacto suele crecer a medida que el problema se propaga. No hay que interpretar sus multiplicadores como una constante válida para todos los proyectos.

### 13.4. Diferencias de terminología entre apuntes

Para testing se usará:

- **Error:** acción o decisión humana equivocada.
- **Defecto:** imperfección introducida en un producto de trabajo.
- **Fallo o falla en ejecución:** comportamiento observado que no cumple lo esperado.

En el archivo de revisiones, «falla» se usa de forma más amplia como hallazgo en un producto; distingue «error» originado en el producto inspeccionado y «defecto» proveniente de un predecesor. Es una clasificación propia de ese material. En una respuesta conviene aclarar qué convención se está usando.

---

<a id="testing"></a>
## 14. Testing: fundamentos, proceso y planificación

### 14.1. Qué es y para qué sirve

El testing permite evaluar software y aportar información sobre su comportamiento, defectos, cumplimiento y riesgos. Incluye planificar, analizar, diseñar, preparar, ejecutar, evaluar y reportar, no solamente «usar la aplicación a ver qué pasa».

Las diapositivas enfatizan la actitud de buscar defectos: un caso útil puede demostrar que un supuesto era incorrecto. El material de testing ágil complementa esa visión con prevención, comprensión del negocio y construcción colaborativa de un mejor producto.

Una prueba que pasa también aporta evidencia sobre el comportamiento comprobado. No demuestra que todo el sistema sea correcto ni que no existan defectos fuera de esas condiciones.

### 14.2. Error, defecto y fallo: ejemplo causal

El analista interpreta equivocadamente una regla de edad (**error humano**). Se especifica que basta con tener 17 años cuando el requisito real exige 18 (**defecto en el requisito**). El código reproduce la regla y acepta a una persona de 17 (**fallo observado**).

Un defecto puede existir sin manifestarse en una ejecución: tal vez nunca se ingresó la condición que lo activa. También una falla puede depender de la combinación de código, datos, ambiente y secuencia de acciones.

### 14.3. Severidad y prioridad

**Severidad:** magnitud del impacto del defecto. **Prioridad:** urgencia u orden con que debe atenderse, considerando negocio, exposición, fechas y alternativas.

| Severidad del material | Ejemplo ilustrativo |
|---|---|
| Bloqueante | No se puede iniciar el sistema o continuar una actividad esencial. |
| Crítica | Pérdida importante de datos o acceso indebido grave. |
| Mayor | Una función relevante produce resultados incorrectos. |
| Menor | Problema acotado que no impide el objetivo principal. |
| Cosmética | Defecto visual o de texto de impacto limitado. |

El material usa prioridad urgente, alta, media y baja. Las escalas concretas deben acordarse.

Ejemplo de diferencia: un error visible en el nombre del producto puede tener baja severidad técnica y alta prioridad antes de una presentación. Un defecto grave en una función rara sigue siendo grave, aunque su prioridad dependa de exposición y mitigaciones. No hay una equivalencia automática entre ambas escalas.

### 14.4. Principios de testing

1. **Las pruebas muestran presencia de defectos, no su ausencia absoluta.** Que no fallen los casos seleccionados no cubre todos los posibles.
2. **Las pruebas exhaustivas suelen ser inviables.** La combinación de entradas, estados, secuencias y ambientes crece rápidamente.
3. **Conviene comenzar temprano.** Analizar y revisar requisitos permite prevenir errores antes de programar.
4. **Los defectos tienden a agruparse.** Algunos componentes concentran más problemas y merecen atención basada en evidencia.
5. **Repetir siempre las mismas pruebas tiene límites.** La «paradoja del pesticida» recuerda que hay que revisar y ampliar casos. La regresión sigue siendo útil, pero no reemplaza nuevas preguntas.
6. **El contexto importa.** Cambian riesgos, técnicas y profundidad según el producto.
7. **Ausencia de defectos detectados no equivale a utilidad.** El sistema puede cumplir sus pruebas y no satisfacer la necesidad.

El desarrollador debe probar su código, pero conviene complementar su perspectiva con otras personas y técnicas. La recomendación del apunte de no probar exclusivamente el propio código apunta a evitar sesgos, no a quitar responsabilidad al desarrollador.

### 14.5. Cuánto testing es suficiente

Se decide considerando riesgos, criticidad, objetivos, cobertura, defectos conocidos y recursos. Una fecha agotada no demuestra calidad; obliga a comunicar el riesgo pendiente y tomar una decisión informada.

Los apuntes ilustran el crecimiento del esfuerzo con muchas pantallas y entradas. Para comprenderlo mejor: diez campos con cien valores posibles cada uno generan `100^10` combinaciones de entradas si se consideran todas las combinaciones, sin contar estados ni secuencias. Es inviable enumerarlas indiscriminadamente.

Se priorizan situaciones de mayor impacto y probabilidad, clases representativas, límites e interacciones relevantes.

### 14.6. Proceso de pruebas

| Etapa | Qué se realiza | Resultados típicos |
|---|---|---|
| Planificación y control | Definir objetivos, alcance, riesgos, recursos, estrategia y seguimiento. | Plan, cronograma, criterios y ajustes. |
| Análisis y diseño / identificación y especificación | Examinar la base de prueba, identificar condiciones y diseñar casos y datos. | Casos, datos, cobertura y trazabilidad. |
| Preparación y ejecución | Preparar ambiente y versión, ejecutar, comparar y registrar. | Resultados y reportes de defectos. |
| Evaluación y reportes | Evaluar criterios de salida, cobertura y riesgos; comunicar conclusiones. | Informe de pruebas y recomendación. |

Las denominaciones varían levemente entre archivos. Las actividades son iterativas: un defecto puede exigir nuevos casos y un cambio de requisitos puede modificar el plan.

### 14.7. Planificación de pruebas: desarrollo práctico

La siguiente estructura amplía las indicaciones de los apuntes para poder explicar cómo planificar:

1. **Objetivo:** qué información y confianza se necesita obtener.
2. **Objeto y alcance:** funciones, interfaces, atributos y versiones incluidas; exclusiones justificadas.
3. **Base de prueba:** requisitos, historias, criterios de aceptación, diseños, riesgos y estándares aplicables.
4. **Estrategia:** niveles, tipos, técnicas, automatización y prioridad basada en riesgo.
5. **Ambientes y datos:** configuraciones, dependencias, permisos y preparación de datos.
6. **Recursos y responsabilidades:** quién diseña, prepara, ejecuta, analiza y decide.
7. **Calendario y dependencias:** cuándo estarán disponibles versión, ambiente y datos.
8. **Criterios de entrada:** condiciones necesarias para comenzar una actividad de pruebas.
9. **Criterios de salida:** condiciones que permiten concluirla y evaluar la entrega.
10. **Gestión de defectos y evidencias:** registro, clasificación, seguimiento y reportes.
11. **Riesgos y contingencias:** qué hacer si falta un ambiente, una dependencia falla o cambia el alcance.

**Ejemplo de entrada:** versión identificada, ambiente preparado, datos cargados y smoke test satisfactorio.

**Ejemplo de salida:** escenarios críticos ejecutados con resultado satisfactorio, ausencia de defectos bloqueantes abiertos, cobertura acordada alcanzada y riesgos residuales comunicados. Estos criterios son ilustrativos y se acuerdan para cada proyecto.

No confundir **criterios de aceptación de una historia** con **criterios de salida de una campaña de pruebas**: los primeros especifican comportamiento; los segundos regulan la finalización del trabajo de evaluación.

### 14.8. Casos de prueba y trazabilidad

Un caso de prueba debe indicar, como mínimo, qué se comprueba, bajo qué entradas y condiciones, y cuál es el resultado esperado. Para ejecutarlo y repetirlo conviene añadir identificador, pasos, precondiciones, versión y resultado observado.

| Campo | Ejemplo |
|---|---|
| ID | CP-RES-01. |
| Objetivo | Impedir dos reservas activas para el mismo turno. |
| Precondición | El turno ya está confirmado para un socio. |
| Entrada | Otro socio intenta reservar ese mismo turno. |
| Pasos | Iniciar sesión, seleccionar turno e intentar confirmar. |
| Resultado esperado | Rechazo claro y conservación de una única reserva activa. |
| Evidencia | Respuesta, registro de operación y estado final de datos. |

El **resultado esperado** debe provenir de una base confiable. Comparar con «lo que el programa hizo» sin un criterio previo no permite decidir si es correcto.

La **trazabilidad** conecta requisitos con diseño, implementación, pruebas y resultados. Una matriz puede mostrar qué requisito carece de pruebas, qué casos se afectan por un cambio o qué evidencia respalda su cumplimiento.

### 14.9. Reporte y seguimiento de defectos

Un reporte útil incluye identificador, título preciso, versión, ambiente, precondiciones, pasos reproducibles, esperado frente a observado, evidencia, severidad, prioridad y estado.

Ejemplo de título útil: «Se confirma una segunda reserva sobre un turno ocupado». «No funciona» no da suficiente información.

Un flujo ilustrativo es: registrado → analizado → asignado → corregido → verificado → cerrado. También puede haber duplicado, rechazado con justificación o diferido con riesgo conocido.

La corrección debe ser comprobada. Cerrar un defecto porque alguien modificó código no aporta la misma evidencia que repetir el caso y ejecutar la regresión pertinente.

### 14.10. Modelo en V

El modelo relaciona productos de definición con niveles de prueba:

| Base de definición | Evaluación asociada |
|---|---|
| Necesidades o requisitos de negocio | Aceptación. |
| Requisitos del sistema/software | Pruebas de sistema. |
| Diseño general y relaciones entre componentes | Integración. |
| Diseño detallado e implementación de unidades | Pruebas de componente o unitarias. |

Su enseñanza central es preparar las evaluaciones desde que se define el producto. No hay que esperar al final para pensar cómo se comprobará un requisito.

<a id="niveles"></a>
## 15. Niveles, tipos y ambientes de prueba

### 15.1. Niveles

El nivel indica **qué alcance del sistema se prueba**.

| Nivel | Objeto | Problemas típicos | Ejemplo |
|---|---|---|---|
| Unitario o componente | Una unidad delimitada, como una función, clase o módulo. | Reglas locales, cálculos, condiciones y manejo de errores. | Calcular el importe de una reserva. |
| Integración | Interacciones entre componentes o sistemas. | Formatos, contratos, datos, secuencia y comunicación. | Verificar que el servicio guarda correctamente en la base. |
| Sistema | El sistema integrado. | Incumplimientos funcionales y atributos globales. | Completar reserva, pago y confirmación. |
| Aceptación | Adecuación al uso y criterios acordados. | Diferencias entre lo construido y lo necesario. | Usuarios validan que pueden operar las reservas del club. |

**Unitarias:** suelen ser rápidas y permitir localizar errores. Pueden usar dobles para controlar dependencias. Que todas pasen no implica que las partes se entiendan correctamente al integrarse.

**Integración:** puede realizarse progresivamente. En **top-down** se comienza por componentes de mayor nivel y pueden simularse los inferiores. En **bottom-up** se integran primero los inferiores y pueden usarse controladores para invocarlos. Como vocabulario complementario, un *stub* reemplaza una dependencia llamada y un *driver* invoca al componente bajo prueba. La integración completa de una sola vez dificulta aislar causas.

**Sistema:** necesita un entorno representativo y considera requisitos funcionales y no funcionales. Incluye comportamiento ante fallos, seguridad, rendimiento y recuperación según alcance.

**Aceptación:** busca confianza en la adecuación al uso. Participan usuarios, representantes o responsables de aceptación. Las pruebas alfa se realizan en un entorno controlado; las beta incorporan usuarios en condiciones reales o más cercanas al uso final, según el contexto.

### 15.2. Tipos de pruebas

El tipo indica **qué característica o propósito se evalúa**. Los tipos no son niveles y pueden aplicarse en varios niveles.

**Funcionales:** comprueban qué hace el sistema: reglas, cálculos, procesos e interacciones exigidas. Ejemplo: una reserva cancelada dentro del plazo habilita reintegro.

**No funcionales:** comprueban cómo se comporta y con qué calidad:

| Tipo | Pregunta | Ejemplo |
|---|---|---|
| Rendimiento | ¿Qué tiempos y recursos necesita bajo condiciones definidas? | Tiempo de respuesta al consultar turnos. |
| Carga | ¿Cómo responde ante una cantidad prevista de actividad? | Muchos usuarios consultando y reservando simultáneamente. |
| Estrés | ¿Qué ocurre al superar límites o reducir recursos? | Saturar solicitudes y evaluar degradación y recuperación. |
| Volumen | ¿Qué sucede con grandes cantidades de datos? | Consultar un historial de millones de reservas. |
| Usabilidad | ¿Los usuarios pueden comprender y realizar sus tareas? | Encontrar y cancelar una reserva sin asistencia. |
| Seguridad | ¿Protege acceso, datos y acciones? | Impedir consulta de reservas ajenas. |
| Recuperación | ¿Puede restablecerse después de una interrupción? | Reiniciar sin perder confirmaciones ya persistidas. |
| Instalación | ¿Se instala, actualiza o desinstala según lo esperado? | Actualizar una versión conservando datos. |
| Portabilidad | ¿Funciona en los entornos requeridos? | Verificar ambientes o plataformas soportados. |
| Mantenibilidad/testabilidad | ¿Puede analizarse, modificarse y evaluarse con esfuerzo razonable? | Identificar dependencias y ejecutar pruebas aisladas. |

Algunos atributos, como mantenibilidad, también se evalúan mediante revisión y análisis estático. No todos se comprueban exclusivamente ejecutando casos de interfaz.

### 15.3. Smoke, confirmación y regresión

- **Smoke test:** comprobación breve de funciones esenciales para saber si tiene sentido continuar con pruebas más profundas. Si no inicia la aplicación, no conviene ejecutar cientos de casos de detalle.
- **Confirmación o retest:** repetir la prueba que evidenció un defecto para comprobar que fue corregido.
- **Regresión:** comprobar que un cambio no dañó comportamientos existentes, incluso en otras partes relacionadas.

Ejemplo: se corrige un reintegro. El retest comprueba el reintegro reportado; la regresión evalúa además cancelaciones, pagos y otros caminos que el cambio podría afectar.

El apunte describe una regresión total al cambiar de versión. Para comprender la práctica, la cobertura de regresión puede ser total o seleccionada según riesgo e impacto; su objetivo es detectar efectos no deseados. No debe confundirse «volver a probar el bug» con toda la regresión.

Un **ciclo de pruebas** agrupa ejecuciones sobre una versión identificada. Al cambiar de versión se deben conservar los resultados anteriores y saber cuáles corresponden a cada una.

### 15.4. Ambientes

| Ambiente | Uso |
|---|---|
| Desarrollo | Construcción y comprobaciones durante la implementación. |
| Prueba | Evaluación controlada con versiones y datos identificados. |
| Preproducción | Comprobaciones en condiciones similares a producción. |
| Producción | Servicio real a usuarios. |

Las diferencias de configuración, dependencias y datos pueden explicar fallas que no aparecen localmente. La representatividad del ambiente debe ser proporcional al objetivo de prueba. Separar ambientes ayuda a controlar cambios y resultados, pero sus nombres exactos varían entre organizaciones.

<a id="tecnicas"></a>
## 16. Técnicas de diseño de pruebas y ejercicios

### 16.1. Nivel, tipo y técnica: tres preguntas distintas

- Nivel: ¿qué parte o alcance del sistema se evalúa?
- Tipo: ¿qué propiedad o propósito se prueba?
- Técnica: ¿cómo se seleccionan y diseñan los casos?

Ejemplo: una prueba puede ser de **sistema**, de tipo **funcional** y diseñada mediante **valores límite**. Estas clasificaciones se complementan.

### 16.2. Caja negra

Diseña casos a partir del comportamiento esperado, requisitos o especificaciones sin depender de la estructura interna del código. Se eligen entradas y condiciones y se comparan salidas y efectos con lo esperado.

Es útil para verificar reglas y descubrir funcionalidad ausente o incorrecta. Su limitación es que puede dejar sin recorrer lógica interna relevante si el conjunto de casos es insuficiente.

### 16.3. Partición de equivalencias

Se divide el dominio de entradas en clases cuyos elementos deberían recibir un tratamiento equivalente. Se seleccionan representantes de clases válidas e inválidas.

Pasos:

1. Identificar condiciones y dominios: intervalos, valores discretos, opciones simples o múltiples.
2. Definir particiones válidas e inválidas.
3. Elegir representantes de cada partición.
4. Especificar resultados esperados.
5. Añadir interacciones relevantes que una prueba aislada por campo no cubra.

**Ejemplo resuelto:** el campo edad acepta enteros de 18 a 65, ambos inclusive.

| Clase | Representante | Resultado esperado |
|---|---|---|
| Entero menor que 18 | 16 | Rechazar. |
| Entero entre 18 y 65 | 35 | Aceptar. |
| Entero mayor que 65 | 70 | Rechazar. |
| Tipo de dato no admitido | `abc` | Rechazar con mensaje adecuado. |
| Valor ausente, si es obligatorio | Vacío | Informar obligatoriedad. |

La prueba con 35 representa la clase válida, pero puede no detectar que el código usa `< 65` cuando debía usar `≤ 65`. Para eso se complementa con valores límite.

Al probar entradas inválidas conviene aislarlas cuando sea necesario para saber qué validación falló. Varios errores simultáneos pueden ocultarse entre sí.

### 16.4. Análisis de valores límite

Selecciona casos en las fronteras de las clases y alrededor de ellas, donde suelen aparecer errores de comparaciones, índices y rangos.

Para enteros de 18 a 65, una selección de tres valores alrededor de cada borde es:

```text
17 → rechazar     18 → aceptar     19 → aceptar
64 → aceptar     65 → aceptar     66 → rechazar
```

Si el dominio permite decimales, «inmediatamente antes» debe definirse según la precisión admitida. No siempre corresponde restar o sumar 1.

Equivalencias reduce el dominio; límites profundiza en transiciones. Son técnicas relacionadas y complementarias.

### 16.5. Ejercicio de impuestos de las diapositivas

El enunciado presenta cuatro bandas: hasta 4000 sin impuesto; los siguientes 1500 al 10%; los próximos 2000 al 22%; montos superiores al 40%. La transcripción no resuelve los casos y su redacción mezcla «siguientes» con «sobre el total».

**Primero hay que detectar la ambigüedad:** no es lo mismo una tasa sobre todo el ingreso que un cálculo progresivo por tramos. En un proyecto real se aclara el requisito antes de fijar el resultado esperado. Aquí se explicitan dos interpretaciones para aprender la técnica; los importes son un ejercicio académico.

**Particiones de ingreso no negativo:**

| Clase | Rango | Representante | Tasa de la banda |
|---|---|---|---|
| A | 0 ≤ ingreso ≤ 4000 | 2000 | 0%. |
| B | 4000 < ingreso ≤ 5500 | 5000 | 10%. |
| C | 5500 < ingreso ≤ 7500 | 6500 | 22%. |
| D | ingreso > 7500 | 8000 | 40%. |

Se añaden clases inválidas según el contrato: ingresos negativos, vacío, texto o precisión no aceptada.

**Interpretación 1: tasa de la banda sobre todo el ingreso.** Para los representantes anteriores, los impuestos son 0, 500, 1430 y 3200. Hay saltos en las fronteras; la técnica debe exponerlos para que negocio confirme si son intencionales.

**Interpretación 2: tramos progresivos.** Para 5000: `(5000 − 4000) × 0,10 = 100`. Para 6500: `1500 × 0,10 + 1000 × 0,22 = 370`. Para 8000: `1500 × 0,10 + 2000 × 0,22 + 500 × 0,40 = 790`.

**Casos de valores límite, suponiendo enteros:** 3999, 4000, 4001; 5499, 5500, 5501; 7499, 7500, 7501. Para el límite inferior del dominio: −1, 0 y 1. Si se admiten centavos, usar incrementos de 0,01 en los bordes.

La selección de entradas puede ser similar en ambas interpretaciones; cambian los resultados esperados. Esta diferencia muestra por qué diseñar pruebas ayuda a descubrir defectos en los requisitos.

### 16.6. Caja blanca

Se basa en la estructura interna del código. Los casos se diseñan para recorrer sentencias, decisiones o caminos relevantes.

| Criterio | Qué busca |
|---|---|
| Cobertura de sentencias | Ejecutar las instrucciones consideradas. |
| Cobertura de decisiones/ramas | Ejercitar las salidas de las decisiones, como verdadero y falso. |
| Cobertura de caminos | Recorrer secuencias de ejecución seleccionadas; todos los caminos suelen ser inviables con ciclos y combinaciones. |

Ejemplo:

```text
si socio_habilitado:
    permitir_reserva()
mostrar_mensaje_final()
```

Con `socio_habilitado = verdadero` se ejecutan las sentencias mostradas. Sin embargo, falta comprobar el resultado falso de la decisión. Por eso 100% de sentencias no implica 100% de decisiones.

Una decisión compuesta, como `habilitado Y sin_deuda`, también puede necesitar combinaciones específicas para descubrir errores en sus condiciones. Conocer el código no reemplaza comprobar los requisitos: un comportamiento omitido no genera necesariamente una rama que se pueda cubrir.

### 16.7. Técnicas basadas en experiencia

**Adivinanza de defectos:** utilizar conocimiento del dominio y fallas habituales para diseñar casos. Ejemplos: valores vacíos, duplicados, doble clic, fechas invertidas, interrupción de una conexión o reintento de una operación.

**Testing exploratorio:** aprender sobre el producto, diseñar y ejecutar pruebas de manera integrada. La observación de un resultado orienta el siguiente caso.

Explorar no equivale a actuar sin propósito. Puede definirse una misión, un tiempo y un registro. Ejemplo: «Durante 30 minutos explorar cancelaciones alrededor del límite horario y registrar riesgos, casos y hallazgos».

### 16.8. Combinar técnicas

Para reservas se pueden usar equivalencias en duración, límites en horarios, caja blanca en validaciones, exploración en interrupciones y pruebas de integración para persistencia y pagos.

La elección depende de riesgo, información disponible y costo. Ninguna técnica aislada cubre todas las clases de problemas.

<a id="herramientas"></a>
## 17. Herramientas y automatización

### 17.1. Qué funciones cubren las herramientas

| Categoría | Para qué sirve | Evidencia que aporta |
|---|---|---|
| Gestión de casos y resultados | Organizar pruebas, ejecuciones y cobertura. | Qué se probó, en qué versión y con qué resultado. |
| Seguimiento de defectos | Registrar, clasificar y dar seguimiento. | Historial de hallazgos y correcciones. |
| Frameworks de pruebas | Ejecutar casos automatizados y comprobar expectativas. | Resultados repetibles. |
| Dobles de prueba | Controlar respuestas de dependencias para aislar comportamiento. | Verificaciones bajo condiciones preparadas. |
| Medición de cobertura | Identificar elementos recorridos o requisitos cubiertos. | Porcentajes y partes pendientes. |
| Análisis estático | Examinar código sin ejecutarlo. | Advertencias, posibles defectos y violaciones de reglas. |
| Pruebas de API, interfaz, carga o seguridad | Evaluar interacciones o atributos específicos. | Respuestas, tiempos, errores y hallazgos. |
| Integración y builds | Ejecutar comprobaciones al cambiar versiones. | Historial de construcciones y resultados. |
| Revisión colaborativa | Compartir cambios, comentarios y decisiones. | Evidencias de revisión y seguimiento. |

Los archivos mencionan JUnit, MSTest, SpecFlow y Moq, además de scripts Make/Ant en el PDF. Son ejemplos del material; no una lista obligatoria ni una recomendación sobre qué herramientas actuales elegir.

### 17.2. Qué conviene automatizar

Las pruebas repetitivas, con resultado esperado claro, comportamiento relativamente estable y alto valor de regresión suelen ser buenas candidatas. También conviene automatizar tareas mecánicas de preparación y construcción.

Automatizar tiene costos: diseño, datos, ambientes, mantenimiento y análisis de fallas. Si una prueba cambia constantemente o aporta poca información, su automatización puede no compensar.

La exploración, la evaluación contextual de usabilidad y el diseño de nuevas preguntas requieren juicio humano, aunque usen herramientas de apoyo.

### 17.3. Condiciones de una buena automatización

- Pruebas legibles, con propósito claro y verificaciones significativas.
- Datos y estados controlados para poder repetir resultados.
- Independencia suficiente para evitar fallas por orden de ejecución.
- Versionado junto con los cambios pertinentes del producto.
- Ejecución razonablemente rápida y reportes que faciliten investigar.
- Mantenimiento cuando cambia el comportamiento esperado.

Una prueba intermitente que falla sin cambios relevantes debilita la confianza. Ignorar sistemáticamente fallas de automatización hace perder su función de señal temprana.

### 17.4. Beneficios y límites

El material destaca rapidez, reutilización, cobertura, precisión, alcance y posible reducción de costos. Estos beneficios dependen de una implementación adecuada.

Una herramienta puede ejecutar mal una expectativa equivocada con gran velocidad. La calidad de la automatización depende de la calidad del diseño de pruebas y de la base usada para decidir qué es correcto.

---

<a id="revisiones"></a>
## 18. Revisiones técnicas

### 18.1. Definición y objetivos

Una revisión técnica examina un producto de trabajo para detectar defectos, inconsistencias o incumplimientos antes de que se propaguen. Es una actividad estática: no requiere ejecutar el programa.

Se pueden revisar requisitos, arquitectura, diseño, código, planes, casos de prueba y documentación, incluso cuando están incompletos. La revisión debe tener objetivos y alcance definidos para no convertirse en una conversación general sin resultados.

Sus ventajas son detección temprana, intercambio de conocimiento, consistencia y reducción de retrabajo. Sus dificultades incluyen tiempo de preparación, coordinación, capacitación y resistencia cultural.

### 18.2. Hallazgos y gravedad

El apunte diferencia:

- **Mayor:** puede ocasionar una falla operativa, resultado incorrecto o incumplimiento importante. Ejemplo: una regla de diseño permite dos reservas simultáneas sobre el mismo recurso.
- **Menor:** condición no deseable de menor impacto dentro del contexto de la clasificación. Ejemplo: una convención de documentación incumplida.
- **Cosmético:** detalle de presentación, ortografía o plantilla sin impacto significativo en el uso previsto.

La gravedad necesita contexto. Aunque las diapositivas incluyen «requisito no testeable» entre ejemplos menores, una ambigüedad que impida evaluar una función crítica puede requerir tratamiento mayor. La etiqueta no reemplaza el análisis del impacto.

### 18.3. Inspección y walkthrough

| Aspecto | Inspección | Walkthrough o recorrida |
|---|---|---|
| Propósito destacado | Detectar y registrar defectos sistemáticamente. | Comprender el producto, compartir conocimiento y detectar problemas. |
| Formalidad | Proceso definido y roles explícitos. | Menor formalidad en el material. |
| Preparación | Revisión individual previa. | Puede requerir menos preparación. |
| Conducción | Moderador y roles de apoyo. | Habitualmente el autor guía la explicación. |
| Herramientas | Checklists, registros, métricas y seguimiento. | Presentación, preguntas y anotaciones. |
| Resultado | Hallazgos y correcciones verificadas. | Comprensión compartida y problemas identificados. |

Una recorrida útil no reemplaza automáticamente una inspección exigida por el plan, porque tienen distinto grado de control y evidencia.

### 18.4. Roles de la inspección

- **Autor:** creó o mantiene el producto; explica contexto y realiza el retrabajo.
- **Moderador:** organiza, distribuye material, conduce la sesión, cuida el proceso y da seguimiento.
- **Lector:** recorre o presenta el contenido de forma sistemática.
- **Anotador:** registra los hallazgos y decisiones.
- **Inspector:** analiza previamente el material y aporta posibles defectos.

Las responsabilidades deben estar cubiertas, aunque en ciertos equipos una persona cumpla más de una función compatible. La elección de participantes depende del artefacto: para arquitectura interesa sumar diseño, requisitos y pruebas; para código, conocimiento técnico y del comportamiento esperado.

### 18.5. Proceso convencional de inspección

1. **Planificación:** elegir producto, versión, alcance, participantes, criterios y calendario.
2. **Visión general:** explicar contexto y propósito para que todos comprendan qué examinan.
3. **Preparación individual:** cada inspector estudia el material y registra hallazgos.
4. **Reunión:** consolidar defectos, aclarar y descartar falsos positivos; registrar resultados.
5. **Corrección:** el autor atiende los defectos fuera de la reunión.
6. **Seguimiento:** verificar correcciones, completar métricas y determinar si se cumplen los criterios o hace falta otra inspección.

La reunión se centra en encontrar y entender problemas. Resolver extensamente cada uno consume tiempo y desvía la revisión. Tampoco debe usarse para evaluar el desempeño personal.

El apunte dice que las inspecciones «no son para aprobar productos», pero también menciona una decisión al cierre. La distinción útil es que la reunión de detección no equivale a una autorización general de entrega: el seguimiento sí puede decidir si el artefacto cumple los criterios de salida de la inspección.

### 18.6. Recomendaciones de tamaño y duración del material

Las diapositivas proponen distribuir material con 48 horas de anticipación, reuniones de hasta dos horas y lotes pequeños: aproximadamente 250 líneas de código o 280 líneas de texto. También muestran tasas orientativas de preparación y revisión.

Son referencias del proceso convencional presentado, no límites universales. La complejidad, el lenguaje y el objetivo cambian la velocidad de revisión. La lección es evitar reuniones extensas y grandes paquetes imposibles de analizar con atención.

### 18.7. Checklists y herramientas

Un checklist orienta la atención hacia defectos relevantes. Debe adaptarse al tipo de producto y al historial del equipo.

Ejemplo para requisitos:

- ¿La necesidad y el actor están claros?
- ¿El requisito es coherente con los demás?
- ¿Tiene condiciones, entradas y resultados verificables?
- ¿Se contemplaron excepciones y restricciones?
- ¿Tiene identificación y trazabilidad?

Ejemplo para código:

- ¿Implementa el comportamiento esperado y maneja errores?
- ¿Existen límites, nulos o estados no considerados?
- ¿Es comprensible y mantiene las convenciones acordadas?
- ¿Las pruebas comprueban los riesgos del cambio?
- ¿Se introducen duplicación o dependencias innecesarias?

Herramientas de comparación de versiones, comentarios sobre cambios, registros de hallazgos y análisis estático ayudan a revisar. El análisis automático no reemplaza comprender intención y contexto.

### 18.8. Métricas de inspección

```text
Total de defectos = mayores + menores, según la clasificación adoptada
Densidad = defectos / tamaño inspeccionado
Esfuerzo = planificación + preparación + reunión + retrabajo
Esfuerzo por defecto = esfuerzo total / defectos encontrados
```

Ejemplo: en 200 líneas se encuentran 10 defectos y se invierten 5 horas-persona. La densidad es `10 / 200 = 0,05 defectos/LOC`, equivalente a 50 por cada 1000 líneas. El esfuerzo por defecto es `5 / 10 = 0,5 horas-persona`.

Se debe aclarar si el esfuerzo incluye seguimiento y si las notas cosméticas se cuentan. Sin una definición consistente, las comparaciones engañan. Si no se encuentran defectos, no corresponde dividir por cero ni concluir automáticamente que la inspección fue excelente o inútil.

### 18.9. Reglas de conducta

Revisar el producto y no a su autor; preparar antes; seguir una agenda; limitar discusiones; registrar hallazgos; capacitar a quienes participan; separar detección de solución y verificar el cierre.

La seguridad para señalar problemas ayuda a encontrar defectos. Una revisión usada como castigo favorece ocultamiento y reduce su utilidad.

<a id="auditorias"></a>
## 19. Auditorías de software

### 19.1. Definición

Una auditoría evalúa de manera objetiva e independiente productos o procesos para determinar su cumplimiento respecto de criterios: estándares, procedimientos, especificaciones y acuerdos aplicables.

Necesita tres elementos:

- **Criterio:** qué debería cumplirse.
- **Evidencia:** qué se observa o registra realmente.
- **Conclusión:** comparación fundamentada entre ambos.

Sin criterio definido, una preferencia personal del auditor no constituye una no conformidad. Sin evidencia suficiente, una afirmación del auditado no alcanza para concluir cumplimiento.

### 19.2. Por qué auditar

Las auditorías aportan una mirada independiente, visibilidad gerencial, detección de riesgos de insatisfacción y oportunidades de mejora. Permiten evaluar si los procesos organizacionales, del proyecto y de soporte realmente se implementan.

Tienen costo de preparación, entrevistas, revisión y seguimiento. Su valor depende de que los hallazgos se utilicen para corregir y mejorar, no de producir un informe extenso.

### 19.3. Auditoría de proyecto

Verifica el cumplimiento del proceso del proyecto y la consistencia de sus productos a medida que evolucionan. Se realiza según el PACS y debe tener responsables identificados.

Puede examinar:

- Existencia y actualización del plan, responsabilidades y recursos.
- Compromisos y aprobación de cambios.
- Requisitos identificados, revisados y controlados.
- Consistencia entre requisitos, diseño y código.
- Planes de verificación y validación que cubran los requisitos.
- Evidencias de revisiones, pruebas y gestión de configuración.

En el vocabulario del material, **ERS** es la especificación de requisitos de software y **DDS** el documento de diseño de software. Se verifica que el DDS responda a la ERS y que el código sea consistente con el diseño. La trazabilidad ayuda a seguir esas relaciones.

### 19.4. Auditoría de configuración funcional

Compara el producto construido y la evidencia disponible con los requisitos especificados. Busca determinar si las capacidades requeridas están implementadas y verificadas.

Preguntas útiles: ¿cada requisito tiene evidencia?, ¿la matriz de trazabilidad está actualizada?, ¿qué versión se probó?, ¿hay capacidades faltantes o cambios no autorizados?

La expresión del material «solo y completamente los requerimientos» apunta a cumplimiento e identificación del alcance; cualquier comportamiento adicional relevante debe analizarse respecto de requisitos y control de cambios.

### 19.5. Auditoría de configuración física

Compara la configuración construida con la documentación que la describe y con los elementos que se entregan. «Física» se refiere a correspondencia e identificación de componentes; no se limita a inspeccionar hardware.

Ejemplo: verificar que el paquete contiene los módulos previstos, que sus versiones coinciden con el registro, que las instrucciones de instalación corresponden y que la documentación representa el producto entregado.

El material exige atender las desviaciones antes de la entrega en este proceso. La auditoría debe dejar claro qué se verificó y qué correcciones faltan.

### 19.6. Auditorías al Grupo de Calidad

**Complemento desarrollado a partir de las responsabilidades de SQA y del proceso general de auditoría.** Los archivos no incluyen una exposición separada extensa, pero el tema está en el programa proporcionado.

El objeto es el propio **Grupo de Aseguramiento de Calidad** y la efectividad con que cumple sus responsabilidades. Se evalúa, por ejemplo:

- Si planifica y ejecuta las actividades de aseguramiento comprometidas.
- Si dispone de criterios, personal competente y recursos.
- Si conserva independencia y comunica problemas por los canales previstos.
- Si sus conclusiones se basan en evidencia objetiva.
- Si registra no conformidades y verifica su resolución.
- Si mantiene reportes, métricas y registros identificados.
- Si mejora sus prácticas a partir de resultados.

La evaluación debe evitar que el grupo se limite a aprobar su propio trabajo sin una mirada independiente. Puede realizarla una función independiente o personal calificado sin responsabilidad directa sobre las actividades examinadas, según la organización.

**Diferencia central:** auditar un proyecto pregunta si el proyecto cumple el proceso y sus compromisos; auditar al GAC pregunta si el aseguramiento de calidad se realiza de acuerdo con sus propios criterios y responsabilidades.

Ejemplo: el GAC afirma haber cerrado todas las desviaciones. La auditoría encuentra registros cerrados sin comprobación de las correcciones. El hallazgo se refiere al proceso de seguimiento del GAC, aunque las desviaciones originales pertenecieran a proyectos.

### 19.7. Roles y responsabilidades

| Rol | Responsabilidades del material |
|---|---|
| Gerente de SQA | Preparar plan de auditorías, calcular costos, asignar recursos y asegurar que las no conformidades se resuelvan. |
| Auditor | Acordar fecha y alcance, reunir y analizar evidencia, realizar la auditoría, informar y verificar seguimiento. |
| Auditado | Preparar información, participar, aportar evidencia, responder hallazgos, proponer y ejecutar acciones. |

El auditor no reemplaza al responsable de corregir. El auditado no cierra unilateralmente una desviación solo por declarar que la atendió: se necesita la verificación prevista.

### 19.8. Proceso completo de auditoría

#### A. Preparación y planificación

Definir objetivo, alcance, criterios, participantes, fecha, lugar, recursos y documentación. Revisar antecedentes y preparar preguntas.

El auditado reúne documentación y propone participantes. El auditor comprende el contexto y decide qué evidencia necesita. El plan debe evitar una evaluación indefinida que se extienda a cualquier tema sin acuerdo.

#### B. Ejecución: reunión de apertura

Presentar participantes, confirmar alcance y objetivo, revisar agenda, explicar dinámica y aclarar dudas. Se busca que todos sepan qué se evaluará y cómo se comunicarán resultados.

#### C. Ejecución: obtención de evidencia

Realizar preguntas, observar prácticas, revisar registros y completar el checklist. El auditado muestra evidencias y explica el trabajo.

La evidencia debe ser pertinente, identificable y suficiente para el alcance. Si se usa muestreo, las conclusiones deben reconocer sus límites. Un ejemplo correcto no demuestra automáticamente que todos los casos estén controlados.

#### D. Análisis de resultados

Revisar notas, documentos y respuestas; contrastar hallazgos con los criterios; verificar datos y preparar un informe preliminar. No hay que convertir un malentendido en una desviación sin corroborarlo.

#### E. Reunión de cierre

Presentar resultados preliminares, explicar evidencias y criterios, aclarar dudas y acordar próximos pasos y plazos. Acordar comprensión no significa negociar para ocultar un incumplimiento documentado.

#### F. Reporte final

Incorporar aclaraciones pertinentes, registrar el informe, conservar copia y comunicarlo. El reporte permite que otras personas comprendan qué se evaluó y qué acciones se requieren.

#### G. Seguimiento

El auditado analiza desviaciones, propone un plan con responsables y fechas y realiza las acciones. El auditor revisa el plan, verifica su cumplimiento y registra el cierre cuando corresponde.

Una acción realizada sin evidencia de resultado puede requerir comprobaciones adicionales. La auditoría no termina necesariamente con enviar el informe.

### 19.9. Técnicas y herramientas

- **Entrevistas:** comprender cómo se trabaja y solicitar ejemplos.
- **Checklists:** mantener cobertura de los criterios sin olvidar aspectos relevantes.
- **Muestreo:** seleccionar registros o productos cuando no es viable revisar todo.
- **Revisión de registros:** contrastar afirmaciones con evidencia conservada.
- **Herramientas automatizadas:** consultar versiones, historiales, pruebas y métricas.

Un checklist debería identificar auditoría, fecha, proyecto o proceso, fase, auditor, auditados y roles, objetivo, alcance y preguntas. Es una guía, no un reemplazo de la investigación.

Preguntas abiertas como «¿cómo se aprueban los cambios?» permiten comprender. Luego preguntas concretas como «¿dónde está la aprobación de este cambio?» verifican un caso. Conviene escuchar, tomar notas, reformular para confirmar comprensión y mantener un trato profesional.

### 19.10. Clasificación de resultados

| Resultado | Significado en el material | Tratamiento |
|---|---|---|
| Buena práctica | Desempeño destacable, superior a lo esperado y con resultados útiles. | Reconocer y analizar su posible reutilización. |
| Desviación o no conformidad | Incumplimiento de un criterio aplicable que afecta o introduce incertidumbre sobre el control o la calidad. | Requiere plan de acción y seguimiento. |
| Observación | Condición mejorable o riesgo potencial que no se registra como desviación en el esquema utilizado. | Comunicar para prevenir problemas futuros. |

**Aclaración:** si existe un requisito aplicable incumplido y evidencia clara, no corresponde rebajarlo a observación por comodidad. La clasificación debe seguir criterios acordados.

### 19.11. Cómo redactar un hallazgo

Un hallazgo sólido une **criterio + evidencia + diferencia**.

Ejemplo didáctico:

> El procedimiento de cambios exige aprobación previa a la incorporación en la release. En los cambios C-14 y C-18 de la versión 2.3 no se encontró el registro de aprobación exigido. No se pudo demostrar el cumplimiento del control previo para esos cambios.

Es más preciso que afirmar «el equipo trabaja mal». Describe el incumplimiento y permite investigar su causa.

Una **corrección** atiende el caso puntual. Una **acción correctiva** busca eliminar su causa para evitar repetición. Si faltaban revisiones, revisar los cambios pendientes es corrección; ajustar el flujo para exigir y conservar evidencia puede formar parte de la acción correctiva.

### 19.12. Reporte y métricas

El reporte incluye identificación, fecha, auditor, auditados, proyecto o proceso, fase si aplica, resultados, comentarios y solicitud de planes de acción. Es conveniente que cada resultado remita a su evidencia y criterio.

Métricas del material: esfuerzo, duración, cantidad de desviaciones y distribución por área de proceso. Pueden ayudar a identificar patrones y planificar recursos.

Pocas desviaciones pueden significar buen cumplimiento o una evaluación superficial. Muchas pueden significar problemas reales o mayor profundidad de revisión. La cantidad se interpreta con alcance, muestra y contexto.

<a id="testing-agil"></a>
## 20. Testing en ambientes ágiles

### 20.1. Cambio de enfoque

El testing ágil se integra con el descubrimiento, diseño y construcción. Se busca prevenir malentendidos, obtener feedback temprano y completar incrementos de calidad dentro de la iteración.

Las diapositivas contrastan el testing al final de un ciclo secuencial con una actividad continua. El modelo en V también enseña preparación temprana: el contraste no debe usarse para afirmar que toda práctica tradicional espera necesariamente al último día.

### 20.2. Manifiesto del testing

El material prioriza prevenir defectos, entender lo que se prueba, construir un mejor sistema y asumir responsabilidad de equipo por la calidad. Encontrar defectos sigue siendo necesario, pero se integra con comprensión y prevención.

Ejemplo: discutir antes de programar qué significa «cancelación gratuita» puede evitar varias implementaciones contradictorias y más pruebas correctivas después.

### 20.3. Los nueve principios explicados

1. **Adelantar testing:** participar desde requisitos e historias.
2. **Testing no es una fase aislada:** ocurre durante el trabajo del equipo.
3. **Todos contribuyen:** negocio aclara ejemplos, desarrollo prueba y testers aportan análisis especializado.
4. **Reducir latencia del feedback:** descubrir errores cerca del cambio que los introdujo.
5. **Las pruebas representan expectativas:** hacen observables los acuerdos.
6. **Mantener código limpio y corregir pronto:** evita acumular deuda y defectos.
7. **Reducir documentación innecesaria:** conservar evidencia útil y actualizada.
8. **Pruebas como parte de Done:** una historia no se completa dejando su evaluación para después.
9. **Avanzar hacia desarrollo guiado por pruebas:** usar expectativas para orientar implementación.

Reducir documentación no significa perder trazabilidad o reproducibilidad. La información necesaria puede estar en escenarios, código de pruebas, reportes y registros del trabajo.

### 20.4. Las seis prácticas concretas

1. Pruebas unitarias e integración automatizadas.
2. Regresión de sistema automatizada donde sea apropiado.
3. Pruebas exploratorias.
4. TDD.
5. ATDD.
6. Pruebas versionadas junto con el código.

Estas prácticas se refuerzan: TDD genera feedback local; integración detecta problemas entre piezas; regresión protege comportamientos; exploración busca riesgos nuevos; ATDD alinea expectativas; versionado mantiene correspondencia.

### 20.5. Rol del tester

Con el **Product Owner**, ayuda a precisar historias, ejemplos y criterios de aceptación. Con **desarrollo**, identifica dependencias, estrategias, riesgos y posibilidades de automatización. Con otros equipos que intervienen en integración, comunica escenarios, datos, ambientes y defectos.

También prepara y mantiene pruebas y datos, analiza resultados, registra defectos y aporta a evaluar Done. La mención de «System Team» en las diapositivas describe un contexto posible; no establece una responsabilidad obligatoria de Scrum.

La calidad compartida no elimina la especialización. El tester aporta una perspectiva que ayuda a cuestionar supuestos y descubrir riesgos que otras personas pueden no advertir.

### 20.6. Cuadrantes de testing ágil

Los cuadrantes clasifican pruebas por audiencia y propósito. No son fases secuenciales ni obligan a hacer primero Q1 y al final Q4.

| Cuadrante | Orientación | Propósito | Ejemplos del material |
|---|---|---|---|
| Q1 | Tecnología | Apoyar al equipo en la construcción. | Unitarias y componentes, normalmente automatizadas. |
| Q2 | Negocio | Apoyar al equipo aclarando expectativas. | Ejemplos, pruebas de historia, funcionales, prototipos y simulaciones. |
| Q3 | Negocio | Evaluar críticamente el producto. | Exploratorias, escenarios, usabilidad, aceptación de usuario, alfa y beta. |
| Q4 | Tecnología | Evaluar críticamente atributos técnicos. | Carga, rendimiento, seguridad y otros atributos de calidad. |

«Criticar» significa examinar el resultado para revelar problemas. «Apoyar» significa orientar decisiones de construcción y aportar feedback durante el desarrollo.

Ejemplo: una prueba de cálculo aislado ayuda en Q1; un escenario acordado de cancelación en Q2; observar a un usuario intentando cancelar aporta Q3; probar cientos de cancelaciones simultáneas puede aportar Q4.

### 20.7. Pirámide de pruebas

La pirámide propone muchas comprobaciones rápidas y enfocadas en niveles bajos, una cantidad intermedia a través de servicios o integraciones y menos pruebas completas de interfaz.

| Zona | Características |
|---|---|
| Base | Unitarias: rápidas, específicas y útiles para localizar problemas. |
| Medio | Servicios, API e integración: verifican reglas e interacciones con más alcance. |
| Cúspide | Flujos completos e interfaz: validan recorridos importantes, suelen ser más costosos y frágiles. |

El apunte muestra porcentajes orientativos de 80–90%, 5–15% y 1–5%. No deben sumarse como una distribución fija ni convertirse en una obligación para cualquier producto. La idea es equilibrar costo, velocidad y confianza según riesgos.

El **cono de helado** es el antipatrón de depender principalmente de pruebas lentas de interfaz, con poca base de verificaciones rápidas. Produce feedback tardío y fallas difíciles de localizar.

La diapositiva también ubica exploración manual cerca de la cúspide. Conceptualmente, la pirámide orienta especialmente la estrategia de automatización; no prescribe que el juicio humano o la exploración deban ocupar un porcentaje mínimo residual.

### 20.8. Testing dentro de un Sprint

Antes de seleccionar trabajo, se aclaran ejemplos y riesgos. Durante el Sprint se desarrollan pruebas y código, se revisa, integra y explora. Al considerar una historia terminada se comprueban criterios y DoD. En la Review se inspecciona el incremento con interesados. En la Retrospective se analiza cómo mejorar el trabajo.

Si todas las historias llegan a pruebas el último día, se forma una fase final dentro del Sprint y se pierde feedback temprano. Dividir historias, colaborar y limitar WIP ayuda a evitarlo.

### 20.9. Desafíos de adopción

El material menciona falta de formación, experiencias previas negativas, expectativas gerenciales y temor a perder identidad profesional. También aparecen dificultades para mantener ambientes, automatización y coordinación.

La respuesta combina capacitación, acuerdos, resultados visibles y mejora gradual. Cambiar nombres de reuniones sin integrar calidad en el trabajo no resuelve el problema.

---

<a id="caso"></a>
## 21. Caso integrador: sistema de reservas de un club

Este caso es una elaboración didáctica para relacionar todos los temas. El club recibe reservas por teléfono, tiene demoras y conflictos de horarios. Se propone un producto digital para consultar disponibilidad, reservar y cancelar.

### 21.1. Producto y aprendizaje

La hipótesis de valor es que los socios podrán gestionar reservas con menos esfuerzo y menos errores. Un MVP permite probar el flujo esencial con un grupo acotado. Se mide si logran completar reservas y si disminuyen conflictos.

La primera versión no necesita torneos, ranking, promociones y una red social. Sí necesita que la reserva confirmada sea confiable. Recortar alcance es compatible con mantener los atributos esenciales.

### 21.2. Lean y Kanban

El equipo observa trabajo de interfaz terminado que espera reglas de cancelación: es inventario y espera. También hay cambios continuos entre soporte y desarrollo, que agregan pérdida de contexto.

Se visualiza el flujo y se limita el WIP. Si pruebas está saturado, se colabora para finalizar historias. Se acuerdan criterios de ingreso a pruebas y una política de urgencias para incidentes reales.

Se mide una solicitud que tarda 12 días desde ingreso a entrega, con 8 días desde inicio y 3 de trabajo efectivo. Entonces:

```text
Lead time = 12 días
Cycle time = 8 días
Touch time = 3 días
Eficiencia de solicitud a entrega = 3 / 12 × 100 = 25%
Eficiencia dentro del ciclo = 3 / 8 × 100 = 37,5%
```

Los resultados orientan a investigar esperas. No indican automáticamente que alguien deba programar más rápido.

### 21.3. Planificación y métricas ágiles

El equipo define un objetivo: «Los socios pueden reservar un turno disponible sin intervención administrativa». Selecciona historias según capacidad, riesgos e información histórica.

Solo cuenta como terminada una historia que cumple DoD. Un formulario visible que no guarda ni confirma reservas no demuestra el cumplimiento del objetivo.

La velocidad orienta próximos Sprints; el RTF muestra funcionalidades que operan y están probadas. Las métricas de uso posterior permiten averiguar si el producto aporta el resultado buscado.

### 21.4. Prácticas continuas y TDD

La regla de precio se implementa con pruebas unitarias previas. Cada cambio se construye localmente y se integra con frecuencia. El build de integración ejecuta pruebas de las interacciones entre servicio, base y pagos.

Para entregar, se genera un paquete identificado con sus resultados. Si está listo para desplegarse cuando el club lo decida, ilustra entrega continua; si cada cambio aprobado por controles llega automáticamente a producción, ilustra despliegue continuo. [Referencia complementaria para esta aplicación y el repaso de CI/CD: documentación de AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/what-is-continuous-integration-and-continuous-deliverydeployment.html).

### 21.5. Calidad y planificación

Se priorizan adecuación funcional, fiabilidad, usabilidad y seguridad. «Ser confiable» se concreta en reglas observables, como conservar una única reserva confirmada por turno y recuperarse de una interrupción sin duplicar operaciones.

El PACS define revisiones, auditorías y responsabilidades. El plan de pruebas desarrolla escenarios, ambientes, datos, niveles, tipos y criterios de salida.

### 21.6. Revisiones y pruebas

Una revisión de requisitos detecta que «cancelar con anticipación» no especifica cuántas horas. Se aclara antes de programar.

Luego se combinan:

- Unitarias para reglas de precio y plazos.
- Integración para persistencia, notificaciones y pagos.
- Sistema para flujos completos.
- Aceptación con usuarios del club.
- Valores límite alrededor del plazo de cancelación.
- Pruebas concurrentes para dos solicitudes sobre un mismo turno.
- Pruebas de seguridad para reservas de otros usuarios.
- Exploración de interrupciones, reintentos y mensajes confusos.

Un sistema podría pasar pruebas secuenciales y fallar con dos reservas simultáneas. Esto muestra por qué los riesgos y las interacciones importan tanto como cubrir valores individuales.

### 21.7. Auditorías

La auditoría del proyecto comprueba el cumplimiento de revisiones y cambios. La funcional revisa evidencia de los requisitos. La física verifica correspondencia del paquete, versiones e instrucciones. La del GAC examina si el grupo ejecutó las evaluaciones previstas y verificó el cierre de desviaciones.

Se encuentra que una release se preparó sin evidencia de revisión exigida. Se registra criterio, evidencia y diferencia; se pide plan de acción y luego se verifica su cumplimiento.

### 21.8. Mejora del proceso

El análisis revela que se omitían revisiones cuando faltaba un revisor designado. La solución no se limita a revisar esa release: se asignan suplencias y se modifica el flujo para visibilizar pendientes.

Con IDEAL se inicia la mejora, se diagnostica, se planifica, se prueba y se aprende. CMMI o SPICE pueden orientar qué prácticas y capacidades conviene evaluar. Las métricas permiten saber si las omisiones disminuyen sin agregar demoras desproporcionadas.

<a id="comparaciones"></a>
## 22. Comparaciones y errores frecuentes

### 22.1. Diferencias que conviene explicar sin mirar

| Conceptos | Diferencia central |
|---|---|
| Calidad y testing | Calidad es un conjunto de propiedades y resultados; testing aporta evidencia sobre ellos. |
| Aseguramiento y control | Aseguramiento establece y sostiene confianza en prácticas; control evalúa cumplimiento concreto. |
| Plan de calidad y plan de pruebas | El primero abarca objetivos y evaluaciones de calidad; el segundo desarrolla testing. |
| Proceso y producto | Forma de trabajar frente a resultado construido. |
| Verificación y validación | Conformidad con especificación frente a adecuación a necesidades y uso. |
| Error, defecto y fallo | Acción humana equivocada, imperfección del artefacto y manifestación en ejecución. |
| Severidad y prioridad | Impacto frente a orden o urgencia de atención. |
| Nivel, tipo y técnica | Alcance evaluado, propiedad buscada y forma de diseñar casos. |
| Caja negra y caja blanca | Comportamiento especificado frente a estructura interna. |
| Equivalencias y límites | Representantes de clases frente a fronteras y vecinos. |
| Confirmación y regresión | Verificar una corrección frente a buscar efectos secundarios. |
| Smoke y prueba exhaustiva | Chequeo esencial inicial frente a todas las posibilidades, usualmente inviables. |
| Inspección y walkthrough | Revisión formal con preparación y seguimiento frente a recorrida guiada más informal. |
| Revisión técnica y auditoría | Defectos del artefacto frente a cumplimiento de criterios mediante evidencia; pueden compartir técnicas. |
| Auditoría funcional y física | Cumplimiento de requisitos frente a correspondencia de configuración y documentación. |
| Corrección y acción correctiva | Atender el caso frente a eliminar su causa para prevenir repetición. |
| Capacidad y velocidad ágil | Disponibilidad frente a cantidad estimada de trabajo terminado por iteración. |
| Esfuerzo y duración | Horas-persona frente a tiempo transcurrido. |
| Lead, cycle y touch time | Solicitud a entrega; inicio a fin; trabajo efectivo, bajo la convención del apunte. |
| WIP y throughput | Trabajo en curso frente a cantidad terminada por unidad de tiempo. |
| CI y entrega continua | Integrar y comprobar frente a sostener capacidad de desplegar. |
| Entrega y despliegue continuo | Estar listo para publicar por decisión frente a publicar automáticamente al superar controles. |
| TDD y pruebas posteriores | La expectativa guía el código frente a comprobarlo después de escribirlo. |
| TDD y ATDD | Diseño mediante pruebas de unidades frente a aceptación colaborativa basada en ejemplos. |
| Refactoring y cambio funcional | Modificar estructura interna conservando comportamiento frente a modificar comportamiento. |
| CMMI y SPICE | Modelos/esquemas distintos para mejora y evaluación de procesos; no intercambiar escalas. |
| Madurez y capacidad | Estado del conjunto de procesos en un alcance organizacional frente a un proceso particular. |
| ISO 9001 e ISO 25010 | Sistema de gestión frente a modelos de calidad del producto y uso en la edición estudiada. |
| MVP y MMP | Aprender sobre hipótesis frente a un producto mínimo comercializable. |
| Cuadrantes y pirámide | Propósito y audiencia de pruebas frente a distribución de verificaciones por nivel/costo. |

### 22.2. Afirmaciones engañosas y cómo corregirlas

| Afirmación | Explicación correcta |
|---|---|
| «Si pasa todas las pruebas, no tiene defectos». | Solo sabemos que satisfizo las comprobaciones ejecutadas bajo ciertas condiciones. |
| «La calidad es responsabilidad del tester». | Es de todo el equipo y la organización; testing aporta especialización. |
| «En Agile no se documenta ni se planifica». | Se conserva lo útil y se planifica/adapta con frecuencia. |
| «Un tablero con tarjetas ya es Kanban». | Faltan límites, políticas, gestión del flujo y feedback si no se aplican. |
| «Más WIP implica entregar más». | Puede aumentar colas y demoras; hay que atender capacidad y restricciones. |
| «Todos ocupados al máximo es el mejor sistema». | Puede empeorar el flujo y eliminar capacidad para resolver variaciones. |
| «Velocidad mayor demuestra más valor». | Los puntos no miden directamente utilidad o impacto en usuarios. |
| «Más cobertura demuestra pruebas perfectas». | Puede haber expectativas débiles y riesgos sin evaluar. |
| «TDD reemplaza todo el testing». | Se complementa con otros niveles, tipos y técnicas. |
| «Refactorizar permite cambiar reglas sin avisar». | Conserva comportamiento; modificar reglas es un cambio funcional. |
| «Instalar una herramienta crea CI». | Se necesita integrar frecuentemente, verificar y atender resultados. |
| «Toda norma ISO certifica productos». | Cada norma tiene su alcance; muchas orientan procesos, modelos o evaluación. |
| «Nivel 4 de CMMI es cualquier medición». | Requiere gestión cuantitativa del proceso, no solo recolectar datos. |
| «La auditoría termina al enviar el informe». | Debe hacerse el seguimiento requerido de las desviaciones. |
| «Inspeccionar es buscar culpables». | Se examina el producto y el proceso para aprender y corregir. |
| «Una observación sirve para ocultar un incumplimiento». | Un criterio incumplido con evidencia debe clasificarse según las reglas aplicables. |

### 22.3. Fórmulas de repaso

```text
Esfuerzo = suma del trabajo humano invertido
Capacidad = suma de disponibilidad efectiva en el período
Velocidad = suma de puntos de historias Done en la iteración

Lead time = instante de entrega − instante de solicitud
Cycle time = instante de finalización − instante de inicio
Touch time = tiempo de trabajo efectivo del ítem
Eficiencia (%) = Touch time / tiempo transcurrido elegido × 100

Densidad de defectos = defectos / tamaño definido
Cobertura (%) = elementos cubiertos / elementos considerados × 100
Esfuerzo por defecto = esfuerzo de inspección / defectos encontrados
```

En cualquier ejercicio, escribir unidad, alcance y supuestos. No mezclar días hábiles con calendario ni horas-persona con horas transcurridas. No calcular razones si el denominador es cero.

<a id="preguntas"></a>
## 23. Preguntas de parcial con respuestas guía

Las preguntas son de práctica y no constituyen un examen oficial. Una buena respuesta combina definición, propósito, aplicación y un ejemplo. Para estudiar, intentar responder primero sin mirar y después comparar.

### 23.1. Lean, Kanban y métricas

**1. ¿Qué significa eliminar desperdicio en software?**

Identificar trabajo o demoras que no aportan valor y reducirlos. Incluye funcionalidades innecesarias, trabajo parcialmente terminado, esperas, transferencias, cambios de contexto, defectos y talento desaprovechado. Algunos desperdicios son necesarios por restricciones actuales y se minimizan; los evitables se eliminan.

**2. ¿Por qué «ver el todo» puede cambiar una decisión de mejora?**

Porque acelerar una etapa no garantiza mejorar las entregas. Si pruebas es la restricción, aumentar producción de código puede agrandar su cola. Hay que evaluar el flujo completo y colaborar donde limita el resultado.

**3. Explique los siete principios Lean con un ejemplo común.**

En reservas: eliminar funciones innecesarias; aprender con usuarios; construir reglas coherentes; decidir arquitectura con evidencia suficiente; dar autonomía al equipo; optimizar desde solicitud hasta entrega; y liberar porciones pequeñas útiles. La explicación debe mostrar cómo cada principio contribuye al valor.

**4. ¿Qué diferencia a Kanban de un tablero de tareas?**

Kanban incluye visualización, límites WIP, gestión del flujo, políticas explícitas, feedback y mejora experimental. El tablero es la representación que ayuda a aplicar esas prácticas, pero no las sustituye.

**5. ¿Qué hace el equipo cuando una columna llega a su límite WIP?**

Evita incorporar trabajo que viole la política y busca terminar o desbloquear lo existente. Puede colaborar con la etapa saturada. Si necesita una excepción, debe estar regida por una política explícita; ignorar límites de forma habitual oculta el problema.

**6. Diferencie push y pull.**

Push envía trabajo hacia adelante según lo que produce una etapa, aunque la siguiente no tenga capacidad. Pull incorpora trabajo cuando hay capacidad y se cumplen condiciones acordadas. Pull ayuda a controlar acumulación y flujo.

**7. ¿Cuáles son las clases de servicio del material?**

Expreso, fecha fija, estándar e intangible. Se diferencian por urgencia y costo de demora, y necesitan reglas sobre selección, WIP y tratamiento. No basta con asignar un color.

**8. ¿Qué métricas caracterizan cada enfoque?**

Tradicional: esfuerzo, duración, costos, tamaño y defectos. Ágil: velocidad, capacidad y RTF. Lean: lead time, cycle time, touch time y eficiencia. Se distinguen por su énfasis, pero pueden combinarse según las preguntas del proyecto.

**9. Un ítem se solicita el día 2, empieza el 6 y se entrega el 14, con 3 días efectivos. Calcule sus métricas.**

Lead time: 12 días. Cycle time: 8 días. Touch time: 3 días. Eficiencia sobre lead time: 25%; sobre cycle time: 37,5%. Debe declararse qué intervalo se usa como denominador.

**10. ¿Por qué capacidad y velocidad no son intercambiables?**

La capacidad mide disponibilidad para trabajar; la velocidad refleja trabajo estimado completamente terminado en una iteración. Ausencias pueden afectar ambas, pero no hay conversión universal entre horas y puntos.

**11. ¿Qué significa RTF y qué evita?**

Running Tested Features: funcionalidades que funcionan y están probadas. Ayuda a no presentar código aislado o porcentajes subjetivos como si fueran producto utilizable.

**12. ¿Por qué una métrica puede producir efectos negativos?**

Si se convierte en un objetivo aislado, las personas pueden mejorar el número sin mejorar el resultado. Premiar líneas de código favorece volumen; premiar cantidad de bugs puede distorsionar detección y clasificación. Debe interpretarse junto con calidad y valor.

### 23.2. Producto y prácticas continuas

**13. ¿Qué diferencia hay entre entregar una funcionalidad y obtener un resultado?**

La funcionalidad es un output; el cambio conseguido para usuarios o negocio es un outcome. Un formulario nuevo puede existir sin reducir abandonos. Hay que observar el uso y contrastar la hipótesis de valor.

**14. ¿Qué es un MVP y por qué no significa «producto defectuoso»?**

Es el experimento mínimo adecuado para aprender sobre una hipótesis. Reduce alcance y esfuerzo, pero debe conservar las condiciones necesarias para que la evidencia sea válida y el uso resulte adecuado. Un alcance pequeño puede ser coherente y confiable.

**15. Explique los tres builds del PDF.**

El privado verifica cambios en el espacio del desarrollador; el de integración comprueba el trabajo conjunto; el de release prepara e identifica la versión distribuible. Cambian destinatario, alcance y frecuencia, aunque conviene compartir mecanismos de construcción.

**16. ¿Por qué automatizar un build?**

Para repetir pasos, reducir omisiones, identificar resultados y obtener feedback con frecuencia. Los scripts conservan conocimiento ejecutable. Deben mantenerse y ejecutarse en condiciones controladas; automatizar una secuencia incorrecta no la vuelve correcta.

**17. Diferencie CI, entrega continua y despliegue continuo.**

CI integra y verifica cambios frecuentes. Entrega continua mantiene capacidad de desplegar de forma confiable cuando se decide. Despliegue continuo automatiza el paso a producción de los cambios que superan los controles. Ninguno elimina la necesidad de calidad.

**18. ¿Cuál es el ciclo TDD y por qué debe verse fallar la prueba?**

Red, Green, Refactor. Primero falla una expectativa no satisfecha; después se implementa lo mínimo; finalmente se mejora estructura. Observar el fallo correcto aporta evidencia de que la prueba detecta la ausencia del comportamiento.

**19. ¿Qué diferencia hay entre TDD y ATDD?**

TDD guía el desarrollo mediante pruebas pequeñas, habitualmente unitarias. ATDD alinea expectativas de negocio mediante ejemplos y pruebas de aceptación acordadas antes de implementar. Pueden utilizarse juntas.

**20. ¿Cuándo un cambio es refactoring?**

Cuando modifica estructura interna conservando el comportamiento observable. Extraer duplicación puede ser refactoring; cambiar una tasa o un plazo de cancelación altera comportamiento y debe tratarse como cambio funcional.

### 23.3. Calidad y modelos

**21. ¿Por qué la calidad es relativa al contexto?**

Porque depende de necesidades, uso, riesgos e interesados. Lo adecuado para un prototipo puede ser insuficiente para una operación real. Se deben explicitar atributos y criterios prioritarios para evaluar, evitando una noción vaga de excelencia.

**22. ¿Qué representan calidad necesaria, programada y realizada?**

Necesaria es lo que se requiere; programada, lo que se especifica; realizada, lo que se obtiene. Diferencias entre ellas pueden generar omisiones, incumplimiento o desperdicio. La gestión busca alinearlas.

**23. ¿Por qué testing no puede asegurar por sí solo toda la calidad?**

Porque evalúa una selección de situaciones y no elimina automáticamente las causas de defectos. La calidad también depende de requisitos, diseño, prácticas, personas y mantenimiento. Sus resultados necesitan corrección y mejora.

**24. ¿Qué hace SQA y por qué necesita independencia?**

Establece y evalúa prácticas, verifica cumplimiento, comunica no conformidades y sigue su resolución. La independencia reduce conflictos cuando hay presión por fechas o costos. No implica que SQA sea el único responsable de la calidad.

**25. ¿Qué debería incluir un plan de calidad?**

Objetivos y atributos, alcance, estándares, adaptaciones, responsables, recursos, actividades de evaluación, evidencias y tratamiento de problemas. Debe explicar qué calidad se necesita y cómo se determinará si se alcanza.

**26. Nombre y ejemplifique las ocho características ISO 25010:2011 del material.**

Adecuación funcional, eficiencia de desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad. Ejemplos: regla correcta, respuesta rápida, intercambio con pagos, operación comprensible, recuperación, protección de datos, cambio sencillo e instalación en ambientes previstos.

**27. ¿Calidad de producto y calidad en uso son lo mismo?**

No. La primera describe propiedades del sistema; la segunda observa resultados de usuarios en un contexto. Un sistema con buen rendimiento técnico puede ser difícil de usar para su audiencia. Se necesitan evidencias de ambas perspectivas.

**28. ¿Cómo se diferencian CMMI, SPICE e ISO 9001?**

CMMI organiza prácticas de mejora y evaluación de madurez o capacidad. SPICE proporciona un enfoque de evaluación de capacidad de procesos. ISO 9001 establece requisitos de un sistema de gestión. No son certificados equivalentes sobre corrección del código.

**29. Explique los niveles de madurez de CMMI.**

Inicial: reactivo e impredecible. Administrado: proyectos planificados y controlados. Definido: procesos organizacionales adaptados a proyectos. Cuantitativamente administrado: comportamiento gestionado con técnicas cuantitativas. Optimizado: mejora continua basada en causas y resultados.

**30. ¿Qué diferencia hay entre nivel 2 y nivel 3?**

En nivel 2 se gestionan los procesos del proyecto; en nivel 3 existe una base de procesos organizacionales compartida que los proyectos adaptan. La diferencia no es solamente tener más documentos.

**31. ¿Qué distingue madurez de capacidad?**

Madurez considera conjuntos de procesos en un alcance organizacional; capacidad considera un proceso o área particular. En v1.3 hay cinco niveles de madurez, 1 a 5, y cuatro de capacidad, 0 a 3. La lámina de seis niveles continuos mezcla versiones.

**32. ¿Qué aporta IDEAL?**

Una forma de organizar mejora: iniciar con contexto y patrocinio, diagnosticar, establecer prioridades y plan, actuar mediante implementación y pilotos, y aprender para ajustar. Ayuda a convertir una intención de mejora en un proceso sostenido.

### 23.4. Testing, revisiones y auditorías

**33. Diferencie verificación y validación con un ejemplo.**

Verificar es comprobar que el cálculo aplica la tarifa especificada. Validar es comprobar que esa tarifa y ese comportamiento responden a la necesidad real del club. Una especificación equivocada puede verificarse correctamente y producir un resultado no válido para el uso.

**34. ¿Cómo planificaría pruebas para una función nueva?**

Definiría objetivo y alcance, analizaría requisitos y riesgos, elegiría niveles, tipos y técnicas, prepararía datos y ambiente, asignaría responsables y tiempos y acordaría criterios de entrada y salida. Luego registraría ejecución, defectos, cobertura y riesgos pendientes.

**35. Explique los cuatro niveles de prueba.**

Unitario: unidades aisladas. Integración: relaciones entre piezas. Sistema: producto completo y sus atributos. Aceptación: adecuación al uso y criterios acordados. Que las unidades funcionen separadas no garantiza que colaboren correctamente.

**36. ¿Qué diferencia carga de estrés?**

Carga observa comportamiento bajo actividad prevista o especificada. Estrés explora condiciones más allá de límites o con recursos insuficientes para evaluar degradación, fallos y recuperación. Ambas requieren condiciones y resultados definidos.

**37. Diseñe equivalencias y límites para un entero de 1 a 10.**

Clases: menor que 1, de 1 a 10 y mayor que 10; representantes posibles: −3, 5 y 20. Límites y vecinos: 0, 1, 2, 9, 10 y 11. Agregar tipos inválidos y ausencia según el contrato.

**38. ¿Por qué 100% de sentencias no significa 100% de decisiones?**

Porque un caso puede ejecutar todas las instrucciones existentes y recorrer solo una salida de una condición. Para decisiones se necesita cubrir sus resultados relevantes, no solamente las líneas ejecutables.

**39. ¿Cómo se diferencia testing exploratorio de improvisación?**

La exploración integra aprendizaje, diseño y ejecución con una misión y registro. Usa observaciones para orientar nuevas pruebas. Puede ser flexible sin carecer de objetivo ni evidencia.

**40. ¿Qué información debe tener un defecto para ser reproducible?**

Versión, ambiente, precondiciones, entradas, pasos, resultado esperado, resultado observado y evidencia. Severidad y prioridad ayudan a decidir atención, pero no reemplazan la descripción reproducible.

**41. ¿Qué diferencia una inspección de un walkthrough?**

La inspección utiliza preparación, roles, checklists, registro y seguimiento formales. El walkthrough suele ser una explicación guiada por el autor con preguntas y menor formalidad. Ambos pueden detectar problemas y compartir conocimiento.

**42. Describa el proceso de inspección.**

Planificar, dar visión general, preparar individualmente, reunir y registrar hallazgos, corregir y verificar seguimiento. Durante la reunión se prioriza detectar y aclarar problemas, sin convertirla en una sesión extensa de reparación o evaluación personal.

**43. ¿Qué evidencia sustenta una desviación de auditoría?**

Debe existir un criterio aplicable y evidencia de que no se cumple. Por ejemplo, un procedimiento exige aprobación previa y registros concretos muestran cambios incorporados sin esa aprobación. El hallazgo explica criterio, evidencia y diferencia.

**44. Compare auditoría de proyecto, funcional y física.**

La de proyecto evalúa cumplimiento del proceso y consistencia de productos. La funcional contrasta capacidades y requisitos. La física contrasta configuración construida, componentes y documentación. Tienen focos distintos, aunque puedan compartir evidencias.

**45. ¿Qué se audita al evaluar al GAC?**

Su cumplimiento de actividades de aseguramiento: planificación, independencia, criterios, evidencia, reportes y seguimiento. La pregunta es si el sistema que asegura calidad también cumple su proceso y responsabilidades.

**46. Describa el proceso de auditoría.**

Preparación y planificación; apertura y ejecución; análisis de evidencia; presentación de resultados en el cierre; reporte final; plan de acciones y seguimiento hasta verificar resolución. Deben distinguirse auditor, auditado y responsabilidades de gerencia.

**47. Diferencie desviación, observación y buena práctica.**

La desviación registra incumplimiento y exige acción; la observación señala mejora o riesgo según los criterios; la buena práctica destaca un desempeño útil superior a lo esperado. No se debe usar observación para ocultar un incumplimiento claro.

**48. ¿Cómo conviven responsabilidad compartida de calidad e independencia de SQA?**

El equipo construye y controla la calidad cotidianamente; una evaluación independiente aporta visibilidad sobre cumplimiento y riesgos. Compartir responsabilidad no elimina la necesidad de objetividad ni convierte cada decisión en responsabilidad exclusiva de SQA.

### 23.5. Testing ágil e integración de conceptos

**49. ¿Por qué testing ágil es una actividad continua?**

Porque comienza al aclarar expectativas y sigue durante diseño, código, integración y evaluación del incremento. Reduce la espera entre introducir y detectar un problema. La DoD integra las pruebas necesarias al trabajo terminado.

**50. Explique los cuadrantes y su relación con la pirámide.**

Q1 y Q2 apoyan la construcción desde tecnología y negocio; Q3 y Q4 evalúan críticamente el producto desde negocio y tecnología. La pirámide ayuda a distribuir pruebas por alcance y costo. Son perspectivas complementarias, no secuencias de ejecución.

**51. ¿Qué haría si todas las historias llegan a pruebas al final del Sprint?**

Investigaría tamaño, dependencias, políticas y WIP; promovería historias más pequeñas, definición temprana de ejemplos y colaboración para completar trabajo. Pasar pruebas al Sprint siguiente de manera habitual posterga calidad y crea trabajo incompleto.

**52. ¿Cómo conecta Lean con TDD, CI y calidad?**

Lean busca reducir desperdicio y acortar feedback. TDD aclara comportamiento y detecta problemas localmente; CI detecta incompatibilidades frecuentes; revisiones y pruebas evitan propagación. Juntas reducen retrabajo y sostienen entregas pequeñas con confianza.

<a id="fuentes"></a>
## 24. Lista de control de estudio y fuentes

### 24.1. Cobertura del temario

| Tema del programa | Secciones principales |
|---|---|
| Filosofía Lean y Kanban en desarrollo de software | 3 y 4. |
| Métricas tradicional, Lean y Agile | 5; ejercicios en 21 y 23. |
| Prácticas continuas | 7 y 8; relación con testing en 20. |
| Conceptos generales de calidad | 9. |
| Importancia, ventajas y dificultades de trabajar con calidad | 9.5 y 9.6. |
| Actividades de aseguramiento | 10. |
| Modelos CMMI, SPICE e ISO | 11 y 12. |
| Auditorías de proyecto y al Grupo de Calidad | 19.3 y 19.6. |
| Proceso de auditoría | 19.7 a 19.12. |
| Planificación, niveles, tipos, técnicas y herramientas de pruebas | 14 a 17. |
| Técnicas y herramientas de revisiones técnicas | 18. |
| Testing en ambientes ágiles | 20. |

Scrum básico y gestión de producto aparecen como contexto en 2 y 6. La cobertura documental no establece el peso que tendrá cada tema en el examen.

### 24.2. Autoevaluación

- [ ] Puedo explicar los principios Lean y reconocer desperdicios en un caso.
- [ ] Distingo Kanban de un tablero y explico WIP, pull, políticas y cadencias.
- [ ] Comparo las métricas de los tres enfoques y calculo tiempos y eficiencia.
- [ ] Distingo esfuerzo, duración, capacidad, velocidad y valor.
- [ ] Explico SCM, build privado, de integración y de release.
- [ ] Distingo CI, entrega continua y despliegue continuo.
- [ ] Desarrollo un ejemplo Red-Green-Refactor y explico ATDD.
- [ ] Defino calidad según interesados y contexto.
- [ ] Comparo aseguramiento, planificación, control y testing.
- [ ] Explico actividades de SQA y por qué importa su independencia.
- [ ] Reconozco atributos de calidad de producto y calidad en uso.
- [ ] Comparo CMMI, SPICE, normas ISO e IDEAL.
- [ ] Distingo madurez y capacidad, aclarando la versión de CMMI.
- [ ] Diferencio verificación y validación con ejemplos.
- [ ] Elaboro un esquema de plan de pruebas y un caso reproducible.
- [ ] Distingo niveles, tipos y técnicas de prueba.
- [ ] Resuelvo equivalencias y valores límite sin inventar requisitos ambiguos.
- [ ] Diferencio severidad, prioridad, confirmación y regresión.
- [ ] Explico roles, proceso y métricas de inspección.
- [ ] Comparo inspección, walkthrough y auditoría.
- [ ] Explico auditorías de proyecto, configuración y GAC.
- [ ] Redacto un hallazgo con criterio, evidencia y diferencia.
- [ ] Describo el seguimiento de desviaciones hasta su cierre.
- [ ] Explico principios, prácticas, cuadrantes y pirámide de testing ágil.
- [ ] Puedo relacionar todos esos conceptos con el caso de reservas.

### 24.3. Material base de la carpeta

El resumen integra los once archivos Markdown y el PDF de siete páginas. Las referencias locales corresponden a la ubicación original del material.

| Archivo | Aporte principal |
|---|---|
| [05 Gestión de Productos.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/05 Gestión de Productos.md>) | Valor, Lean Startup, MVP, mínimos comercializables y experiencia de producto. |
| [08 SCRUM 2026, Planificación de release y sprint, Métricas Scrum.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/08 SCRUM 2026, Planificación de release y sprint, Métricas Scrum.md>) | Empirismo, Scrum, planificación y métricas. |
| [10 LEAN KANBAN.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/10 LEAN  KANBAN.md>) | Principios, desperdicios, prácticas Kanban y flujo. |
| [11 Métricas en los Diferentes Enfoques.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/11 Métricas en los Diferentes Enfoques.md>) | Comparación de métricas y fórmulas. |
| [Agile SCM.pdf](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/Agile SCM.pdf>) | Artículo de Berczuk, Appleton y Konieczka de 2003 sobre builds, integración y automatización. |
| [TDD.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/TDD.md>) | Ciclo TDD, patrones y refactoring. |
| [12 PPQA_Intro.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/12 PPQA_Intro.md>) | Calidad, SQA, modelos de producto, CMMI e IDEAL. |
| [09 Testing de Software.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/09 Testing de Software.md>) | Fundamentos, proceso, niveles, tipos y ambientes. |
| [09 Testing de Software Estrategias Caja Negra.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/09 Testing de Software Estrategias Caja Negra.md>) | Equivalencias, límites y ejercicios. |
| [13 Revisiones Técnicas.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/13 Revisiones Técnicas.md>) | V&V, inspección, walkthrough, roles y métricas. |
| [14 Auditorías de Sw.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/14 Auditorías de Sw.md>) | Tipos, proceso, roles, hallazgos y seguimiento. |
| [09 Agile Testing.md](<C:/Users/vale-/Desktop/UTN 2026/Ingenieria y Calidad de Software/Parcial2Teo/Archivos en md/09 Agile Testing.md>) | Principios, prácticas, cuadrantes, pirámide e IDEAL. |

### 24.4. Alcance de complementos y aclaraciones

Las referencias externas están enlazadas junto a las explicaciones que respaldan: CI/CD, distinción de modelos ISO, propósito de ciertas normas, niveles de capacidad CMMI v1.3 y escala histórica SPICE. Su función es completar contenidos breves y aclarar inconsistencias, manteniendo como eje el material de la cátedra.

Los desarrollos de auditoría al GAC, estructura práctica del plan de pruebas, caso integrador y ejercicios resueltos son elaboraciones didácticas identificadas dentro del texto. No se atribuyen como transcripciones literales de las diapositivas.

Se conserva la terminología relevante de clase, pero se aclaran especialmente: las ediciones de CMMI e ISO, el uso de «falla» en distintos apuntes, las proporciones orientativas de la pirámide, la distinción entre confirmación y regresión y los supuestos necesarios para resolver ejercicios. Para responder una consigna que mencione una edición o convención específica, indicar explícitamente cuál se utiliza.
