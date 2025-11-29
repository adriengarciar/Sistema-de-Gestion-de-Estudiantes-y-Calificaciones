estudiantes = []

def registrar_alumnos():
    def validar_nombre(nombre):
        if nombre.strip() == '':
            print('Error, por favor intente colocar algo')
            return False
        if ' ' in nombre.strip():
            print('Solo coloque un nombre, sin espacios.')
            return False
        if not nombre.isalpha():
            print('Error, por favor intente sin números')
            return False
        return True

    def validar_apellido(apellido):
        if apellido.strip() == '':
            print('Error, por favor intente colocar algo')
            return False
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
        if validar_nombre(nombre):
            break

    while True:
        apellido = input('Ingrese el apellido del estudiante: ')
        if validar_apellido(apellido):
            break

    while True:
        nota = input('Ingrese la nota acumulada del estudiante: ')
        if validar_nota(nota):
            nota = float(nota)
            break

    return nombre, apellido, nota




