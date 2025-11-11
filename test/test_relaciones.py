"""Módulo de pruebas unitarias para verificar relaciones y herencias."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelo import Cliente, Factura, ProductoControl, ControlPlagas, Fertilizante, Antibiotico
from crud import CRUDCliente

class TestHerencia(unittest.TestCase):
    """Pruebas para verificar la herencia de ProductoControl."""
    
    def test_control_plagas_hereda_producto_control(self):
        """Verifica que ControlPlagas hereda de ProductoControl."""
        control = ControlPlagas("ICA001", "Insecticida X", 15, 50000, 7)
        self.assertIsInstance(control, ProductoControl)
        self.assertIsInstance(control, ControlPlagas)
    
    def test_fertilizante_hereda_producto_control(self):
        """Verifica que Fertilizante hereda de ProductoControl."""
        fertilizante = Fertilizante("ICA002", "Abono Y", 30, 80000, "2023-04-01")
        self.assertIsInstance(fertilizante, ProductoControl)
        self.assertIsInstance(fertilizante, Fertilizante)
    
    def test_atributos_heredados(self):
        """Verifica que los atributos de la clase base están presentes."""
        control = ControlPlagas("ICA003", "Fungicida Z", 20, 60000, 10)
        self.assertEqual(control.registro_ica, "ICA003")
        self.assertEqual(control.nombre, "Fungicida Z")
        self.assertEqual(control.frecuencia_aplicacion, 20)
        self.assertEqual(control.valor, 60000)
        self.assertEqual(control.periodo_carencia, 10)

class TestRelacionClienteFactura(unittest.TestCase):
    """Pruebas para verificar la relación Cliente-Factura (1:N)."""
    
    def test_cliente_tiene_multiples_facturas(self):
        """Verifica que un cliente puede tener múltiples facturas."""
        cliente = Cliente("Juan Pérez", "123456789")
        factura1 = Factura("2023-05-01", cliente)
        factura2 = Factura("2023-05-15", cliente)
        
        cliente.agregar_factura(factura1)
        cliente.agregar_factura(factura2)
        
        self.assertEqual(len(cliente.facturas), 2)
        self.assertIn(factura1, cliente.facturas)
        self.assertIn(factura2, cliente.facturas)
    
    def test_factura_pertenece_a_cliente(self):
        """Verifica que una factura está asociada a un cliente."""
        cliente = Cliente("María López", "987654321")
        factura = Factura("2023-05-02", cliente)
        
        self.assertEqual(factura.cliente, cliente)
        self.assertEqual(factura.cliente.nombre, "María López")

class TestRelacionFacturaProducto(unittest.TestCase):
    """Pruebas para verificar la relación Factura-Producto."""
    
    def test_factura_contiene_productos(self):
        """Verifica que una factura puede contener múltiples productos."""
        cliente = Cliente("Pedro Gómez", "456789123")
        factura = Factura("2023-05-03", cliente)
        
        control = ControlPlagas("ICA004", "Herbicida A", 15, 45000, 5)
        fertilizante = Fertilizante("ICA005", "Fertilizante B", 30, 70000, "2023-04-20")
        antibiotico = Antibiotico("Penicilina", 500, "Bovinos", 120000)
        
        factura.agregar_producto(control)
        factura.agregar_producto(fertilizante)
        factura.agregar_producto(antibiotico)
        
        self.assertEqual(len(factura.productos), 3)
        self.assertIn(control, factura.productos)
        self.assertIn(fertilizante, factura.productos)
        self.assertIn(antibiotico, factura.productos)
    
    def test_calculo_valor_total_factura(self):
        """Verifica que el valor total de la factura se calcula correctamente."""
        cliente = Cliente("Ana Torres", "789123456")
        factura = Factura("2023-05-04", cliente)
        
        control = ControlPlagas("ICA006", "Insecticida C", 20, 30000, 8)
        antibiotico = Antibiotico("Amoxicilina", 450, "Porcinos", 90000)
        
        factura.agregar_producto(control)
        factura.agregar_producto(antibiotico)
        
        self.assertEqual(factura.valor_total, 120000)

class TestValidacionAntibiotico(unittest.TestCase):
    """Pruebas para validar las restricciones de Antibiotico."""
    
    def test_dosis_valida(self):
        """Verifica que se acepta una dosis válida."""
        antibiotico = Antibiotico("Tetraciclina", 500, "Caprinos", 85000)
        self.assertEqual(antibiotico.dosis, 500)
    
    def test_dosis_invalida_menor(self):
        """Verifica que se rechaza una dosis menor a 400."""
        with self.assertRaises(ValueError):
            Antibiotico("Tetraciclina", 350, "Caprinos", 85000)
    
    def test_dosis_invalida_mayor(self):
        """Verifica que se rechaza una dosis mayor a 600."""
        with self.assertRaises(ValueError):
            Antibiotico("Tetraciclina", 650, "Caprinos", 85000)

class TestCRUDBuscarPorCedula(unittest.TestCase):
    """Pruebas para la funcionalidad buscar_por_cedula."""
    
    def test_buscar_cliente_con_facturas(self):
        """Verifica que se pueden buscar todas las facturas de un cliente."""
        crud = CRUDCliente()
        cliente = crud.crear_cliente("Carlos Ruiz", "111222333")
        
        factura1 = crud.crear_factura("111222333", "2023-05-05")
        factura2 = crud.crear_factura("111222333", "2023-05-10")
        
        cliente_encontrado, facturas = crud.buscar_por_cedula("111222333")
        
        self.assertIsNotNone(cliente_encontrado)
        self.assertEqual(cliente_encontrado.nombre, "Carlos Ruiz")
        self.assertEqual(len(facturas), 2)
    
    def test_buscar_cliente_inexistente(self):
        """Verifica que retorna None para un cliente inexistente."""
        crud = CRUDCliente()
        cliente, facturas = crud.buscar_por_cedula("999999999")
        
        self.assertIsNone(cliente)
        self.assertIsNone(facturas)

if __name__ == '__main__':
    unittest.main()
