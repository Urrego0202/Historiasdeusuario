"""9. Concurso “Adivina el número secreto”
Como participante, quiero que el programa me pida un número entre 1 y 5 usando un while.
Si acierto, mostrar “¡Correcto!”.
Si no, mostrar “Intenta otra vez” y seguir hasta acertar."""

numeroCorrecto = 3
numeroUser = ""

while numeroUser != numeroCorrecto:
    numeroUser = int(input("Ingresa un numero entre 1 y 5: "))
    print("Intenta otra vez")
else:
    print("!Correcto¡")