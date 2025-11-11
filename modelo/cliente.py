"""Módulo que define la clase Cliente."""

class Cliente:
    """Representa un cliente de la tienda agrícola."""
    
    def __init__(self, nombre: str, cedula: str):
        """
        Inicializa un cliente.
        
        Args:
            nombre: Nombre del cliente
            cedula: Cédula del cliente
        """
        self.nombre = nombre
        self.cedula = cedula
        self.facturas = []
    
    def agregar_factura(self, factura):
        """Agrega una factura al historial del cliente."""
        self.facturas.append(factura)
    
    def __str__(self):
        return f"Cliente: {self.nombre} (CC: {self.cedula})"
    
    def __repr__(self):
        return f"Cliente(nombre='{self.nombre}', cedula='{self.cedula}')"
