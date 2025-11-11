"""2. Cine “La Estrella” - Cuenta regresiva antes de iniciar la función
Como proyeccionista, quiero mostrar una cuenta regresiva del 5 al 1 usando for. Si llega al número 1, debe imprimir “¡Que empiece la función!”."""

contador = [5,4,3,2,1,0]

for numero in contador:
    if numero < 1:
        print("¡Que empiece la función!")
    else:
        print(numero)
    