"""Como supervisor, quiero que un for muestre los productos 
fabricados del 1 al número que indique el usuario.
Si el número es par, mostrar “Producto verificado”.
Si es impar, mostrar “Producto pendiente”."""

numerouser = int(input("Ingresa un numero: "))

for numerouser in range(1, numerouser + 1):
    if numerouser % 2 == 0:
        print(f"Producto {numerouser} verificado")
    else:
        print(f"Producto {numerouser} pendiente")