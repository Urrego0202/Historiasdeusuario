"""12. Gimnasio “Level Up” - Control de repeticiones
Como deportista, quiero ingresar un número de repeticiones y usar 
un for para imprimir “Repetición X completada”.
Si X es divisible por 3, mostrar además “¡Excelente ritmo!”."""

repeticiones = int(input("Ingresa el número de repeticiones: "))

for repeticion in range(1, repeticiones, + 1):
    if repeticion % 3 == 0:
        print(f"Repetición {repeticion} completada !Excelente ritmo¡")
    else:
        print(f"Repetición {repeticion} completada")