presentation_layer.py# presentation_layer.py - Capa de presentación
from capa_negocio import ProductoService

def mostrar_menu():
    print("\n--- Sistema de Gestión de Productos (3 Capas) ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Salir")

def agregar_producto_interfaz():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))
    
    try:
        ProductoService.crear_producto(nombre, precio, cantidad)
        print(f"Producto '{nombre}' agregado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")

def listar_productos_interfaz():
    productos = ProductoService.listar_productos()
    
    if not productos:
        print("No hay productos registrados.")
        return
    
    print("\nLista de productos:")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto_interfaz()
        elif opcion == "2":
            listar_productos_interfaz()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
