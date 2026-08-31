<div align="center">

<img src="https://identidad.frc.utn.edu.ar/ui/logos/logos-utn-frc/logo-utn-frc-v-Extendida_Facultad_Azul.png?v=2" alt="Logo UTN FRC" width="300"/>

### **Ingeniería y Calidad de Software**

</div>

**Integrantes:**

- 95028 Alvaretto Caterina
- 94309 Arce Sayago Camila 
- 431124 Cardozo Soledad Sofía
- 84037 Ficarra Carla Valentina
- 88440 Garcia Pintos Valentin
- 78797 Ostermann Guillermo
- 94017 Pereyra Agustín
- 97376 Pregot Ulises Valentin
- 86363 Pucheta Lanfranco
- 90112 Terreno Monla Florencia Sofia
- 92380 Vaca Sofia Eugenia

**Docentes:**

- Adjunto: Ing. Laura Covaro
- Auxiliares de Trabajos Prácticos
  - Ing. Cecilia Massano
  - Ing. Constanza Garnero
- Adscripto: Ezequiel Izaguirre

**Curso:** 4K3

## **Documento de Gestión de Configuración**

**Enlace al repositorio público:** [_Repositorio_](https://github.com/fterreno/ISW_2026_4K3_G7)

## Herramientas SCM y Flujo de Trabajo

### Herramientas a utilizar:
- **Git:** Como motor de control de versiones mediante línea de comandos.
- **GitHub:** Como plataforma de alojamiento y gestión del repositorio remoto (proporciona accesibilidad y facilita el trabajo colaborativo).

### Flujo de comandos básico:
Para evitar conflictos y mantener el repositorio sincronizado, todos los integrantes deberán seguir este flujo de trabajo al interactuar con el repositorio:

1. **Actualizar el repositorio local antes de empezar a trabajar:**
   ```bash
   git pull origin main
   ```
2. **Realizar los cambios o agregar los archivos necesarios.**
3. **Preparar los cambios para el commit:**
   ```bash
   git add .
   ```
   *(o especificar el archivo modificado)*.
4. **Crear el commit respetando la convención de nombrado:**
   ```bash
   git commit -m "[PREFIJO] Descripción del cambio"
   ```
5. **Subir los cambios al repositorio remoto:**
   ```bash
   git push origin main
   ```

## Estructura del Repositorio

```
ISW_2026_4K3_G/
├── 01_Recursos_Catedra/
│   ├── Bibliografia/
│   ├── Guias/
│   ├── Planificacion/
│   ├── Presentaciones/
│   └── Templates/
├── 02_Material_Estudio_Grupal/
│   ├── Registro_Clases/
│   └── Resumenes/
│   └── Ejercicios/
├── 03_Trabajos_Practicos/
│   ├── Evaluables/
│   ├── Investigacion_Grupal/
│   └── No_Evaluables/
└── README.md
```

## Ítems de Configuración

| Ítem de Configuración | Tipo | Convención de Nombre | Extensión | Ubicación |
|---|---|---|---|---|
| Bibliografía | Material de Estudio | Se mantiene el nombre oficial de la cátedra. | `.pdf`| `ISW_2026_4K3_G7/01_Recursos_Catedra/Bibliografia/` |
| Guías | Material de Estudio | Se mantiene el nombre oficial de la cátedra. | `.pdf` | `ISW_2026_4K3_G7/01_Recursos_Catedra/Guias/` |
| Planificación | Planificación | Se mantiene el nombre oficial de la cátedra. | `.doc`, `.xls` | `ISW_2026_4K3_G7/01_Recursos_Catedra/Planificacion/` |
| Presentaciones | Material de Estudio | Se mantiene el nombre oficial de la cátedra. | `.pdf` | `ISW_2026_4K3_G7/01_Recursos_Catedra/Presentaciones/` |
| Templates | Material de Estudio | Se mantiene el nombre oficial de la cátedra. | `.doc`, `.xls` | `ISW_2026_4K3_G7/01_Recursos_Catedra/Templates/` |
| Registro de Clases | Material de Estudio Grupal | `<AAAA-MM-DD>_<autor>` | `.doc`, `.pdf`, `.md` | `ISW_2026_4K3_G7/02_Material_Estudio_Grupal/Registro_Clases/` |
| Resúmenes | Material de Estudio Grupal | `resumen_parcial_<nro>_<autor>` | `.pdf` | `ISW_2026_4K3_G7/02_Material_Estudio_Grupal/Resumenes/` |
| Ejercicios de la Guía | Material de Estudio Grupal | `<nro>_<nombre_ejercicio>_<autor>` | `.pdf`, `.doc`, `.png`, `.jpeg`, `.md` | `ISW_2026_4K3_G7/02_Material_Estudio_Grupal/Ejercicios/` |
| Trabajos Prácticos Evaluables | Entregas | `tp_<nro>_<nombre>` | `.pdf` o archivos de código | `ISW_2026_4K3_G7/03_Trabajos_Practicos/Evaluables/` |
| Trabajos de Investigación Grupal | Entregas | `tig_<nro>_<nombre>` | `.pdf` | `ISW_2026_4K3_G7/03_Trabajos_Practicos/Investigacion_Grupal/` |
| Trabajos Prácticos No Evaluables | Trabajo en Clase | `tp_<nro>_<nombre>` | `.pdf`, `.doc`, `.png`, `.jpeg`, `.md` | `ISW_2026_4K3_G7/03_Trabajos_Practicos/No_Evaluables/` |
| Plan de Gestión de Configuración | Gestión de Proyecto | `README` | `.md` | `ISW_2026_4K3_G7/` |


Aclaraciones sobre las reglas de nombrado:
- El nombre del archivo se escribe en formato snake_case, sin espacios ni tildes (ej. unidad_1_introduccion.pdf).
- El contenido encerrado con "<>" será remplazado con el siguiente criterio:
  - "AAAA-MM-DD": es fecha de la clase a la que corresponden las notas.
  - "autor": es el integrante del equipo que realizó las notas.
  - "nro": será un numero decimal entero correspondiente al parcial o trabajo practico del que trata el archivo.
  - "nombre": se corresponde al nombre asignado por la catedra para el Trabajos Prácticos o Trabajos de Investigación Grupal.
  - "nombre_ejercicio": nombre descriptivo del ejercicio.

## Convención de Nombrado de Commits

Para mantener la consistencia en el historial del repositorio, todos los mensajes de confirmación (commits) deberán redactarse en español y seguir la siguiente estructura:

`[PREFIJO] Descripción breve del cambio en presente.`

**Prefijos permitidos:**

- `[NUEVO]`: Para la creación o subida de cualquier archivo nuevo, ya sean entregables, material de estudio, apuntes o plantillas *(Ej: `[NUEVO] Se sube la resolución del TP4` o `[NUEVO] Se agrega PDF de la Unidad 3`)*.
- `[CORRECCION]`: Para solucionar errores o modificar entregas y archivos previos *(Ej: `[CORRECCION] Se arregla ubicación de la carpeta de no evaluables`)*.
- `[REORGANIZACION]`: Para mover carpetas, renombrar archivos o ajustar la estructura del repositorio sin cambiar el contenido esencial *(Ej: `[REORGANIZACION] Se mueve archivo de planificación a la carpeta correcta`)*.

## Criterio de Línea Base

Se establece como criterio que la línea base se creará luego de la entrega y revisión de cada Trabajo Práctico Evaluable (TP) y de los Trabajos Prácticos de Investigación, una vez que los ítems de configuración asociados se encuentren completos, revisados y estables. Esto ocurrirá después de la corrección y validación realizada por el profesor.

De esta manera, se garantiza que el repositorio contenga una versión actualizada, revisada y validada del trabajo, sobre la cual se podrán gestionar y controlar los cambios posteriores. Asimismo, la creación de la línea base permitirá asegurar que la información incorporada haya sido revisada y aceptada por las autoridades de la materia.

Las líneas base se identificarán con la siguiente etiqueta: `linea_base_<nro>_<nombre_TP>`. El nombre del TP se escribe en formato snake_case, sin espacios ni tildes.

### Implementación técnica:
Las líneas base se marcarán utilizando etiquetas (tags) en el motor de Git.

**Ejemplo de uso:**
```bash
git tag -a linea_base_1_herramientas_scm -m "Línea Base 1 tras corrección del TP evaluable 1"
```

### Historial de Línea Base

| Etiqueta | Fecha | Descripción |
| --- | --- | --- |
| *`linea_base_0_ejemplo`* | *DD/MM/AAAA* | *Ejemplo: Entrega y revisión del trabajo practico* |
