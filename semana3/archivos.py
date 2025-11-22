import csv

def guardar_csv(inventario, ruta, incluir_header=True): #Exportar inventario actual a csv
    if len(inventario) == 0:
        print("El inventario está vacío, no se puede guardar.")
        return
    
    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            if incluir_header:
                escritor_csv.writerow(["nombre", "precio", "cantidad"])
            for producto in inventario:
                escritor_csv.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
        print(f"Inventario guardado en: {ruta}")
    except IOError:
        print("Error al guardar el archivo. Verifica los permisos o la ruta especificada.")



def cargar_csv(ruta): # Cargar inventario anteriormente guardado en csv
    """Carga productos desde un archivo CSV"""
    productos_cargados = []
    filas_invalidas = 0
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            
            # Leer y validar encabezado
            try:
                encabezado = next(lector)
                if encabezado != ['nombre', 'precio', 'cantidad']:
                    print("Error: El encabezado debe ser exactamente: nombre,precio,cantidad")
                    return None
            except StopIteration:
                print("Error: El archivo está vacío")
                return None
            
            # Leer cada fila
            for numero_fila, fila in enumerate(lector, start=2):
                # Validar que tenga 3 columnas
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                
                try:
                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])
                    
                    # Validar que no sean negativos
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue
                    
                    # Validar que el nombre no esté vacío
                    if not nombre:
                        filas_invalidas += 1
                        continue
                    
                    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
                    productos_cargados.append(producto)
                    
                except ValueError:
                    filas_invalidas += 1
                    continue
        
        # Informar sobre filas inválidas
        if filas_invalidas > 0:
            print(f"{filas_invalidas} fila(s) inválida(s) omitida(s)")
        
        return productos_cargados
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta}'")
        return None
    except UnicodeDecodeError:
        print(f"Error: El archivo '{ruta}' no tiene codificación UTF-8 válida")
        return None
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {e}")
        return None


def fusionar_inventarios(inventario_actual, productos_nuevos):
    """Fusiona productos nuevos con el inventario actual"""
    productos_agregados = 0
    productos_actualizados = 0
    
    for producto_nuevo in productos_nuevos:
        encontrado = False
        
        for producto_actual in inventario_actual:
            if producto_actual["nombre"] == producto_nuevo["nombre"]:
                # Producto existe: sumar cantidad y actualizar precio
                producto_actual["cantidad"] += producto_nuevo["cantidad"]
                producto_actual["precio"] = producto_nuevo["precio"]
                productos_actualizados += 1
                encontrado = True
                break
        
        if not encontrado:
            # Producto nuevo: agregarlo
            inventario_actual.append(producto_nuevo)
            productos_agregados += 1
    
    return productos_agregados, productos_actualizados


"""En archivos.py, implementa:
cargar_csv(ruta) → retorna lista de productos con la misma estructura de inventario.
Reglas de validación:
El archivo debe tener encabezado válido: nombre,precio,cantidad.
Cada fila debe tener exactamente 3 columnas.
precio debe convertirse a float y cantidad a int, no negativos.
Si hay filas inválidas, omítelas y acumula un contador de errores para informar al final (p. ej. “3 filas inválidas omitidas”).
Manejar FileNotFoundError, UnicodeDecodeError, ValueError y errores genéricos con mensajes claros.
Al cargar, preguntar al usuario:
“¿Sobrescribir inventario actual? (S/N)”
Si S: reemplaza inventario por lo cargado.
Si N: fusiona por nombre:
Si un nombre ya existe, actualiza precio/cantidad u omite (define una política y muéstrala al usuario; por defecto, actualiza cantidad sumando y si el precio difiere, actualiza al nuevo).
Al finalizar, refresca la salida/menú y muestra un resumen: productos cargados, filas inválidas, acción (reemplazo/fusión)."""

