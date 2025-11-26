def asignar_nota(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return

    print("\n===== ASIGNAR CALIFICACIÓN =====")
    id_buscar = input("Ingrese el ID del estudiante: ")

    # Buscar a cualquier estudiante  por ID
    for est in estudiantes:
        if est["ID"] == id_buscar:
            print(f"\nEstudiante encontrado: {est['nombre']} {est['apellido']}")

            try:
                nueva_nota = float(input("Ingrese la calificación (0 - 100): "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print(" La nota debe estar entre 0 y 100.")
                    return
            except ValueError:
                print("Debe ingresar un número válido.")
                return

            # Si no tiene calificaciones crear lista
            if est["calificaciones"] is None:
                est["calificaciones"] = []

            est["calificaciones"](nueva_nota)

            print("Nota asignada correctamente.")
            print(f"Notas actuales: {est['calificaciones']}")
            return

    print(" No se encontró un estudiante con ese ID.")

