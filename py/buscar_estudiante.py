def buscar_estudiante(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return  
    id_buscar = int(input("Ingrese el ID del estudiante a buscar: "))
    for estu in estudiantes:
        if estu['id'] == id_buscar:
            print("\n==============================")
            print(f"Estudiante encontrado:\n")
            print(f"ID: {estu['id']} | Nombre: {estu['nombre']} {estu['apellido']} | Nota: {estu.get('nota', 'No asignada')}")
            print("==============================")
            return
        else:
            print("No se encontró un estudiante con ese ID.")
            print("==============================\n") 