<<<<<<< HEAD
=======
estudiantes = []

>>>>>>> 96a591da1220bc0dc08bc038c005e7afa7da8657
def registrar_alumnos():
    def validar_nombre(nombre):
        if nombre.strip() == '':
            print('Error, por favor intente colocar algo')
            return False
<<<<<<< HEAD
        elif " " in nombre.strip():
            print("Solo coloque un nombre, sin espacios.")
            return False
        elif not nombre.isalpha():
            print('error, por favor intente sin numeros')
=======
        if ' ' in nombre.strip():
            print('Solo coloque un nombre, sin espacios.')
            return False
        if not nombre.isalpha():
            print('Error, por favor intente sin números')
>>>>>>> 96a591da1220bc0dc08bc038c005e7afa7da8657
            return False
        return True

    def validar_apellido(apellido):
        if apellido.strip() == '':
            print('Error, por favor intente colocar algo')
            return False
<<<<<<< HEAD
        elif " " in apellido.strip():
            print("Solo coloque un apellido, sin espacios.")
            return False
        elif not apellido.isalpha():
            print('error, por favor intente de nuevo')
            return False
        return True

    while True:
        nombre = input('Ingrese el nombre del estudiante: ')
=======
        if ' ' in apellido.strip():
            print('Solo coloque un apellido, sin espacios.')
            return False
        if not apellido.isalpha():
            print('Error, por favor intente de nuevo')
            return False
        return True

    def validar_nota(nota):
        try:
            acumulado = float(nota)
        except ValueError:
            print('Ingrese una entrada válida. (Un acumulado decimal)')
            return False
        if acumulado < 0.0 or acumulado > 100.0:
            print('Esta nota excede los rangos aceptables')
            return False
        return True

    while True:
        nombre = input('\nIngrese el nombre del estudiante: ')
>>>>>>> 96a591da1220bc0dc08bc038c005e7afa7da8657
        if validar_nombre(nombre):
            break

    while True:
        apellido = input('Ingrese el apellido del estudiante: ')
        if validar_apellido(apellido):
<<<<<<< HEAD
            apellido = apellido.capitalize()
            break

    return nombre, apellido
=======
            break

    while True:
        nota = input('Ingrese la nota acumulada del estudiante: ')
        if validar_nota(nota):
            nota = float(nota)
            break

    return nombre, apellido, nota



>>>>>>> 96a591da1220bc0dc08bc038c005e7afa7da8657


if __name__ == "__main__":
    nombre, apellido = registrar_alumnos()
    print(f'Nombre: {nombre}, Apellido: {apellido}')
