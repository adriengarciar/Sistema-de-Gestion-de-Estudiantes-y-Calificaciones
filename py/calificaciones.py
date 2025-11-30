def asignar_nota(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
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

            try:
                nueva_nota = float(input("Ingrese la calificación (0 - 100): "))
                if nueva_nota < 0 or nueva_nota > 100:
                    print(" La nota debe estar entre 0 y 100.")
                    return
            except ValueError:
                print("Debe ingresar un número válido.")
                return

            # Si no tiene calificaciones crear lista
            if est.get("calificaciones") is None:
                est["calificaciones"] = []

            # Añadir la nueva nota
            est["calificaciones"].append(nueva_nota)

            print("Nota asignada correctamente.")
            print(f"Notas actuales: {est['calificaciones']}")
            return

    print(" No se encontró un estudiante con ese ID.")


