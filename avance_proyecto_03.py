# =======================================================
# FUNCIONES
# =======================================================

def calcular_promedio(lista_notas):
    """
    Precondición:
        - lista_notas contiene al menos un valor numérico válido en [0..100]
    Postcondición:
        - Retorna un número real con el promedio de todas las notas
        - Si lista_notas está vacía, retorna 0
    """
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)


def cargar_datos_desde_archivo():
    """
    Precondición:
        - Puede existir o no el archivo "notas.txt"
    Postcondición:
        - Retorna dos listas: lista_cursos y lista_notas
        - Si no existe archivo, ambas listas estarán vacías
    """
    lista_cursos = []
    lista_notas = []

    try:
        with open("notas.txt", "r") as archivo:
            for linea in archivo:
                curso, nota = linea.strip().split(",")
                lista_cursos.append(curso)
                lista_notas.append(float(nota))
    except FileNotFoundError:
        pass  # Si no existe el archivo, se retorna vacío

    return lista_cursos, lista_notas


# =======================================================
# PROCEDIMIENTOS
# =======================================================

def guardar_notas_en_archivo(lista_cursos, lista_notas):
    """
    Precondición:
        - lista_cursos y lista_notas contienen datos válidos
    Postcondición:
        - El archivo "notas.txt" es sobrescrito con los datos actuales
    """
    with open("notas.txt", "w") as archivo:
        for curso, nota in zip(lista_cursos, lista_notas):
            archivo.write(f"{curso},{nota}\n")


def registrar_curso(lista_cursos, lista_notas):
    """
    Precondición:
        - Usuario ingresa un curso no vacío y una nota válida [0..100]
    Postcondición:
        - Curso y nota son agregados a las listas y guardados en archivo
    """
    curso = input("Ingrese el nombre del curso: ").strip()
    try:
        nota = float(input("Ingrese la nota (0 a 100): "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    if 0 <= nota <= 100:
        lista_cursos.append(curso)
        lista_notas.append(nota)
        guardar_notas_en_archivo(lista_cursos, lista_notas)
        print("Curso y nota registrados con éxito.")
    else:
        print("Nota inválida, intente nuevamente.")


def mostrar_cursos(lista_cursos, lista_notas):
    """
    Precondición:
        - lista_cursos y lista_notas pueden estar vacías
    Postcondición:
        - Imprime los cursos con sus notas, o un mensaje si no hay datos
    """
    if not lista_cursos:
        print("No hay cursos registrados.")
    else:
        for i, (curso, nota) in enumerate(zip(lista_cursos, lista_notas), start=1):
            print(f"{i}. {curso} - Nota: {nota}")


def contar_aprobados(lista_notas):
    """
    Precondición:
        - lista_notas contiene valores numéricos en [0..100]
    Postcondición:
        - Muestra la cantidad de cursos aprobados y reprobados
    """
    aprobados = sum(1 for nota in lista_notas if nota >= 60)
    reprobados = len(lista_notas) - aprobados

    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")


def buscar_curso(lista_cursos, lista_notas):
    """
    Precondición:
        - lista_cursos y lista_notas contienen registros
    Postcondición:
        - Muestra el curso y nota si lo encuentra, o un mensaje si no
    """
    buscado = input("Ingrese el nombre del curso a buscar: ").strip()
    encontrado = False

    for curso, nota in zip(lista_cursos, lista_notas):
        if curso.lower() == buscado.lower():
            print(f"Curso encontrado: {curso} - Nota: {nota}")
            encontrado = True

    if not encontrado:
        print("Curso no encontrado.")


def actualizar_nota(lista_cursos, lista_notas):
    """
    Precondición:
        - lista_cursos y lista_notas contienen registros
    Postcondición:
        - Si el curso existe, su nota se actualiza y se guarda en archivo
    """
    buscado = input("Ingrese el nombre del curso a actualizar: ").strip()
    encontrado = False

    for i, curso in enumerate(lista_cursos):
        if curso.lower() == buscado.lower():
            try:
                nueva_nota = float(input("Ingrese la nueva nota (0 a 100): "))
            except ValueError:
                print("Debe ingresar un número válido.")
                return

            if 0 <= nueva_nota <= 100:
                lista_notas[i] = nueva_nota
                guardar_notas_en_archivo(lista_cursos, lista_notas)
                print("Nota actualizada con éxito.")
            else:
                print("Nota inválida.")

            encontrado = True

    if not encontrado:
        print("Curso no encontrado.")


def mostrar_menu():
    """
    Precondición: N/A
    Postcondición: Muestra las opciones disponibles al usuario
    """
    print("\n====== GESTOR DE NOTAS ======")
    print("1. Registrar curso y nota")
    print("2. Mostrar cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar aprobados y reprobados")
    print("5. Buscar curso por nombre")
    print("6. Actualizar nota de un curso")
    print("7. Salir")


def leer_opcion():
    """
    Precondición:
        - Usuario debe ingresar un valor válido (1–7)
    Postcondición:
        - Retorna la opción seleccionada
    """
    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        return 0


# =======================================================
# PROGRAMA PRINCIPAL
# =======================================================

def main():
    lista_cursos, lista_notas = cargar_datos_desde_archivo()

    opcion = 0
    while opcion != 7:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            registrar_curso(lista_cursos, lista_notas)
        elif opcion == 2:
            mostrar_cursos(lista_cursos, lista_notas)
        elif opcion == 3:
            promedio = calcular_promedio(lista_notas)
            print(f"Promedio general: {promedio:.2f}")
        elif opcion == 4:
            contar_aprobados(lista_notas)
        elif opcion == 5:
            buscar_curso(lista_cursos, lista_notas)
        elif opcion == 6:
            actualizar_nota(lista_cursos, lista_notas)
        elif opcion == 7:
            print("Gracias por usar el Gestor de Notas.")
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
