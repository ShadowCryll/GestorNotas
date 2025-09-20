# Para este avance se añadieron nuevamente los PRE Y POST como comentarios en las funciones y procedimientos, cosa que en el 
# avance anterior se me olvidó jajaja :D la estructura del código es similar a la del avance anterior, pero ahora se maneja una lista de estudiantes
# donde cada estudiante es un diccionario con su nombre y una lista de cursos (cada curso es una tupla de nombre y nota). Se añadieron las funcionalidades de buscar, actualizar y eliminar.
# También se quito la funcionalidad de guardar y cargar desde archivo, ya que estuvo causando problemas a la hora de implementarlo y no sabía como solucionarlo,
# así que preferí dejarlo para el próximo avance y enfocarme en las funcionalidades principales del gestor de notas. Si para el proximo avace logro que me funcione
# puessss.... se va añadir jssjjss de momento no :D 
# La funcion de eliminar curso se implemento tal que el usuario es capaz de eliminar un curso de los tres que se solicitan para registrar un estudiante.
# esto da como paso que un estudiante puede quedar con 0, 1 o 2 cursos, pero no más de 3. por lo que de algun modo se incumple el requisito de 3 cursos por estudiante,
# pero creo que es un detalle menor y no afecta la funcionalidad principal del programa. para el siguiente avance se puede mejorar esto, pero de momento lo dejo así.
# Además, se mejoró la validación de entradas para evitar errores al ingresar datos no numéricos. Y implementamos .strip() y .lower() para evitar complicacion con el usuario :)
# De esa manera es mas intuitivo y amigable dentro de lo que cabe :D Y..... pues eso, eso sería todo, cualquier duda o consulta podrán verla en el archivo .Md que traera las intrucciones de todo el pograma. 
# Adios :D
# En aprobados o reprobados se piensa cambiar para la proxima ya que se cuenta por cursos y no estudiantes, eso da como resultado que en aprobados o reprobados no se tome en cuenta el promedio general y solo por curso.

# =======================================================
# FUNCIONES
# =======================================================

def calcular_promedio_cursos(cursos):
    """
    Precondición:
        - cursos es una lista de tuplas (curso, nota), puede estar vacía
    Postcondición:
        - Retorna el promedio de las notas de los cursos
        - Si cursos está vacío, retorna 0
    """
    if not cursos:
        return 0
    return sum(nota for _, nota in cursos) / len(cursos)


# =======================================================
# PROCEDIMIENTOS
# =======================================================

def registrar_estudiante(estudiantes):
    """
    Precondición:
        - Se debe ingresar un nombre válido y al menos 1 curso con nota válida
    Postcondición:
        - El estudiante queda registrado en la lista
    """
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    cursos = []

    cantidad = 3  # seguimos pidiendo 3 cursos al registrar
    for i in range(1, cantidad + 1):
        curso = input(f"Ingrese el nombre del curso {i}: ").strip()
        try:
            nota = float(input(f"Ingrese la nota de {curso} (0 a 100): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return

        if 0 <= nota <= 100:
            cursos.append((curso, nota))
        else:
            print("Nota inválida. Registro cancelado.")
            return

    estudiantes.append({"nombre": nombre, "cursos": cursos})
    print("Estudiante registrado con éxito.")


def mostrar_estudiantes(estudiantes):
    """
    Precondición:
        - estudiantes puede estar vacío
    Postcondición:
        - Muestra estudiantes con sus cursos y notas
    """
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for i, est in enumerate(estudiantes, start=1):
        print(f"\n{i}. {est['nombre']}")
        for curso, nota in est["cursos"]:
            print(f"   {curso} - Nota: {nota}")
        promedio = calcular_promedio_cursos(est["cursos"])
        print(f"   Promedio: {promedio:.2f}")


def contar_aprobados(estudiantes):
    """
    Precondición:
        - estudiantes contiene registros válidos
    Postcondición:
        - Muestra cuántos cursos están aprobados y reprobados
    """
    aprobados = 0
    reprobados = 0

    for est in estudiantes:
        for _, nota in est["cursos"]:
            if nota >= 60:
                aprobados += 1
            else:
                reprobados += 1

    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")


def buscar_estudiante(estudiantes):
    """
    Precondición:
        - estudiantes contiene registros
    Postcondición:
        - Muestra al estudiante y sus cursos si lo encuentra
    """
    buscado = input("Ingrese el nombre del estudiante a buscar: ").strip().lower()
    encontrado = False

    for est in estudiantes:
        if est["nombre"].lower() == buscado:
            print(f"\nEstudiante encontrado: {est['nombre']}")
            for curso, nota in est["cursos"]:
                print(f"   {curso} - Nota: {nota}")
            promedio = calcular_promedio_cursos(est["cursos"])
            print(f"   Promedio: {promedio:.2f}")
            encontrado = True

    if not encontrado:
        print("Estudiante no encontrado.")


def actualizar_nota(estudiantes):
    """
    Precondición:
        - estudiantes contiene registros
    Postcondición:
        - Si el estudiante existe, se puede actualizar una nota
    """
    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    for est in estudiantes:
        if est["nombre"].lower() == nombre:
            print(f"\nCursos de {est['nombre']}:")
            for i, (curso, nota) in enumerate(est["cursos"], start=1):
                print(f"{i}. {curso} - Nota: {nota}")

            try:
                indice = int(input("Seleccione el número del curso a actualizar: ")) - 1
                nueva_nota = float(input("Ingrese la nueva nota (0 a 100): "))
            except ValueError:
                print("Entrada inválida.")
                return

            if 0 <= nueva_nota <= 100 and 0 <= indice < len(est["cursos"]):
                curso, _ = est["cursos"][indice]
                est["cursos"][indice] = (curso, nueva_nota)
                print("Nota actualizada con éxito.")
            else:
                print("Datos inválidos.")
            return

    print("Estudiante no encontrado.")


def eliminar_curso(estudiantes):
    """
    Precondición:
        - estudiantes contiene registros
    Postcondición:
        - Si el estudiante existe, se puede eliminar uno de sus cursos
    """
    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    for est in estudiantes:
        if est["nombre"].lower() == nombre:
            print(f"\nCursos de {est['nombre']}:")
            for i, (curso, nota) in enumerate(est["cursos"], start=1):
                print(f"{i}. {curso} - Nota: {nota}")

            try:
                indice = int(input("Seleccione el número del curso a eliminar: ")) - 1
            except ValueError:
                print("Entrada inválida.")
                return

            if 0 <= indice < len(est["cursos"]):
                eliminado = est["cursos"].pop(indice)
                print(f"Curso '{eliminado[0]}' eliminado con éxito.")
            else:
                print("Índice inválido.")
            return

    print("Estudiante no encontrado.")


def mostrar_menu():
    print("\n====== GESTOR DE NOTAS ======")
    print("1. Registrar estudiante (3 cursos)")
    print("2. Mostrar estudiantes y notas")
    print("3. Contar aprobados y reprobados")
    print("4. Buscar estudiante por nombre")
    print("5. Actualizar nota de un curso")
    print("6. Eliminar curso de un estudiante")
    print("7. Salir")


# =======================================================
# PROGRAMA PRINCIPAL
# =======================================================

def main():
    estudiantes = []  # empieza vacío, no carga de archivo

    opcion = 0
    while opcion != 7:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            opcion = 0

        if opcion == 1:
            registrar_estudiante(estudiantes)
        elif opcion == 2:
            mostrar_estudiantes(estudiantes)
        elif opcion == 3:
            contar_aprobados(estudiantes)
        elif opcion == 4:
            buscar_estudiante(estudiantes)
        elif opcion == 5:
            actualizar_nota(estudiantes)
        elif opcion == 6:
            eliminar_curso(estudiantes)
        elif opcion == 7:
            print("Gracias por usar el Gestor de Notas.")
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
