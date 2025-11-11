"""Módulo que define la clase Antibiotico."""

class Antibiotico:
    """Representa un antibiótico para animales de granja."""
    
    def __init__(self, nombre: str, dosis: int, tipo_animal: str, precio: float):
        """
        Inicializa un antibiótico.
        
        Args:
            nombre: Nombre del antibiótico
            dosis: Dosis en Kg (debe estar entre 400 y 600)
            tipo_animal: Tipo de animal (Bovinos, caprinos o porcinos)
            precio: Precio del antibiótico
        
        Raises:
            ValueError: Si la dosis no está entre 400 y 600 Kg
        """
        if not (400 <= dosis <= 600):
            raise ValueError("La dosis debe estar entre 400 y 600 Kg")
        
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio
    
    def __str__(self):
        return f"Antibiótico: {self.nombre} - ${self.precio} (Dosis: {self.dosis}Kg, Animal: {self.tipo_animal})"
    
    def __repr__(self):
        return f"Antibiotico(nombre='{self.nombre}', dosis={self.dosis}, tipo_animal='{self.tipo_animal}')"
