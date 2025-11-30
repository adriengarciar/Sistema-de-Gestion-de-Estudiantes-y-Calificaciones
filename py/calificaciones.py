def asignar_nota(estudiantes):
    if not estudiantes:
        print("\n No hay estudiantes registrados para asignar notas.")
        return

    # Mostrar lista breve de estudiantes
    print("\n=== ASIGNAR NOTA ===\n")
    print("Estudiantes disponibles:")
    for est in estudiantes:
        print(f"ID: {est.get('id')} - {est.get('nombre','')} {est.get('apellido','')}")

    # Seleccionar estudiante por ID
    try:
        id_est = int(input("\nIngrese el ID del estudiante: "))
    except ValueError:
        print("ID inválido. Debe ingresar un número entero.")
        return

    estudiante = next((e for e in estudiantes if e.get('id') == id_est), None)
    if not estudiante:
        print("\n Estudiante con ese ID no encontrado.")
        return

    # Seleccionar materia
    print(f"\nAsignando nota a: {estudiante.get('nombre','')} {estudiante.get('apellido','')}\n")
    print("Materias disponibles:\n")
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

    # Ingresar y validar la nota
    try:
        nota = float(input(f"Ingrese la nota para {materia} (0-100): "))
    except ValueError:
        print("\n Error: Nota inválida. Ingrese un número.")
        return

    if not (0 <= nota <= 100):
        print("\n La nota debe ser un valor entre 0 y 100.")
        return

    # Asegurar que la clave 'nota' exista y sea un diccionario.
    # Si existe una clave antigua 'calificaciones', migramos su contenido para compatibilidad.
    if 'nota' not in estudiante or not isinstance(estudiante.get('nota'), dict):
        estudiante['nota'] = {}
        if 'calificaciones' in estudiante:
            cal = estudiante.get('calificaciones')
            if isinstance(cal, dict):
                estudiante['nota'].update(cal)
            elif isinstance(cal, list):
                for i, v in enumerate(cal, start=1):
                    estudiante['nota'][f'Nota{i}'] = v

    estudiante['nota'][materia] = nota
    # Mantener compatibilidad con la clave antigua 'calificaciones'
    estudiante['calificaciones'] = dict(estudiante['nota'])

    print(f"\nNota asignada: {estudiante.get('nombre','')} {estudiante.get('apellido','')} | {materia}: {nota:.2f}\n")


if __name__ == "__main__":
    # Este módulo está pensado para ser importado desde `main.py`.
    # Ejecutar funciones de interfaz aquí puede provocar errores porque
    # `menu_principal` está definido en `main.py`. Solo mostrar ayuda.
    print("Módulo de calificaciones. Importar desde `main.py` para usar la aplicación.")





