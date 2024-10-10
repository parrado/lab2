# Se deben codificar las siguientes funciones y replicar la funcionalidad descrita en los comentarios
# Además, para la gestión de usuarios y preguntas se debe hacer uso de archivos

# La función recibe name y password
# Si el usuario ya existe deber retornar  "User already registered"
# Si el usuario no existe debe registrarlo y retornar  "User succesfully registered"
def registerUser(name,password):
    pass
            

# Función que abre o cierra una sesión
# Abre/cierra una sesión del usuario dependiendo del valor de flag 
# lo hace si el nombre de usuario y la contraseña son correctos
# Si la sesión se pudo abrir/cerrar debe retornar "Session was succesfully opened/closed" de lo contrario
# debe retornar "error"
def openCloseSession(name,password,flag):
    pass

# Función que actualiza el puntaje
# Actualiza el puntaje del usuario con el valor de score si el nombre de usuario y la contraseña 
# son correctos y si el usuario se encuentra con sesión abierta
# Si se pudo actualizar el puntaje debe retornar "Score was succesfully updated" de lo contrario
# debe retornar "error"
def updateScore(name,password,score):
    pass


# Función que lee el puntaje
# Retorna el puntaje del usuario si el nombre de usuario y la contraseña 
# son correctos y si el usuario se encuentra con sesión abierta
# Si se pudo leer el puntaje debe retornar el puntaje de lo contrario
# debe retornar "error"
def getScore(name,password):
    pass

# Función que lee la lista de usuarios conectados
# retorna una lista con los usuarios conectados, solo debe devolver nombre y puntaje
# si el nombre de usuario y la contraseña  son correctos y si el usuario se encuentra con sesión abierta
# de lo contrario debe retornar "error"
def usersList(name,password):
    pass
            
    
# Función que genera una pregunta en una categoría cat
# retorna la pregunta si el nombre de usuario y la contraseña  son correctos y si el usuario se encuentra con sesión abierta
# de lo contrario debe retornar "error"
def question(name,password,cat):
    pass
                
                
            
        
    
            
    
