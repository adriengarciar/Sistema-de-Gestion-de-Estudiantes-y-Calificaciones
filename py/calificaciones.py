def asignar_calificaciones():
    """Asigna calificaciones a un estudiante en diferentes materias"""
    print("\n--- ASIGNAR CALIFICACIONES ---")
    
    if not estudiantes:
        print(" No hay estudiantes registrados. Registre uno primero.")
        return
    
    # Mostrar estudiantes disponibles
    print("\nEstudiantes registrados:")
    for id_est, datos in estudiantes.items():
        print(f"  ID: {id_est} - {datos['nombre']}")
    
    id_estudiante = input("\nIngrese ID del estudiante: ").strip()
    
    if id_estudiante not in estudiantes:
        print(" Error: Estudiante no encontrado.")
        return
    
    estudiante = estudiantes[id_estudiante]
    print(f"\nAsignando calificaciones para: {estudiante['nombre']}")
    print("\nMaterias disponibles:")
    
    for i, materia in enumerate(materias, 1):
        print(f"  {i}. {materia}")
    
    print("\nOpciones:")
    print("  A - Asignar todas las materias")
    print("  E - Asignar materia específica")
    
    opcion = input("\nSeleccione opción (A/E): ").strip().upper()
    
    if opcion == "A":
        # Asignar todas las materias
        print("\nIngrese las calificaciones (0-100):")
        for materia in materias:
            while True:
                try:
                    nota = float(input(f"  {materia}: "))
                    if 0 <= nota <= 100:
                        estudiante["calificaciones"][materia] = nota
                        break
                    else:
                        print("     La nota debe estar entre 0 y 100")
                except ValueError:
                    print("      Ingrese un número válido")
        
        print(f"Calificaciones asignadas exitosamente a {estudiante['nombre']}")
    
    elif opcion == "E":
