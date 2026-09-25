# Practico 1: Requerimientos Agiles - User Stories

Unidad Nro. 2: Gestión Lean-Ágil de Productos de Software

Consigna: Identificar y escribir las US identificadas en el Dominio presentado para el práctico.

Salidas:

- Identificación de los roles principales
- US identificadas con sus tarjetas completas

## Dominio

Objetivo del producto: facilitar a las personas la gestión de sus gastos cotidianos y poder acceder a información relacionada a estos.

A continuación, se transcribe parte de la entrevista realizada al experto en el dominio:

Product Owner (PO): ¿Cómo debe visualizarse la planilla de gastos?

Experto en el Dominio (ED): Similar a una tabla en Excel, con columnas donde se pueda indicar el monto, el tipo de gasto, y la fecha en que se realizó el gasto.

PO: ¿La fecha del gasto es la fecha actual? ¿Se toma automáticamente?

ED: Debería mostrar la fecha actual, pero permitir modificarse.

PO: ¿Cuáles son los tipos de gastos permitidos?

ED: Cada persona debería poder registrar sus tipos de gastos, así como indicar si el gasto es propio o de otra persona (por ejemplo, de su esposa).

PO: ¿El nombre o la relación con el usuario debe indicarse?

ED: Debe indicarse el nombre y apellido. También por defecto debe mostrarse el nombre y el apellido del usuario logueado, permitiendo modificarlo, y si alguna vez se registró el nombre y apellido que se comienza a ingresar (no importa si esta vez o una vez anterior), el sistema debería mostrar aquellos nombres y apellidos que comiencen de forma similar, como hace el Excel.

PO: Ah ¿Es decir que el usuario debe registrarse y cuando va a usar la aplicación debe iniciar sesión?, y ¿la sesión caduca en algún momento?

ED: El usuario debe registrarse para permitirle descargar la aplicación, y la primera vez debe iniciar sesión, pero luego se consideran los datos de la sesión registrados, salvo que el usuario decida de loguearse. La sesión no caduca nunca.

PO: ¿Y la planilla de gastos muestra todos los gastos? ¿Cómo se ordenan?

ED: Por defecto se deben mostrar todos los gastos del mes en curso ordenados desde el gasto más actual, pero el sistema debería permitir ver cualquier período que el usuario quiera, y que pueda filtrar por tipo de gasto, por responsable de gasto, por rango de montos. Además debe poder modificar el criterio de ordenamiento. Y para cada filtro que se aplique arriba se debe mostrar el total de gastos según el filtro aplicado.

---

Roles Principales:

- Responsable de Gastos

User Stories:

    **como** <rol> **quiero** <feature> **para** <valor de negocio>
    Criterios de Aceptacion:
        - **Se debe**
    Pueba de Aceptacion de Usuario:
        - **Probar** ... (falla/pasa).

Identificar frases verbales:

- Visualizar Planilla de Gastos
- Registrar Gasto
- Registrar Tipo de Gasto
- Registrar Grupo Familiar

US 1: Visualizar Planilla de Gastos

Como responsable de gastos quiero ser capaz de ver los gastos que registre para poder saber los consumos que hay en su hogar.

Criterios de Aceptacion:

- Se debe poder vizualizar las columnas que indican monto, responsable, tipo de gasto y la fecha en que se realizo el gasto.
- Se debe ver los gastos del mes actual ordenados de forma decendente.
- Se debe poder filtrar por tipo de gasto, fecha, responsable y rango de monto.
- Se debe poder visualizar el total de gasto segun el filtro aplicado.
- Se debe poder seleccionar el tipo de gasto para filtrar
- Se debe poder ingresar el resonsable para filtrar.
- Se debe poder ingresar el rango de monto en decimales para filtrar.
- Se debe poder ingresar las fechas en formato "dd/mm/yyyy" para filtrar por ella.

Pueba de Aceptacion de Usuario:

- Probar filtrar por tipo de gasto y el total de gasto no cambia. (falla)
- Probar filtar por tipo de gasto y aparecen registros del tipo especificado. (pasa)
- Probar filtrar por responsable y aparecen los registros del responsable especificado. (pasa)
- Probar filtrar por rango de monto y aparecen los registros en el rango especificado. (pasa)
- Probar filtrar por periodo y aparecen los registros en el periodo especificado. (pasa)

US 2: Registrar Gastos

Como responsable de gastos quiero ser capaz de registrar mis gastos para poder tener asentado en que cosas gasto mi dinero.

Criterios de Aceptacion:

- Se debe registrar un gasto ingresando un monto positivo, el nombre y apellido del responsable del gasto y seleccionando tipo de gasto
- Se debe ingresar unicamente numeros decimales, para indicar el monto.
- Se debe seleccionar el tipo de gasto.
- Se debe autocompletar el campo de la fecha con la fecha actual.
- Se debe poder modificar la fecha.
- Se debe autocompletar el campo del responsable con el nombre y apellido del usuario logeado.
- Se debe poder modificar el reponsable.
- Se debe mostrar los nombres y apellidos de las personas pertenecientes al grupo familiar que empiecen de forma similar a medida que se va ingresando el responsable

Pueba de Aceptacion de Usuario:

- Probar ingresar caracteres en el campo de monto. (falla)
- Probar intentar grabar el registro sin haber ingresado el valor de un campo. (falla)
- Probar modificar la fecha autocompletada.
- Probar ingresar un gasto y que se autocomplete la fecha.
- Probar ingresar un gasto y que se autocomplete el nombre y apellido del usuario logeado como responsable. (pasa)
- Probar ingresar el nombre de un responsable guardado y que se muestre entre las opciones a seleccionar. (pasa)
- Probar modificar el nombre y apellido del responsable. (pasa)
