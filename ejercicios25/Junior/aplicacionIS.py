"""20. Aplicación “Inicio Seguro” - Intentos de inicio de sesión
Como usuario, quiero usar un while con máximo 3 intentos de contraseña.
Si acierto, mostrar “Acceso permitido”.
Si agoto los intentos, mostrar “Acceso denegado”."""

passwordCorrect = "hola123"
passworduser = ""
intentos = 0
maxintentos = 3

while intentos < maxintentos:
    passworduser = str(input("Ingresa la contraseña: "))
    
    if passworduser == passwordCorrect:
        print("Acceso permitido")
        break
    intentos += 1
    
else:
    print("Acceso denegado")



