"""Módulo CRUD para gestión de clientes y búsquedas."""

from modelo.cliente import Cliente
from modelo.factura import Factura

class CRUDCliente:
    """Gestiona operaciones CRUD sobre clientes."""
    
    def __init__(self):
        """Inicializa el repositorio de clientes."""
        self.clientes = {}
    
    def crear_cliente(self, nombre: str, cedula: str) -> Cliente:
        """
        Crea un nuevo cliente.
        
        Args:
            nombre: Nombre del cliente
            cedula: Cédula del cliente
        
        Returns:
            Cliente creado
        """
        cliente = Cliente(nombre, cedula)
        self.clientes[cedula] = cliente
        return cliente
    
    def obtener_cliente(self, cedula: str) -> Cliente:
        """
        Obtiene un cliente por su cédula.
        
        Args:
            cedula: Cédula del cliente
        
        Returns:
            Cliente encontrado o None
        """
        return self.clientes.get(cedula)
    
    def buscar_por_cedula(self, cedula: str):
        """
        Busca todas las facturas asociadas a un cliente por su cédula.
        
        Args:
            cedula: Cédula del cliente
        
        Returns:
            Tupla (cliente, facturas) o (None, None) si no existe
        """
        cliente = self.clientes.get(cedula)
        if cliente:
            return cliente, cliente.facturas
        return None, None
    
    def crear_factura(self, cedula: str, fecha: str) -> Factura:
        """
        Crea una factura para un cliente.
        
        Args:
            cedula: Cédula del cliente
            fecha: Fecha de la factura
        
        Returns:
            Factura creada o None si el cliente no existe
        """
        cliente = self.clientes.get(cedula)
        if cliente:
            factura = Factura(fecha, cliente)
            cliente.agregar_factura(factura)
            return factura
        return None
    
    def listar_clientes(self):
        """Retorna la lista de todos los clientes."""
        return list(self.clientes.values())
