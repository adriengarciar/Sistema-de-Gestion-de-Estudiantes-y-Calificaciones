# Lista donde se almacenan todos los estudiantes
estudiantes = []

#Diccionario base para crear los nuevos estudiantes
estudiante_base = {
    "nombre": "",
    "apellido": "",
    "calificaciones": None
}

# FUNCIONES A IMPORTAR

#from calificaciones import 
#from registro import 
#from reportes import

#          MENÚ PRINCIPAL

def menu_principal():
    while True:
        print("\n==============================")
        print("  SISTEMA DE ESTUDIANTES")
        print("==============================")
        print("1. Registrar estudiante")
        print("2. Asignar nota")
        print("3. Lista de estudiantes")
        print("4. Generar reportes de notas")
        print("5. Ranking global")
        print("6. Buscar estudiante por nombre")
        print("9. Salir")
        print("==============================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante(estudiantes, estudiante_base)

        elif opcion == "2":
            asignar_nota(estudiantes)

        elif opcion == "3":
            listar_estudiantes(estudiantes)

        elif opcion == "4":
            generar_reportes(estudiantes)

        elif opcion == "5":
            ranking_global(estudiantes)

        elif opcion == "6":
            buscar_estudiante(estudiantes)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()

