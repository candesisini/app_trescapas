# business_layer.py - Capa de lógica de negocio
from data_layer import ProductoRepository

class ProductoService:
    @staticmethod
    def crear_producto(nombre, precio, cantidad):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
            
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        
        return ProductoRepository.agregar_producto(producto)
    
    @staticmethod
    def listar_productos():
        return ProductoRepository.obtener_productos()