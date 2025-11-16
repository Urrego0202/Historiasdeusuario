
                        # HISTORIA DE USUARIO - SEMANA 1

#Solicitar datos al usuario
nombre = str(input("Ingresa nombre del producto: "))
precio = float(input("Ingresa el precio: "))
cantidad = int(input("Ingresa la cantidad: "))

#Revisar valores
while precio <= 0 or cantidad <= 0:
    if precio <= 0:
        precio = float(input("Ingresa el precio: "))
    elif cantidad <= 0:
        cantidad = int(input("Ingresa la cantidad: "))

#Operación para saber el total
costo_total = precio * cantidad

#Se imprime el inventario con sus variables ingresadas
print(f"Nombre: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

#El programa funciona para ingresar productos al inventario de una tienda
# donde encontramos el nombre del producto, valor, cantidad y el costo que
# se multiplica por cada unidad para saber el total de este.