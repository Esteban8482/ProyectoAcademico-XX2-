"""Módulo que define la clase Factura."""

class Factura:
    """Representa una factura o pedido de la tienda."""
    
    def __init__(self, fecha: str, cliente):
        """
        Inicializa una factura.
        
        Args:
            fecha: Fecha de la factura
            cliente: Cliente asociado a la factura
        """
        self.fecha = fecha
        self.cliente = cliente
        self.productos = []
        self.valor_total = 0.0
    
    def agregar_producto(self, producto):
        """
        Agrega un producto a la factura y actualiza el valor total.
        
        Args:
            producto: Producto a agregar (ProductoControl o Antibiotico)
        """
        self.productos.append(producto)
        if hasattr(producto, 'valor'):
            self.valor_total += producto.valor
        elif hasattr(producto, 'precio'):
            self.valor_total += producto.precio
    
    def __str__(self):
        return f"Factura {self.fecha} - Cliente: {self.cliente.nombre} - Total: ${self.valor_total:.2f}"
    
    def __repr__(self):
        return f"Factura(fecha='{self.fecha}', cliente={self.cliente.nombre}, productos={len(self.productos)})"
