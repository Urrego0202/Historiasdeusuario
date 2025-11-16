
                        # HISTORIA DE USUARIO - SEMANA 2
# Inicializar inventario como una lista vacía
"""inventario = []

while True:
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Calcular Estadísticas")
    print("4. Salir")

    opcionuser = int(input("Elige una opción del menú: "))

    if opcionuser <=0 or opcionuser >=5:
        print("Opción inválida")
    
    elif opcionuser == 1:
        nombre = str(input("Ingresa nombre del producto: "))
        precio = float(input("Ingresa precio del producto: "))
        cantidad = int(input("Ingresa cantidad del producto: "))

        producto = {"nombre":nombre, "precio":precio, "cantidad":cantidad}
        inventario.append(producto)
          
    elif opcionuser == 2:
        
        if len(inventario) == 0:
            print("El inventario está vacio")
        else:
            for producto in inventario:
                print(f"Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")

    elif opcionuser == 3:
        valortotal_inventario = precio * cantidad
        print(f"El valor total del inventario es: {valortotal_inventario}")
        
        total_productos = len(inventario)
        print(f"Productos en el inventario: {total_productos}")
        
    elif opcionuser == 4:
        print("FIN DEL PROGRAMA")
        break"""
    
# ESTRUCTURANDO EL CÓDIGO EN FUNCIONES

inventario = [] # Lista vacía para agregar diccionario

def agregar_producto(): #Función para agregar productos al inventario
    nombre_producto = str(input("Ingresa el nombre del producto: "))
    precio_producto = float(input("Ingresa el precio del producto: "))
    cantidad_producto = int(input("Ingresa la cantidad del producto: "))
    
    producto = {"nombre":nombre_producto, "precio":precio_producto, "cantidad":cantidad_producto}
    inventario.append(producto) 
    
def mostrar_inventario(): # Función para mostrar el inventario
    if len(inventario) == 0:
            print("El inventario está vacio")
    else:
        for producto in inventario:
            print(f"Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
    
def calcular_estadistica(): #Función para calcular estadisticas
    
    if len(inventario) == 0:
        print("El inventario está vacío. No hay estadísticas para mostrar.")
    else:
        total_productos = len(inventario)
        print(f"Productos en el inventario: {total_productos}")
    
        for producto in inventario:
                valor_producto = producto['precio'] * producto['cantidad']
                valor_total = 0
                valor_total += valor_producto
        print(f"El valor total del inventario es: {valor_total}")
        
    
while True: # Menú de opciones para el usuario
    print("1. Agregar Producto")
    print("2. Mostrar Inventario")
    print("3. Calcular Estadísticas")
    print("4. Salir")
    
    opcion_user = int(input("Elige una opción del menú: "))

    if opcion_user <=0 or opcion_user >=5: # Validar que elija un número del menú
        print("Opción inválida")
        
    elif opcion_user == 1:
        agregar_producto()
        
    elif opcion_user == 2:
        mostrar_inventario()

    elif opcion_user == 3:
        calcular_estadistica()
        
    elif opcion_user == 4:
        print("FINAL DEL PROGRAMA")
        break
    

    
