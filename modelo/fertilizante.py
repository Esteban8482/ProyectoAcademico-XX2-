"""Módulo que define la clase Fertilizante."""

from modelo.producto_control import ProductoControl

class Fertilizante(ProductoControl):
    """Representa un fertilizante."""
    
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: int, 
                 valor: float, fecha_ultima_aplicacion: str):
        """
        Inicializa un fertilizante.
        
        Args:
            registro_ica: Registro ICA del producto
            nombre: Nombre del producto
            frecuencia_aplicacion: Frecuencia de aplicación en días
            valor: Valor del producto
            fecha_ultima_aplicacion: Fecha de última aplicación
        """
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
    
    def __str__(self):
        return f"Fertilizante: {self.nombre} - ${self.valor} (Última aplicación: {self.fecha_ultima_aplicacion})"
    
    def __repr__(self):
        return f"Fertilizante(nombre='{self.nombre}', fecha_ultima_aplicacion='{self.fecha_ultima_aplicacion}')"
