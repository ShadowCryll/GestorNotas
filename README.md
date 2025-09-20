# Gestor de Notas Académicas
Proyecto Universitario - El objetivo es armar un gestor de notas que pueda tener muchas funcionalidades que nos ayuden a hacer todo más ordenado en cuanto a registros se refiere, va orientado a Estudiantes, de manera que sean capaces de usarlo sin problemas. Dicho esto, el sistema contará con las funciones de: registrar, visualizar, modificar, eliminar, analizar y organizar las calificaciones de los cursos que el estudiante ha cursado, todo esto mediante la consola del sistema en python. (No se usarán librerías externas)
   
Contará con un menú interactivo que nos permitirá navegar a través de las diferentes funciones, de manera qué sea fácil e intuitivo de usar, el proyecto irá avanzando al pasar los meses. Se actualizará periódicamente el desarrollo de este proyecto, así que puedes esperar los cambios con emoción :D 

El programa es desarrollado en Python como parte de un proyecto modular.  
El diseño sigue principios de "modularidad", usando funciones puras para cálculos y proceimientos para la interacción con el usuario.  
Actualmente, la información se maneja **en memoria** (no se guarda en archivos).  

=======================================

## Funcionalidades Implementadas
Con lo que llevamos hasta el **Avance 04**, el programa permite:

1. **Registrar estudiante (3 cursos iniciales)**  
   - Se solicita el nombre del estudinte.  
   - Se ingresan exactamente 3 cursos con sus respectivas notas (validadas entre 0 y 100).  

2. **Mostrar estudiantes y notas**  
   - Lista todos los estudiantes registrados.  
   - Muestra cada curso, su nota y el promedio individual del estudiante.  

3. **Contar aprobados y reprobados**  
   - Recorre todas las notas registradas.  
   - Muestra el número total de cursos aprobaos (≥ 60) y reprobados (< 60).  

4. **Buscar estudiante por nombre**  
   - Permite ingresar el nombre de un estudiante.  
   - Si existe, muestra sus cursos, notas y promedio.  
   - Si no existe, avisa al usuario.  

5. **Actualizar nota de un curso**  
   - Se selecciona un estudiante y uno de sus cursos.  
   - Permite cambiar la nota, siempre validando que esté en el rango [0..100].  

6. **Eliminar curso de un estudiante**  
   - Se selecciona un estudiante y uno de sus cursos.  
   - El curso se elimina de su registro.  

7. **Salir**  
   - Termina la ejecución del programa.  

====================================

## Estructura del Programa
El código está dividido en tres secciones principales:

- **Funciones puras**  
  Se encargan de cálculos sin efectos secundarios.  
  Ejemplo: `calcular_promedio_cursos(cursos)`

- **Procedimientos de interacción**  
  Gestionan la entrada y salida de datos con el usuario (input/print).  
  Ejemplo: `registrar_estudiante(estudiantes)`

- **Programa principal**  
  Implementa el menú principal y la lógica de control.  
  Ejecuta las funciones y procedimientos según la opción seleccionada por el usuario.  

============================================

## Ejecución
1. Clonar o descargar este repositorio.  
2. Abrir la carpeta en VSCode (o cualquier IDE de Python).  
3. Ejecutar el programa:  

```bash
python gestor_notas.py
```

4. Interactuar con el menú:  

```
====== GESTOR DE NOTAS ======
1. Registrar estudiante (3 cursos)
2. Mostrar estudiantes y notas
3. Contar aprobados y reprobados
4. Buscar estudiante por nombre
5. Actualizar nota de un curso
6. Eliminar curso de un estudiante
7. Salir
```

---

## Ejemplo de uso
```
Seleccione una opción: 1
Ingrese el nombre del estudiante: Ana
Ingrese el nombre del curso 1: Matemáticas
Ingrese la nota de Matemáticas (0 a 100): 90
Ingrese el nombre del curso 2: Historia
Ingrese la nota de Historia (0 a 100): 75
Ingrese el nombre del curso 3: Física
Ingrese la nota de Física (0 a 100): 82
Estudiante registrado con éxito.

Seleccione una opción: 2

1. Ana
   Matemáticas - Nota: 90.0
   Historia - Nota: 75.0
   Física - Nota: 82.0
   Promedio: 82.33
```

============================================

## Estado del Proyecto
- Avance 02 -> Registro de notas y promedios.  
- Avance 03 -> Condicionales, contadores, búsqueda y actualización de datos.  
- Avance 04 -> Eliminación de cursos, uso de listas, funciones y modularización.  
- Próximos avances -> Estadísticas generales, eliminación completa de estudiantes, persistencia en archivos.
- Aún hay partes por arreglar y mejorar, hago mención de esto en **avance_proyecto_04.py** en comentarios nada más abrir el archivo.
- Pero para resumir un poco falta, mejorar la funcion de promedio, ya que toma en cuenta los cursos y no promedio general, ya qué cada
- estudiante tiene 3 cursos, los toma individualmente y no en general. Otro podía ser la eliminacion de cursos, ya que se puede dejar a un estudiante
- solo con 2, 1 o 0 cursos sin la posibilidad de borrar los datos pero que quedé el lugar vacante, basicámente eliminación completa. Entre otras cosas más
- por mejorar, pero bueno, eso es todo por mi parte :D 
