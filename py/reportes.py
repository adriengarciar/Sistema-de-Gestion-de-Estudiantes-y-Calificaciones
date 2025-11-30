def menu_reportes(lista):

    # Funciones auxiliares para calcular promedios y conteos
    def _grades_list(est):
        """Devuelve una lista de calificaciones numéricas para un estudiante."""
        cal = est.get('calificaciones') if est.get('calificaciones') is not None else est.get('nota')
        if isinstance(cal, dict):
            return [v for v in cal.values() if isinstance(v, (int, float))]
        if isinstance(cal, list):
            return [v for v in cal if isinstance(v, (int, float))]
        return []

    def _student_avg(est):
        grades = _grades_list(est)
        return sum(grades) / len(grades) if grades else 0

    def obtener_mejor_estudiante(lista):
        if not lista:
            return None
        return max(lista, key=_student_avg)

    def obtener_peor_estudiante(lista):
        if not lista:
            return None
        return min(lista, key=_student_avg)

    def calcular_promedio(lista):
        if not lista:
            return 0
        avgs = [_student_avg(est) for est in lista]
        return sum(avgs) / len(avgs) if avgs else 0

    def contar_estudiantes(lista):
        return len(lista)

    def contar_aprobados(lista):
        return sum(1 for est in lista if _student_avg(est) >= 70)

    def contar_reprobados(lista):
        return sum(1 for est in lista if _student_avg(est) < 70)

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
                print(f"Mejor estudiante: {mejor.get('nombre','')} ({_student_avg(mejor):.2f})")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "2":
            peor = obtener_peor_estudiante(lista)
            if peor:
                print(f"Peor estudiante: {peor.get('nombre','')} ({_student_avg(peor):.2f})")
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

def generar_reportes(lista):
    """Generador de reportes mínimo: muestra conteos y promedio general."""
    print("\n===== REPORTES BÁSICOS =====")
    print(f"Cantidad total de estudiantes: {len(lista)}")
    all_grades = []
    for s in lista:
        cal = s.get('calificaciones') or {}
        if isinstance(cal, dict):
            all_grades.extend([v for v in cal.values() if isinstance(v, (int, float))])
        elif isinstance(cal, list):
            all_grades.extend([v for v in cal if isinstance(v, (int, float))])
    promedio = sum(all_grades) / len(all_grades) if all_grades else 0
    print(f"Promedio general: {promedio:.2f}")


def ranking_global(lista):
    """Imprime un ranking global por promedio descendente."""
    ranking = []
    for s in lista:
        cal = s.get('calificaciones') or {}
        grades = []
        if isinstance(cal, dict):
            grades = [v for v in cal.values() if isinstance(v, (int, float))]
        elif isinstance(cal, list):
            grades = [v for v in cal if isinstance(v, (int, float))]
        promedio = sum(grades) / len(grades) if grades else 0
        ranking.append({
            'id': s.get('id'),
            'nombre': s.get('nombre'),
            'apellido': s.get('apellido'),
            'promedio': promedio
        })

    ranking.sort(key=lambda x: x['promedio'], reverse=True)

    print("\n===== RANKING GLOBAL =====")
    if not ranking:
        print("No hay estudiantes para mostrar.")
        return
    for i, r in enumerate(ranking, start=1):
        print(f"{i}) ID {r['id']} - {r['nombre']} {r['apellido']} - Promedio: {r['promedio']:.2f}")