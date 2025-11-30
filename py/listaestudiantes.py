# Lista de estudiantes
def lista_estudiantes(estudiantes): 
    print("\n==============================")
    print("\nLos estudiantes registrados son:\n")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        print("\n==============================")
        return
    for est in estudiantes:
        id = est.get('id') if est.get('id') is not None else est.get('ID')
        nombre = est.get('nombre') or est.get('Nombre')
        apellido = est.get('apellido') or est.get('Apellido')
        nota = est.get('nota') or est.get('Nota') or est.get('calificaciones')
        
        if isinstance(nota, dict):
            nota = " | ".join([f"{mat}: {val}" for mat, val in nota.items()])
        elif nota is None:
            nota = "Sin notas"
        
        print(f"ID: {id} | Nombre: {nombre} {apellido} | Nota: {nota}")
        print("\n==============================\n")
