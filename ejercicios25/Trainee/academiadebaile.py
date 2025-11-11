"""8. Academia de baile - Calentamiento previo
Como instructor, quiero usar un while para contar del 1 al 5.
Si el número es menor que 5, mostrar “Sigue calentando...”, y si llega a 5, mostrar “¡Listo para bailar!”."""

contador = 1

while contador < 5:
    print("Sigue calentando...")
    if contador == 4:
        print("!Listo para bailar¡")
        break
    contador += 1 