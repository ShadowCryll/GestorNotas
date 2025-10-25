# =======================================================
# FUNCIONES
# =======================================================

def calcular_promedio_cursos(cursos):
    # Precondición:
    #   cursos es una lista de tuplas (nombre, nota)
    # Postcondición:
    #   Retorna el promedio de notas o 0 si la lista está vacía
    if not cursos:
        return 0
    return sum(nota for _, nota in cursos) / len(cursos)


def ordenar_burbuja(cursos):
    # Precondición:
    #   cursos contiene tuplas válidas (nombre, nota)
    # Postcondición:
    #   Retorna una lista ordenada por nota descendente
    ordenados = cursos.copy()
    n = len(ordenados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if ordenados[j][1] < ordenados[j + 1][1]:
                ordenados[j], ordenados[j + 1] = ordenados[j + 1], ordenados[j]
    return ordenados


def ordenar_insercion(cursos):
    # Precondición:
    #   cursos contiene tuplas válidas (nombre, nota)
    # Postcondición:
    #   Retorna una lista ordenada alfabéticamente por nombre
    ordenados = cursos.copy()
    for i in range(1, len(ordenados)):
        actual = ordenados[i]
        j = i - 1
        while j >= 0 and ordenados[j][0].lower() > actual[0].lower():
            ordenados[j + 1] = ordenados[j]
            j -= 1
        ordenados[j + 1] = actual
    return ordenados


def busqueda_lineal(cursos, nombre_buscar):
    # Precondición:
    #   cursos contiene registros válidos
    # Postcondición:
    #   Retorna el índice del curso si se encuentra, o -1 si no existe
    for i, (nombre, nota) in enumerate(cursos):
        if nombre.lower() == nombre_buscar.lower():
            return i
    return -1


def busqueda_binaria(cursos_ordenados, nombre_buscar):
    # Precondición:
    #   cursos_ordenados está ordenado alfabéticamente
    # Postcondición:
    #   Retorna el índice del curso si lo encuentra, -1 si no existe
    inicio, fin = 0, len(cursos_ordenados) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        nombre_medio = cursos_ordenados[medio][0].lower()
        if nombre_medio == nombre_buscar.lower():
            return medio
        elif nombre_medio < nombre_buscar.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1


# =======================================================
# PROCEDIMIENTOS
# =======================================================

def registrar_curso(cursos, historial):
    # Precondición:
    #   Se debe ingresar un nombre y nota válida
    # Postcondición:
    #   Agrega el curso a la lista
    nombre = input("Ingrese el nombre del curso: ").strip()
    for curso, _ in cursos:
        if curso.lower() == nombre.lower():
            print("Este curso ya existe.")
            return
    try:
        nota = float(input("Ingrese la nota (0 a 100): "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    if 0 <= nota <= 100:
        cursos.append((nombre, nota))
        historial.append(f"Registró el curso {nombre} con nota {nota}")
        print("Curso registrado con éxito.")
    else:
        print("Nota fuera de rango (0-100).")


def mostrar_cursos(cursos):
    # Precondición:
    #   cursos puede estar vacío
    # Postcondición:
    #   Muestra todos los cursos y sus notas
    if not cursos:
        print("No hay cursos registrados.")
        return
    for i, (nombre, nota) in enumerate(cursos, start=1):
        print(f"{i}. {nombre} - Nota: {nota}")
    promedio = calcular_promedio_cursos(cursos)
    print(f"\nPromedio general: {promedio:.2f}")


def contar_aprobados(cursos):
    # Precondición:
    #   cursos contiene registros válidos
    # Postcondición:
    #   Muestra cursos aprobados y reprobados
    if not cursos:
        print("No hay cursos registrados.")
        return
    aprobados = [(n, nt) for n, nt in cursos if nt >= 60]
    reprobados = [(n, nt) for n, nt in cursos if nt < 60]

    print("\n=== RESULTADOS GENERALES ===")
    print(f"Aprobados: {len(aprobados)}")
    for n, nt in aprobados:
        print(f"   {n} - {nt}")
    print(f"\nReprobados: {len(reprobados)}")
    for n, nt in reprobados:
        print(f"   {n} - {nt}")


def actualizar_nota(cursos, historial):
    # Precondición:
    #   cursos contiene registros válidos
    # Postcondición:
    #   Actualiza la nota de un curso
    nombre = input("Ingrese el nombre del curso a actualizar: ").strip()
    indice = busqueda_lineal(cursos, nombre)
    if indice == -1:
        print("Curso no encontrado.")
        return
    try:
        nueva = float(input("Ingrese la nueva nota (0 a 100): "))
    except ValueError:
        print("Entrada inválida.")
        return
    if 0 <= nueva <= 100:
        antiguo = cursos[indice]
        cursos[indice] = (antiguo[0], nueva)
        historial.append(f"Actualizó la nota del curso {antiguo[0]} de {antiguo[1]} a {nueva}")
        print("Nota actualizada correctamente.")
    else:
        print("Nota fuera de rango.")


def eliminar_curso(cursos, historial):
    # Precondición:
    #   cursos contiene registros válidos
    # Postcondición:
    #   Elimina un curso si existe
    nombre = input("Ingrese el nombre del curso a eliminar: ").strip()
    indice = busqueda_lineal(cursos, nombre)
    if indice == -1:
        print("Curso no encontrado.")
        return
    confirmar = input(f"¿Seguro que desea eliminar '{cursos[indice][0]}'? (S/N): ").strip().upper()
    if confirmar == "S":
        eliminado = cursos.pop(indice)
        historial.append(f"Eliminó el curso {eliminado[0]}")
        print("Curso eliminado con éxito.")
    else:
        print("Operación cancelada.")


def agregar_a_cola_revision(cola, cursos):
    # Precondición:
    #   cursos contiene registros válidos
    # Postcondición:
    #   Agrega un curso a la cola (FIFO)
    nombre = input("Ingrese el nombre del curso para revisión: ").strip()
    indice = busqueda_lineal(cursos, nombre)
    if indice == -1:
        print("Curso no encontrado.")
        return
    cola.append(cursos[indice])
    print(f"El curso {cursos[indice][0]} fue agregado a la cola de revisión.")


def procesar_cola_revision(cola):
    # Precondición:
    #   cola contiene cursos
    # Postcondición:
    #   Procesa el primer curso de la cola (FIFO)
    if not cola:
        print("No hay cursos en la cola de revisión.")
        return
    curso = cola.pop(0)
    print(f"Revisando curso: {curso[0]} - Nota: {curso[1]}")


def mostrar_historial(historial):
    # Precondición:
    #   historial puede estar vacío
    # Postcondición:
    #   Muestra las acciones en orden LIFO
    if not historial:
        print("El historial está vacío.")
        return
    print("\n===== HISTORIAL DE CAMBIOS =====")
    for accion in reversed(historial):
        print("-", accion)


def mostrar_menu():
    print("\n====== GESTOR DE NOTAS ACADÉMICAS ======")
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (búsqueda lineal)")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota (burbuja)")
    print("9. Ordenar cursos por nombre (inserción)")
    print("10. Buscar curso por nombre (búsqueda binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios (pila)")
    print("13. Salir")


# =======================================================
# PROGRAMA PRINCIPAL
# =======================================================

def main():
    cursos = []
    historial_acciones = []  # pila
    cola_revision = []       # cola

    opcion = 0
    while opcion != 13:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            opcion = 0

        if opcion == 1:
            registrar_curso(cursos, historial_acciones)
        elif opcion == 2:
            mostrar_cursos(cursos)
        elif opcion == 3:
            promedio = calcular_promedio_cursos(cursos)
            print(f"Promedio general: {promedio:.2f}")
        elif opcion == 4:
            contar_aprobados(cursos)
        elif opcion == 5:
            nombre = input("Ingrese el nombre del curso a buscar: ").strip()
            indice = busqueda_lineal(cursos, nombre)
            if indice == -1:
                print("Curso no encontrado.")
            else:
                print(f"Curso encontrado: {cursos[indice][0]} - Nota: {cursos[indice][1]}")
        elif opcion == 6:
            actualizar_nota(cursos, historial_acciones)
        elif opcion == 7:
            eliminar_curso(cursos, historial_acciones)
        elif opcion == 8:
            cursos_ordenados = ordenar_burbuja(cursos)
            print("\nCursos ordenados por nota (Burbuja):")
            mostrar_cursos(cursos_ordenados)
        elif opcion == 9:
            cursos_ordenados = ordenar_insercion(cursos)
            print("\nCursos ordenados por nombre (Inserción):")
            mostrar_cursos(cursos_ordenados)
        elif opcion == 10:
            cursos_ordenados = ordenar_insercion(cursos)
            nombre = input("Ingrese el nombre del curso a buscar: ").strip()
            indice = busqueda_binaria(cursos_ordenados, nombre)
            if indice == -1:
                print("Curso no encontrado.")
            else:
                print(f"Curso encontrado: {cursos_ordenados[indice][0]} - Nota: {cursos_ordenados[indice][1]}")
        elif opcion == 11:
            agregar_a_cola_revision(cola_revision, cursos)
            procesar_cola_revision(cola_revision)
        elif opcion == 12:
            mostrar_historial(historial_acciones)
        elif opcion == 13:
            print("Gracias por usar el Gestor de Notas Académicas.")
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
