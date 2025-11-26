def registrar_alumnos():
    
    def validar_nombre(nombre):
        if nombre.strip() == '':
            print('Error, por favor intente colocar algo')
            return False
            
        elif " " in nombre.strip():
            print("Solo coloque un nombre, sin espacios.")
            return False

        
        elif not nombre.isalpha():
                print('error, por favor intente sin numeros')
                return False
            
   
        return True
        
        
    def validar_apellido(apellido):
        if apellido.strip() == '':
            print('Error, por favor intente colocar algo')
            return False
            
        elif " " in nombre.strip():
            print("Solo coloque un apellido, sin espacios.")
            return False

        
        elif not apellido.isalpha():
                print('error, por favor intente de nuevo')
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
            nombre = nombre.capitalize()
            break
    while True:
        
        apellido = input('Ingrese el apellido del estudiante: ')
        if validar_apellido(apellido):
            apellido = apellido.capitalize()
            break
        
    while True:
        
        nota = input('Ingrese la nota acumulada del estudiante: ')
        nota_valida = validar_nota(nota)
        if nota_valida:
            nota = nota_valida
            break
      
    return nombre, apellido, nota
            
            
                    
nombre, apellido, nota = registrar_alumnos()


alumno = {
        'Nombre': nombre,
        'Apellido': apellido,
        'Nota': nota,
        }

 return alumno
