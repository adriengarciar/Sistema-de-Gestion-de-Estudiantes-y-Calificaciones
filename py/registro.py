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
 return nombre, apellido
            
nombre, apellido = registrar_alumnos()

alumno = {
        'Nombre': nombre,
        'Apellido': apellido,
        
}

