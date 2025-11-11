"""Módulo que define la clase ControlPlagas."""

from modelo.producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    """Representa un producto de control de plagas."""
    
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: int, 
                 valor: float, periodo_carencia: int):
        """
        Inicializa un producto de control de plagas.
        
        Args:
            registro_ica: Registro ICA del producto
            nombre: Nombre del producto
            frecuencia_aplicacion: Frecuencia de aplicación en días
            valor: Valor del producto
            periodo_carencia: Periodo de carencia en días
        """
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self.periodo_carencia = periodo_carencia
    
    def __str__(self):
        return f"Control de Plagas: {self.nombre} - ${self.valor} (Carencia: {self.periodo_carencia} días)"
    
    def __repr__(self):
        return f"ControlPlagas(nombre='{self.nombre}', periodo_carencia={self.periodo_carencia})"
