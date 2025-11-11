"""1. Cafetería “Buen Café” - Control de tazas servidas
Como barista, quiero usar un bucle for para mostrar cuántas tazas he servido del 1 al 10, pero si el número es 5, mostrar el mensaje “¡Mitad del turno completada!”."""

tazasservidas = 0

for tazasservidas in range(1, 11):
    if tazasservidas == 5:
        print("¡Mitad del turno completada!") 
    else:
        print(f"Taza servida número: {tazasservidas}")