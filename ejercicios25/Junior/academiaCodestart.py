"""Academia “CodeStart” - Contador de ejercicios completados
Como estudiante, quiero usar un for del 1 al número que indique.
Si el número es múltiplo de 5, mostrar “¡Gran avance!”.
Si no, solo mostrar “Ejercicio X completado”."""

numerouser = int(input("Ingresa un numero: "))

for ejercicio in range(1, numerouser + 1):
    if ejercicio % 5 == 0:
        print(f"Ejercicio {ejercicio} completado ¡Gran avance!")
    else:
        print(f"Ejercicio {ejercicio} completado")