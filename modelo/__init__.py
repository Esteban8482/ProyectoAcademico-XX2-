"""Componente Modelo - Contiene todas las clases del dominio."""

from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.producto_control import ProductoControl
from modelo.control_plagas import ControlPlagas
from modelo.fertilizante import Fertilizante
from modelo.antibiotico import Antibiotico

__all__ = [
    'Cliente',
    'Factura',
    'ProductoControl',
    'ControlPlagas',
    'Fertilizante',
    'Antibiotico'
]
