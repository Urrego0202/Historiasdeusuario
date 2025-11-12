"""13. Parqueadero “AutoLoop” - Control de vehículos
Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
Si entra un número par, mostrar “Vehículo par registrado”.
Si el total llega a 20, mostrar “Capacidad completa”."""

vehiculo = 21
contador = 1

while contador < vehiculo:
    if contador % 2:
        print(f"Vehiculo {contador}")
    else:
        print(f"Vehiculo par registrado {contador}")
    contador += 1