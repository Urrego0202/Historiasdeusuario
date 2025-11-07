"""Cine “La Estrella” — Tarifas por edad
Pedir la edad del cliente:

Edad	    Precio
< 5 años	Entrada gratis
5 a 11	    $5.000
12 a 59	    $8.000
≥ 60	    $4.000 (descuento adulto mayor)
Mostrar el precio.
Si la edad es negativa, mostrar error."""

print("Bienvenido al Cine La Estrella")

edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Edad no valida")
elif edad < 5:
    print("La entrada es gratis")
elif 5 <= edad <= 11:
    print("El precio de la entrada es de: $5.000")
elif 12 <= edad <= 59:
    print("El precio de la entrada es de: $8.000")
else:
    print("El precio de la entrada con descuento (adulto mayor) es de: $4.000 ")



