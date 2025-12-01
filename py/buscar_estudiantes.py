def buscar_estudiante(estudiantes):
    if not estudiantes:
        print("\nNo hay estudiantes registrados.")
        return  
        
    try:
        id_buscar = int(input("\nIngrese el ID del estudiante a buscar: "))
    except ValueError:
        print("\nID inválido. Debes ingresar un número entero.")
        return

    for estu in estudiantes:
        if estu['id'] == id_buscar:
            nota = estu.get('nota', 'No asignada')
            if isinstance(nota, dict):
                nota = " | ".join([f"{m}: {v}" for m, v in nota.items()])
            print("\n==============================")
            print(f"Estudiante encontrado:\n")
            print(f"ID: {estu['id']} | Nombre: {estu['nombre']} {estu['apellido']} | Nota: {nota}")
            print("==============================")
            return
        else:
            print("\nNo se encontró un estudiante con ese ID.")
            print("==============================\n") 
