"""4. Tienda “Descuento Express” - Clientes atendidos
Como cajero, quiero usar un for que muestre “Atendiendo cliente número X” del 1 al 8. Si el cliente es el número 8, mostrar “Último cliente del día”."""

clienteatendido = 0

for clienteatendido in range(1,9):
    if clienteatendido < 8:
        print(f"Atendiendo cliente número: {clienteatendido}")
    else:
        print(f"Último cliente del día: {clienteatendido}")
        break