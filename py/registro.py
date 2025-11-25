def registrar_alumnos():
    
    def validar_nombre(nombre):
        if nombre.strip() == '':
            print('Error, por favor intente colocar algo')
            return False
            
        elif not nombre.isalpha():
                print('error, por favor intente sin numeros')
                return False

        return True
        
        
    def validar_apellido(apellido):
        if apellido.strip() == '':
            print('Error, por favor intente colocar algo')
            return False
            
        elif not apellido.isalpha():
                print('error, por favor intente sin numeros')
                return False
        return True
            
    def validar_nota(nota):
        
        try:
            acumulado = float(nota)
        except ValueError:
            print('Ingrese una entrada valida.(Un acumulado decimal)')
            return False
            
        if acumulado < 0.0 or acumulado > 100.0:
            print('Esta nota excede los rangos aceptables')
            return False
      

        return True
            
    while True:
      
        nombre = input('Ingrese el nombre del estudiante: ')
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
            
            

                    
nombre, apellido, nota = registrar_alumnos()


print("Datos obtenidos:")
print(f"{nombre} {apellido} | {nota:.2f}")




