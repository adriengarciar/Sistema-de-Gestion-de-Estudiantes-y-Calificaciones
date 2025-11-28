# Lista de estudiantes
def lista_estudiantes(estudiantes):
    print("\nLos estudiantes registrados son:\n")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for est in estudiantes:
        id = est.get('id') if est.get('id') is not None else est.get('ID')
        nombre = est.get('nombre') or est.get('Nombre')
        apellido = est.get('apellido') or est.get('Apellido')
        nota = est.get('nota') or est.get('Nota') or est.get('calificaciones')
        print(f"ID: {id} | Nombre: {nombre} {apellido} | Nota: {nota}")
