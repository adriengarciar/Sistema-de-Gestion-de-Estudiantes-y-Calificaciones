def asignar_nota(estudiantes):
   
    if not estudiantes:
        print("\n No hay estudiantes registrados para asignar notas.")
        return
    
    # 1. Mostrar lista de estudiantes
    print("\n--- ASIGNAR NOTA ---")
    print("Estudiantes disponibles:")
    for est in estudiantes:
        # Asumiendo que 'id', 'nombre', y 'apellido' existen
        print(f"ID: {est['id']} - {est['nombre']} {est['apellido']}")
    
    try:
        # 2. Seleccionar estudiante
        id_est = int(input("\nIngrese el ID del estudiante: "))
        
        # Buscar el estudiante por ID
        estudiante = next((e for e in estudiantes if e['id'] == id_est), None)
        
        if not estudiante:
            print("\n Estudiante con ese ID no encontrado.")
            return
        
        # 3. Seleccionar materia
        print(f"\nAsignando nota a: {estudiante['nombre']} {estudiante['apellido']}")
        print("Materia:")
        print("1. Algoritmos")
        print("2. Programación")
        
        op = input("Seleccione el número de la materia (1 o 2): ")
        
        if op == "1":
            materia = "Algoritmos"
        elif op == "2":
            materia = "Programación"
        else:
            print("\n Opción de materia no válida. Intente de nuevo.")
            return
        
        # 4. Ingresar y validar la nota
        nota = float(input(f"Ingrese la nota para {materia} (0-100): "))
        
        if 0 <= nota <= 100:
            # 5. Asignar la nota
            estudiante['calificaciones'][materia] = nota
            print(f"\n Nota asignada: {estudiante['nombre']} {estudiante['apellido']} | {materia}: {nota:.2f}")
        else:
            print("\n La nota debe ser un valor entre 0 y 100.")
            
    except ValueError:
        print("\n Error: Entrada inválida. Asegúrese de ingresar números para el ID y la nota.")





