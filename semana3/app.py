#MERCADO
import servicios
import archivos

inventario = [
    {"nombre": "pan", "precio": 250, "cantidad": 71},
    {"nombre": "aceite", "precio": 120, "cantidad": 34},
    {"nombre": "pollo", "precio": 340, "cantidad": 43}
]

while True:
    print("""
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Calcular estadisticas
7. Guardar inventario en csv
8. Cargar inventario desde csv
9. Salir del programa
""")
    
    opcioneuser = int(input("Elige una opción del inventario: "))
    
    if opcioneuser <= 0 or opcioneuser >=10:
        print("Opción Inválida")
        
    elif opcioneuser == 1:
        nombre = (input("Ingresa el nombre del producto: "))
        precio = float(input("Ingresa el precio del producto: "))
        cantidad = int(input("Ingresa la cantidad del producto: "))
        servicios.agregar_producto(inventario, nombre, precio, cantidad)

    elif opcioneuser == 2:
        servicios.mostrar_inventario(inventario)

    elif opcioneuser == 3:
        nombre = input("Ingresa el nombre del producto a buscar: ")
        servicios.buscar_producto(inventario, nombre)
        
    elif opcioneuser == 4:
        nombre = input("Ingresa el nombre del producto a actualizar: ")
        servicios.actualizar_producto(inventario, nombre, nuevo_precio = None, nueva_cantidad = None)
        
    elif opcioneuser == 5:
        nombre = input("Ingresa el nombre del producto a eliminar: ")
        servicios.eliminar_producto(inventario, nombre)    
        
    elif opcioneuser == 6:    
        estadisticas = servicios.calcular_estadisticas(inventario)
        print(f"Unidades totales: {estadisticas["unidades_totales"]}")
        print(f"Valor total: {estadisticas["valor_total"]}")
        print(f"Producto más caro: {estadisticas['producto_mas_caro']['nombre']} | Precio: {estadisticas['producto_mas_caro']['precio']}")
        print(f"Producto mayor stock: {estadisticas['producto_mayor_stock']['nombre']} {estadisticas['producto_mayor_stock']['cantidad']} unidades")
     
    elif opcioneuser == 7: 
        ruta = input("Ingresa la ruta para guardar el archivo CSV: ")
        archivos.guardar_csv(inventario, ruta)
        
    elif opcioneuser == 8:
        ruta = input("Ingresa la ruta del archivo CSV: ")
        productos_nuevos = archivos.cargar_csv(ruta)
    
        if productos_nuevos is not None:
            if len(productos_nuevos) == 0:
                print("No se cargaron productos válidos")
            else:
                # Preguntar qué hacer con el inventario actual
                opcion_carga = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
                
                if opcion_carga == 'S':
                    # Reemplazar inventario
                    inventario.clear()
                    inventario.extend(productos_nuevos)
                    print(f"\nInventario reemplazado: {len(productos_nuevos)} producto(s) cargado(s)")
                
                elif opcion_carga == 'N':
                    # Fusionar inventarios
                    print("\nPolítica de fusión:")
                    print("- Si el producto existe: se suma la cantidad y se actualiza el precio")
                    print("- Si el producto no existe: se agrega al inventario\n")
                    
                    agregados, actualizados = archivos.fusionar_inventarios(inventario, productos_nuevos)
                    
                    print(f"\nFusión completada:")
                    print(f" - {agregados} producto(s) nuevo(s) agregado(s)")
                    print(f" - {actualizados} producto(s) actualizado(s)")
                    print(f" - Total en inventario: {len(inventario)} producto(s)")
                
                else:
                    print("Opción inválida. Operación cancelada.")
                
    elif opcioneuser == 9:
        print("FIN DEL PROGRAMA")
        break


