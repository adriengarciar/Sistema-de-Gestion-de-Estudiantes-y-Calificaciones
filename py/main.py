# Lista donde se almacenan todos los estudiantes
estudiantes = []

#Diccionario base para crear los nuevos estudiantes
# estudiante_base = {
#     "iD", ""
#     "nombre": "",
#     "apellido": "",
#     "calificaciones": None
# }

# FUNCIONES A IMPORTAR

from calificaciones import asignar_nota
from registro import registrar_alumnos
from listaestudiantes import lista_estudiantes
# from reportes import


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

        opcion = input("\nSeleccione una opción: \n")

        if opcion == "1":
            nombre, apellido, nota = registrar_alumnos()

            stu1 = {
                'id': len(estudiantes) + 1,
                'nombre': nombre,
                'apellido': apellido,
                'nota': nota,
            }

            estudiantes.append(stu1)

            print("Datos obtenidos:")
            print(f"ID: {stu1['id']}")
            print(f"{nombre} {apellido} | {nota:.2f}")
            registrar_alumnos()

        elif opcion == "2":
            asignar_nota(estudiantes)

        elif opcion == "3":
            lista_estudiantes(estudiantes)
            
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