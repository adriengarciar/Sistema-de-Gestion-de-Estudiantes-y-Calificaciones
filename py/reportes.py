def menu_reportes(lista):
    while True:
        print("\n===== MENU DE REPORTES =====")
        print("1. Mejor estudiante")
        print("2. Peor estudiante")
        print("3. Nota promedio")
        print("4. Cantidad de estudiantes")
        print("5. Aprobados")
        print("6. Reprobados")
        print("7. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mejor = obtener_mejor_estudiante(lista)
            if mejor:
                print(f"Mejor estudiante: {mejor['nombre']} ({mejor['calificacion']})")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "2":
            peor = obtener_peor_estudiante(lista)
            if peor:
                print(f"Peor estudiante: {peor['nombre']} ({peor['calificacion']})")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "3":
            print(f"Promedio general: {calcular_promedio(lista):.2f}")

        elif opcion == "4":
            print(f"Cantidad total de estudiantes: {contar_estudiantes(lista)}")

        elif opcion == "5":
            print(f"Aprobados: {contar_aprobados(lista)}")

        elif opcion == "6":
            print(f"Reprobados: {contar_reprobados(lista)}")

        elif opcion == "7":
            break

        else:
            print("Opción no válida. Intente de nuevo.")