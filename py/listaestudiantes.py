
# Lista de estudiantes 
def lista_estudiantes(estudiantes):
    print("\nLos estudiantes registrados son:\n")
    for estudiante in estudiantes:
        print(f"- {estudiante["nombre"]} {estudiante["apellido"]}")
