import csv
# Funciones del inventario

"""agregar_producto(inventario, nombre, precio, cantidad)
mostrar_inventario(inventario)
buscar_producto(inventario, nombre) → retorna el dict o None
actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
eliminar_producto(inventario, nombre)
calcular_estadisticas(inventario) → retorna tupla/dict con métricas"""

def agregar_producto(inventario, nombre, precio, cantidad): 
    try:
        # Convertir a los tipos correctos
        precio = float(precio)
        cantidad = int(cantidad)
        
        # Validar que no sean negativos
        if precio < 0:
            print("Error: El precio no puede ser negativo")
            return False
        
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa")
            return False
        
        # Validar que el nombre no esté vacío
        if not nombre or nombre.strip() == "":
            print("Error: El nombre no puede estar vacío")
            return False
        
        # Crear y agregar el producto
        producto = {"nombre": nombre.strip(), "precio": precio, "cantidad": cantidad}
        inventario.append(producto)
        print("\n---------------Producto agregado---------------")
        return True
        
    except ValueError:
        print("Error: El precio debe ser un número decimal y la cantidad un número entero")
        return False
    
def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("El inventario está vacío")    
    else:
        for producto in inventario:
            print(f"Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
            return producto
    return None
    
def actualizar_producto (inventario, nombre, nuevo_precio = None, nueva_cantidad = None):

    for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
            if nuevo_precio is None:
                nuevo_precio = float(input(f"Ingresa el nuevo precio del {nombre}: "))
                producto["precio"] = nuevo_precio
            if nueva_cantidad is None:
                nueva_cantidad = int(input(f"Ingresa la nueva cantidad del {nombre}: "))
                producto["cantidad"] = nueva_cantidad
            print("Producto actualizado")
            return
    print("Producto no encontrado, asegurate de copiarlo correctamente.")
    
def eliminar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            print(f"Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
            inventario.remove(producto)
            print("Producto eliminado")
            return
    print("Producto no encontrado, asegurate de copiarlo correctamente.")
    

"""Implementa calcular_estadisticas(inventario) para obtener:
unidades_totales = suma de cantidad
valor_total = suma de precio * cantidad
producto_mas_caro (nombre y precio)
producto_mayor_stock (nombre y cantidad)
Muestra las estadísticas con formato legible."""

def calcular_estadisticas(inventario):
    unidades_totales = sum(producto["cantidad"] for producto in inventario)
    valor_total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)
    producto_mas_caro = max(inventario, key = lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key = lambda p: p["cantidad"])
    
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": {"nombre": producto_mas_caro["nombre"], "precio": producto_mas_caro["precio"]},
        "producto_mayor_stock": {"nombre": producto_mayor_stock["nombre"], "cantidad": producto_mayor_stock["cantidad"]}
    }


    
