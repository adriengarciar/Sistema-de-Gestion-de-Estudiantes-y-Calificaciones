def asignar_nota(estudiantes):
    if not estudiantes:
        print("\n No hay estudiantes registrados para asignar notas.")
        return

    print("\n===== ASIGNAR CALIFICACIÓN =====")
    id_input = input("Ingrese el ID del estudiante: ")

    # Convertir ID a entero
    try:
        id_buscar = int(id_input)
    except ValueError:
        print("ID inválido. Debe ingresar un número entero.")
        return

    # Buscar al estudiante por ID
    for est in estudiantes:
        if est.get("id") == id_buscar:
            print(f"\nEstudiante encontrado: {est.get('nombre')} {est.get('apellido')}")

    # 1. Mostrar lista de estudiantes
    print("\n=== ASIGNAR NOTA ===\n")
    print("Estudiantes disponibles:\n")
    for est in estudiantes:
        # Asumiendo que 'id', 'nombre', y 'apellido' existen
        print(f"ID: {est.get('id')} - {est.get('nombre','')} {est.get('apellido','')}")

    try:
        # 2. Seleccionar estudiante
        id_est = int(input("\n\nIngrese el ID del estudiante: "))

            # Si no tiene calificaciones crear lista
            if est.get("calificaciones") is None:
                est["calificaciones"] = []

            # Añadir la nueva nota
            est["calificaciones"].append(nueva_nota)

            print("Nota asignada correctamente.")
            print(f"Notas actuales: {est['calificaciones']}")

        # Buscar el estudiante por ID
        estudiante = next((est for est in estudiantes if est.get('id') == id_est), None)

        if not estudiante:
            print("\n Estudiante con ese ID no encontrado.")
            return

        # 3. Seleccionar materia
        print(f"\n\nAsignando nota a: {estudiante.get('nombre','')} {estudiante.get('apellido','')}\n")
        print("Materias disponibles:")
        print(" 1) Algoritmos")
        print(" 2) Programación\n")

        op = input("Seleccione el número de la materia (1 o 2): ")

        if op == "1":
            materia = "Algoritmos"
        elif op == "2":
            materia = "Programación"
        else:
            print("\n Opción de materia no válida. Intente de nuevo.")
            return

        # 4. Ingresar y validar la nota
        nota = float(input(f"\nIngrese la nota para {materia} (0-100): "))

        if 0 <= nota <= 100:
            # 5. Asignar la nota
            # Asegurar que la clave 'nota' exista y sea un diccionario
            if 'nota' not in estudiante or not isinstance(estudiante.get('nota'), dict):
                estudiante['nota'] = {}

            estudiante['nota'][materia] = nota
            print(f"\n\nNota asignada: {estudiante.get('nombre','')} {estudiante.get('apellido','')} | {materia}: {nota:.2f}\n")
        else:
            print("\n La nota debe ser un valor entre 0 y 100.")

    except ValueError:
        print("\n Error: Entrada inválida. Asegúrese de ingresar números para el ID y la nota.")


if __name__ == "__main__":
    # Este módulo está pensado para ser importado desde `main.py`.
    # Ejecutar funciones de interfaz aquí puede provocar errores porque
    # `menu_principal` está definido en `main.py`. Solo mostrar ayuda.
    print("Módulo de calificaciones. Importar desde `main.py` para usar la aplicación.")





