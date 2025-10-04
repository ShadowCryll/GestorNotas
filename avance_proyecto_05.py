# =======================================================
# FUNCIONES
# =======================================================

def calcular_promedio_cursos(cursos):
    # Precondición:
    #   cursos es una lista de tuplas (curso, nota), puede estar vacía
    # Postcondición:
    #   Retorna el promedio de las notas de los cursos
    #   Si cursos está vacío, retorna 0
    if not cursos:
        return 0
    return sum(nota for _, nota in cursos) / len(cursos)


def ordenar_burbuja(estudiantes):
    # Precondición:
    #   estudiantes contiene registros válidos
    # Postcondición:
    #   Retorna una nueva lista ordenada por promedio (descendente)
    ordenados = estudiantes.copy()
    n = len(ordenados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if calcular_promedio_cursos(ordenados[j]["cursos"]) < calcular_promedio_cursos(ordenados[j + 1]["cursos"]):
                ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]
    return ordenados


def ordenar_insercion(estudiantes):
    # Precondición:
    #   estudiantes contiene registros válidos
    # Postcondición:
    #   Retorna una nueva lista ordenada alfabéticamente por nombre
    ordenados = estudiantes.copy()
    for i in range(1, len(ordenados)):
        actual = ordenados[i]
        j = i - 1
        while j >= 0 and ordenados[j]["nombre"].lower() > actual["nombre"].lower():
            ordenados[j + 1] = ordenados[j]
            j -= 1
        ordenados[j + 1] = actual
    return ordenados


# =======================================================
# PROCEDIMIENTOS
# =======================================================

def registrar_estudiante(estudiantes, historial):
    # Precondición:
    #   Se debe ingresar un nombre válido y 3 cursos con notas válidas
    # Postcondición:
    #   El estudiante se agrega a la lista y se registra la acción en el historial
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    cursos = []

    for i in range(1, 4):
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
    historial.append(f"Registró al estudiante {nombre}")
    print("Estudiante registrado con éxito.")


def mostrar_estudiantes(estudiantes):
    # Precondición:
    #   estudiantes puede estar vacío
    # Postcondición:
    #   Muestra estudiantes con sus cursos y promedios
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for i, est in enumerate(estudiantes, start=1):
        print(f"\n{i}. {est['nombre']}")
        for curso, nota in est["cursos"]:
            print(f"   {curso} - Nota: {nota}")
        promedio = calcular_promedio_cursos(est["cursos"])
        print(f"   Promedio general: {promedio:.2f}")


def contar_aprobados(estudiantes):
    # Precondición:
    #   estudiantes contiene registros válidos
    # Postcondición:
    #   Muestra cuántos estudiantes aprobaron y reprobaron (según promedio general)
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    aprobados = []
    reprobados = []

    for est in estudiantes:
        promedio = calcular_promedio_cursos(est["cursos"])
        if promedio >= 60:
            aprobados.append((est["nombre"], promedio))
        else:
            reprobados.append((est["nombre"], promedio))

    print("\n=== RESULTADOS GENERALES ===")
    print(f"Estudiantes aprobados: {len(aprobados)}")
    for nombre, prom in aprobados:
        print(f"   {nombre} - Promedio: {prom:.2f}")

    print(f"\nEstudiantes reprobados: {len(reprobados)}")
    for nombre, prom in reprobados:
        print(f"   {nombre} - Promedio: {prom:.2f}")


def actualizar_nota(estudiantes, historial):
    # Precondición:
    #   estudiantes contiene registros
    # Postcondición:
    #   Actualiza una nota y guarda la acción en historial
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
                historial.append(f"Actualizó la nota de {curso} para {est['nombre']}")
                print("Nota actualizada con éxito.")
            else:
                print("Datos inválidos.")
            return
    print("Estudiante no encontrado.")


def eliminar_curso(estudiantes, historial):
    # Precondición:
    #   estudiantes contiene registros
    # Postcondición:
    #   Elimina un curso y registra la acción
    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    for est in estudiantes:
        if est["nombre"].lower() == nombre:
            for i, (curso, nota) in enumerate(est["cursos"], start=1):
                print(f"{i}. {curso} - Nota: {nota}")

            try:
                indice = int(input("Seleccione el número del curso a eliminar: ")) - 1
            except ValueError:
                print("Entrada inválida.")
                return

            if 0 <= indice < len(est["cursos"]):
                eliminado = est["cursos"].pop(indice)
                historial.append(f"Eliminó el curso {eliminado[0]} de {est['nombre']}")
                print(f"Curso '{eliminado[0]}' eliminado con éxito.")
            else:
                print("Índice inválido.")
            return
    print("Estudiante no encontrado.")


def mostrar_historial(historial):
    # Precondición:
    #   historial puede estar vacío
    # Postcondición:
    #   Muestra las acciones recientes (último en entrar, primero en salir)
    if not historial:
        print("El historial está vacío.")
    else:
        print("\n===== HISTORIAL DE ACCIONES =====")
        for accion in reversed(historial):
            print("-", accion)


def agregar_a_cola_revision(cola, estudiantes):
    # Precondición:
    #   estudiantes contiene registros
    # Postcondición:
    #   Agrega un estudiante a la cola de revisión
    nombre = input("Ingrese el nombre del estudiante a agregar a la cola: ").strip().lower()
    for est in estudiantes:
        if est["nombre"].lower() == nombre:
            cola.append(est)
            print(f"{est['nombre']} fue agregado a la cola de revisión.")
            return
    print("Estudiante no encontrado.")


def procesar_cola_revision(cola):
    # Precondición:
    #   cola contiene estudiantes pendientes
    # Postcondición:
    #   Procesa al primer estudiante en la cola (FIFO)
    if not cola:
        print("No hay estudiantes en la cola de revisión.")
    else:
        est = cola.pop(0)
        print(f"Revisando estudiante: {est['nombre']}")
        for curso, nota in est["cursos"]:
            print(f"   {curso}: {nota}")
        promedio = calcular_promedio_cursos(est["cursos"])
        print(f"Promedio general: {promedio:.2f}")


def mostrar_menu():
    print("\n====== GESTOR DE NOTAS - AVANCE 05 ======")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Contar aprobados y reprobados")
    print("4. Actualizar nota")
    print("5. Eliminar curso")
    print("6. Ordenar estudiantes (Burbuja)")
    print("7. Ordenar estudiantes (Inserción)")
    print("8. Ver historial (Pila)")
    print("9. Agregar estudiante a revisión (Cola)")
    print("10. Procesar revisión (Cola)")
    print("11. Salir")


# =======================================================
# PROGRAMA PRINCIPAL
# =======================================================

def main():
    estudiantes = []
    historial_acciones = []  # pila
    cola_revision = []       # cola

    opcion = 0
    while opcion != 11:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            opcion = 0

        if opcion == 1:
            registrar_estudiante(estudiantes, historial_acciones)
        elif opcion == 2:
            mostrar_estudiantes(estudiantes)
        elif opcion == 3:
            contar_aprobados(estudiantes)
        elif opcion == 4:
            actualizar_nota(estudiantes, historial_acciones)
        elif opcion == 5:
            eliminar_curso(estudiantes, historial_acciones)
        elif opcion == 6:
            ordenados = ordenar_burbuja(estudiantes)
            print("\nEstudiantes ordenados por promedio (Burbuja):")
            mostrar_estudiantes(ordenados)
        elif opcion == 7:
            ordenados = ordenar_insercion(estudiantes)
            print("\nEstudiantes ordenados alfabéticamente (Inserción):")
            mostrar_estudiantes(ordenados)
        elif opcion == 8:
            mostrar_historial(historial_acciones)
        elif opcion == 9:
            agregar_a_cola_revision(cola_revision, estudiantes)
        elif opcion == 10:
            procesar_cola_revision(cola_revision)
        elif opcion == 11:
            print("Gracias por usar el Gestor de Notas (Avance 05).")
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
