"""Módulo que define la clase base ProductoControl."""

class ProductoControl:
    """Clase base para productos de control (fertilizantes y control de plagas)."""
    
    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: int, valor: float):
        """
        Inicializa un producto de control.
        
        Args:
            registro_ica: Registro ICA del producto
            nombre: Nombre del producto
            frecuencia_aplicacion: Frecuencia de aplicación en días
            valor: Valor del producto
        """
        self.registro_ica = registro_ica
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor
    
    def __str__(self):
        return f"{self.nombre} (ICA: {self.registro_ica}) - ${self.valor}"
    
    def __repr__(self):
        return f"ProductoControl(registro_ica='{self.registro_ica}', nombre='{self.nombre}')"
