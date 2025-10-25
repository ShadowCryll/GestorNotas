# Gestor de Notas Académicas
Proyecto Universitario - El objetivo es armar un gestor de notas que pueda tener muchas funcionalidades que nos ayuden a hacer todo más ordenado en cuanto a registros se refiere, va orientado a Estudiantes, de manera que sean capaces de usarlo sin problemas. Dicho esto, el sistema contará con las funciones de: registrar, visualizar, modificar, eliminar, analizar y organizar las calificaciones de los cursos que el estudiante ha cursado, todo esto mediante la consola del sistema en python. (No se usarán librerías externas)
   
Contará con un menú interactivo que nos permitirá navegar a través de las diferentes funciones, de manera qué sea fácil e intuitivo de usar, el proyecto irá avanzando al pasar los meses. Se actualizará periódicamente el desarrollo de este proyecto, así que puedes esperar los cambios con emoción :D 

El programa es desarrollado en Python como parte de un proyecto modular.  
El diseño sigue principios de "modularidad", usando funciones puras para cálculos y proceimientos para la interacción con el usuario.  
Actualmente, la información se maneja **en memoria** (no se guarda en archivos).  

=======================================

## Fases de desarrollo del proyecto

### **Avance 1 y 2 – Fundamentos y modularidad**
- Se implementó el registro de notas de varios estudiantes o cursos.  
- Se aplicó el principio de **modularidad**, dividiendo el código en funciones y procedimientos con responsabilidades específicas.  
- Se introdujeron **precondiciones** y **postcondiciones** para cada función, mejorando la documentación y trazabilidad del código.  
- Validación de notas dentro del rango [0–100].

### **Avance 3 – Condicionales, contadores y búsqueda**
- Se incorporaron estructuras condicionales y contadores para determinar cursos **aprobados y reprobados**.  
- Implementación de **búsqueda lineal** para localizar cursos por nombre.  
- Se mejoró la interacción con el usuario mediante menús iterativos.  

### **Avance 4 – Eliminación, listas y modularización**
- Se añadió la opción de **eliminar cursos** del registro.  
- Introducción del concepto de **listas dinámicas**, reemplazando estructuras fijas.  
- Cada módulo fue documentado y aislado según su responsabilidad.  
- Se incluyó la base para futuras estructuras como pilas y colas.

### **Avance 5 – Pilas, colas y ordenamientos**
- Implementación de una **pila (LIFO)** para registrar el **historial de acciones** (altas, modificaciones y eliminaciones).  
- Creación de una **cola (FIFO)** que simula una lista de **solicitudes de revisión académica**, donde los cursos se atienden en orden de llegada.  
- Incorporación de dos algoritmos de ordenamiento:
  - **Burbuja**: para ordenar cursos por nota (de mayor a menor).  
  - **Inserción**: para ordenar cursos alfabéticamente por nombre.  
- Se añadió la **búsqueda binaria**, complementando la búsqueda lineal y mejorando la eficiencia.  
- Menú actualizado con 13 opciones principales que integran todas las funcionalidades.

### **Avance 6 – Reestructuración con Programación Orientada a Objetos**
- Introducción de las clases `Curso` y `GestorNotas`.  
- Atributos y métodos definidos dentro de `__init__`, sin variables de clase ni decoradores.  
- Métodos principales:
  - `registrar_curso(nombre, nota)`
  - `mostrar_cursos()`
- Uso de listas internas para almacenar objetos `Curso`.  
- Se conserva el mismo flujo de interacción, pero con una arquitectura más limpia y reutilizable.  
- Este avance marca la transición hacia un sistema completamente basado en objetos.

---
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
##  Estructuras de datos utilizadas

| Tipo de estructura | Implementación | Propósito principal |
|--------------------|----------------|----------------------|
| **Lista** | `list` de Python | Almacenar los cursos y sus notas. |
| **Pila (LIFO)** | `append()` / `pop()` | Guardar historial de acciones. |
| **Cola (FIFO)** | `append()` / `pop(0)` | Gestionar solicitudes de revisión. |

---

##  Algoritmos implementados

| Algoritmo | Tipo | Uso dentro del sistema |
|------------|------|------------------------|
| **Burbuja (Bubble Sort)** | Ordenamiento | Ordenar cursos por nota. |
| **Inserción (Insertion Sort)** | Ordenamiento | Ordenar cursos por nombre. |
| **Búsqueda lineal** | Búsqueda secuencial | Localizar cursos por nombre (sin ordenar). |
| **Búsqueda binaria** | Búsqueda optimizada | Buscar cursos en listas previamente ordenadas. |

---

##  Arquitectura modular y flujo

El sistema sigue un flujo lógico basado en la interacción del usuario con el menú principal.  
Cada opción del menú ejecuta un módulo o función específica, garantizando independencia entre las operaciones.  
El control de flujo utiliza un ciclo repetitivo `while` que finaliza únicamente cuando el usuario selecciona la opción “Salir”.

El diseño modular favorece:
- **Mantenimiento del código**: cada función se puede modificar sin afectar otras.  
- **Reutilización**: funciones puras que pueden usarse en otros programas.  
- **Claridad**: estructura limpia, legible y fácil de depurar.  

---

##  Organización del código

- `avance_proyecto_06.py` → versión completa con todas las funcionalidades integradas.  
- `gestor_notas.py` (opcional) → versión orientada a objetos con clases separadas.  
- `README.md` → documentación principal del proyecto.  
- `Guía_tecnico.pdf` → documento técnico con explicación detallada de la estructura interna.  
- `Guía_usuario.pdf` → guía visual para la interacción con el programa.  
============================================

## Requisitos de ejecución

- Python **3.10** o superior.  
- Editor recomendado: **VS Code** o **PyCharm**.  
- No requiere librerías externas.  
- El programa se ejecuta directamente desde consola:
  ```bash
  python avance_proyecto_06.py

---

## Ejemplo de uso
```
====== GESTOR DE NOTAS ACADÉMICAS ======
1. Registrar nuevo curso
2. Mostrar todos los cursos y notas
3. Calcular promedio general
4. Contar cursos aprobados y reprobados
5. Buscar curso por nombre (búsqueda lineal)
6. Actualizar nota de un curso
7. Eliminar un curso
8. Ordenar cursos por nota (burbuja)
9. Ordenar cursos por nombre (inserción)
10. Buscar curso por nombre (búsqueda binaria)
11. Simular cola de revisión
12. Mostrar historial
13. Salir

Selecciones una opción: 1
Curso registrado con éxito.
Promedio general: 87.5
Historial actualizado: Registro de Matemáticas agregado.
```
--- 

## Reflexión personal

Durante el desarrollo del proyecto Gestor de Notas Académicas, aprendí de forma práctica cómo los conceptos fundamentales de la programación pueden integrarse en un sistema completo y funcional.
Al principio, el trabajo consistía únicamente en escribir pseudocódigo estructurado, pero conforme avanzaban las fases del proyecto, fui comprendiendo la importancia de la modularidad, la reutilización del código, y la organización por responsabilidades.

La implementación de estructuras de datos (listas, pilas y colas) me ayudó a entender cómo se puede simular el comportamiento de modelos reales dentro de un programa.
Más adelante, al aplicar algoritmos de ordenamiento y búsqueda, noté cómo el rendimiento y la claridad del código dependen de la elección del método correcto según la situación.
Finalmente, la incorporación de la Programación Orientada a Objetos (POO) me permitió visualizar los cursos y las notas no como simples datos, sino como entidades con atributos y comportamientos propios.

Lo más desafiante fue reorganizar el sistema sin romper su estructura previa, asegurando que todas las funciones conservaran coherencia y compatibilidad.
También fue un reto mantener el equilibrio entre un diseño limpio y la funcionalidad completa, especialmente al integrar nuevas características como el historial y la cola de revisión.

Si tuviera más tiempo, me gustaría mejorar la persistencia del sistema, permitiendo guardar y recuperar los datos desde archivos o incluso una base de datos local.
También exploraría el uso de interfaces gráficas (GUI) para hacerlo más visual e intuitivo.

En general, este proyecto me permitió afianzar conceptos clave de la lógica de programación, comprender el valor del diseño modular y adquirir una visión más amplia sobre cómo se construye un sistema bien estructurado desde cero.

Y... Bueno, eso sería todo por mi parte. Sin duda alguna fue un proecto muy divertido de hacer :D
