print("Hola mundo")


"""door = False

if door:
    print("Entre a la casa")
else:
    print("No entre a la casa")

print("Fin del programa")""" 

#QUE VALIDE LA EDAD DE UNA PERSONA Y DIGA SI ES MAYOR DE EDAD O MENOR DE EDAD

"""edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")"""

"""n = int(input("Ingresa un numero: "))
while n > 0:
    if n % 2 == 0:
        print(f"{n} es un numero par")
    else:
        print(f"{n} es un numero impar")
        n = n - 1
    print("Fin del progrma")"""

"""for i in range(10):
    for j in range(10):
        print(f"(i:{i}, j:{j})")"""

"""print("Bienvenido a la tienda de Don Panchito")

Pan = 300

cantidad = float(input("Ingrese la cantidad de panes que desea comprar: "))

if cantidad >= 20:
    print("Tiene un descuento del 10% y el total a pagar es:", (Pan * cantidad) * 0.9)
elif cantidad >= 50:
    print("Tiene un descuento del 20% y el total a pagar es:", (Pan * cantidad) * 0.20)
elif cantidad < 0:
    print("Cantidad inválida")
else:
    print("No tiene descuento y el total a pagar es:", Pan * cantidad)

    Calcula el total a pagar por la cantidad de panes.

    Reglas:
    - Si cantidad < 0 -> devuelve la cadena "Cantidad inválida"
    - Si cantidad > 50 -> 20% de descuento
    - Si cantidad > 20 -> 10% de descuento
    - En otro caso -> sin descuento
    """
# ------------------------------------------------------------------------------

"""print("GIMNASIO / SOLO LEVELING")
#Mostrar mensaje y si aplica, los puntos ganados.
diasentrenados = int(input("¿Cuántos días entrenaste esta semana?: "))
puntodeenergia = 0
#Pedir cuántos días entrenó esta semana
if diasentrenados >= 4:
    print("!Excelente Disciplina")
    puntodeenergia = 1
elif diasentrenados < 4:
    print("Bien, pero puedes mejorar")
elif diasentrenados < 2:
    print("No aflojes, tú puedes mejorar")
else:
    print("Debes comenzar a entrenar de nuevo")

if puntodeenergia > 0:
    print("Has ganado", puntodeenergia, "punto de energía")
else:
    print("No has ganado puntos de energía")"""

# ------------------------------------------------------------------------------
"""Libro cuesta $25.000.

Si es estudiante → 15% descuento
Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado
Validar:

Si no es estudiante, el cupón no aplica.
Si ingresa cupón incorrecto, ignorarlo.
Mostrar total."""

print("LIBRERIA EL SABER")

libro = 25000

esestudiante = input("¿Eres estudiante? (si/no): ").lower()
if esestudiante == "si":
    total = libro * 0.85
    cupon = input("Ingrese cupón si tiene(En caso de no tener, presiona la tecla ENTER): ")
    if cupon == "LIBRO10":
        total = total * 0.9
else:
    total = libro

print("Total a pagar:", total)

# ------------------------------------------------------------------------------

# Restaurante - El Sabor Colombiano

"""Opciones bebida:

sí → $3.000
no → $0
Luego aplicar IVA del 8% al total final.
Mostrar valor con IVA incluido."""

"""print("RESTAURANTE EL SABOR COLOMBIANO")
menu = 12000
bebida = input("¿Desea bebida? (si/no): ").lower()
if bebida == "si":
    total = menu + 3000
else:
    total = menu
iva = total * 0.08
total_final = total + iva
print("Total a pagar con IVA incluido:", total_final)"""

# ------------------------------------------------------------------------------

# Supermercado “AhorroMax”

"""Cada producto cuesta $2.000.

Reglas:

30 unidades → 15% descuento

10 unidades → 5% descuento

Si el total después del descuento es < $50.000 → agregar $5.000 de envío
Calcular total final."""

"""print("SUPERMERCADO AHORROMAX")
producto = 2000
unidades = int(input("Ingrese las unidades que desea comprar: "))
total = producto * unidades

if unidades >= 30:
    descuento = total * 0.85
elif unidades >= 10:
    descuento = total * 0.95
else:
    descuento = 0

if descuento < 50000:
    envio = 5000
else:
    envio = 0
total_final = descuento + envio
print("Total a pagar:", total_final)"""

