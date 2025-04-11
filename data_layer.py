# data_layer.py - Capa de acceso a datos
productos = []

class ProductoRepository:
    @staticmethod
    def agregar_producto(producto):
        productos.append(producto)
        return producto
    
    @staticmethod
    def obtener_productos():
        return productos.copy()