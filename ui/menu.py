"""Módulo de interfaz de usuario - Menú principal."""

from modelo import ControlPlagas, Fertilizante, Antibiotico
from crud import CRUDCliente

class Menu:
    """Interfaz de usuario para el sistema de facturación."""
    
    def __init__(self):
        """Inicializa el menú con el CRUD de clientes."""
        self.crud = CRUDCliente()
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal."""
        print("\n" + "="*50)
        print("SISTEMA DE FACTURACIÓN - TIENDA AGRÍCOLA")
        print("="*50)
        print("1. Registrar cliente")
        print("2. Crear factura")
        print("3. Buscar facturas por cédula")
        print("4. Listar todos los clientes")
        print("5. Salir")
        print("="*50)
    
    def registrar_cliente(self):
        """Registra un nuevo cliente."""
        print("\n--- REGISTRAR CLIENTE ---")
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        
        cliente = self.crud.crear_cliente(nombre, cedula)
        print(f"\n✓ Cliente registrado: {cliente}")
    
    def crear_factura(self):
        """Crea una factura para un cliente."""
        print("\n--- CREAR FACTURA ---")
        cedula = input("Cédula del cliente: ")
        
        cliente = self.crud.obtener_cliente(cedula)
        if not cliente:
            print("✗ Cliente no encontrado")
            return
        
        fecha = input("Fecha de la factura (YYYY-MM-DD): ")
        factura = self.crud.crear_factura(cedula, fecha)
        
        print(f"\n✓ Factura creada para {cliente.nombre}")
        
        while True:
            print("\n--- AGREGAR PRODUCTOS ---")
            print("1. Control de Plagas")
            print("2. Fertilizante")
            print("3. Antibiótico")
            print("4. Finalizar factura")
            
            opcion = input("Seleccione tipo de producto: ")
            
            if opcion == "1":
                self._agregar_control_plagas(factura)
            elif opcion == "2":
                self._agregar_fertilizante(factura)
            elif opcion == "3":
                self._agregar_antibiotico(factura)
            elif opcion == "4":
                break
        
        print(f"\n✓ {factura}")
    
    def _agregar_control_plagas(self, factura):
        """Agrega un control de plagas a la factura."""
        registro_ica = input("Registro ICA: ")
        nombre = input("Nombre: ")
        frecuencia = int(input("Frecuencia de aplicación (días): "))
        valor = float(input("Valor: "))
        carencia = int(input("Periodo de carencia (días): "))
        
        producto = ControlPlagas(registro_ica, nombre, frecuencia, valor, carencia)
        factura.agregar_producto(producto)
        print(f"✓ Producto agregado: {producto}")
    
    def _agregar_fertilizante(self, factura):
        """Agrega un fertilizante a la factura."""
        registro_ica = input("Registro ICA: ")
        nombre = input("Nombre: ")
        frecuencia = int(input("Frecuencia de aplicación (días): "))
        valor = float(input("Valor: "))
        fecha_ultima = input("Fecha última aplicación (YYYY-MM-DD): ")
        
        producto = Fertilizante(registro_ica, nombre, frecuencia, valor, fecha_ultima)
        factura.agregar_producto(producto)
        print(f"✓ Producto agregado: {producto}")
    
    def _agregar_antibiotico(self, factura):
        """Agrega un antibiótico a la factura."""
        nombre = input("Nombre: ")
        dosis = int(input("Dosis (400-600 Kg): "))
        tipo_animal = input("Tipo de animal (Bovinos/Caprinos/Porcinos): ")
        precio = float(input("Precio: "))
        
        try:
            producto = Antibiotico(nombre, dosis, tipo_animal, precio)
            factura.agregar_producto(producto)
            print(f"✓ Producto agregado: {producto}")
        except ValueError as e:
            print(f"✗ Error: {e}")
    
    def buscar_facturas(self):
        """Busca y muestra todas las facturas de un cliente."""
        print("\n--- BUSCAR FACTURAS POR CÉDULA ---")
        cedula = input("Cédula: ")
        
        cliente, facturas = self.crud.buscar_por_cedula(cedula)
        
        if not cliente:
            print("✗ Cliente no encontrado")
            return
        
        print(f"\n{cliente}")
        print(f"Total de facturas: {len(facturas)}\n")
        
        for i, factura in enumerate(facturas, 1):
            print(f"\nFactura #{i}:")
            print(f"  Fecha: {factura.fecha}")
            print(f"  Valor Total: ${factura.valor_total:.2f}")
            print(f"  Productos ({len(factura.productos)}):")
            for j, producto in enumerate(factura.productos, 1):
                print(f"    {j}. {producto}")
    
    def listar_clientes(self):
        """Lista todos los clientes registrados."""
        print("\n--- LISTA DE CLIENTES ---")
        clientes = self.crud.listar_clientes()
        
        if not clientes:
            print("No hay clientes registrados")
            return
        
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente} - Facturas: {len(cliente.facturas)}")
    
    def ejecutar(self):
        """Ejecuta el menú principal."""
        while True:
            self.mostrar_menu_principal()
            opcion = input("\nSeleccione una opción: ")
            
            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.crear_factura()
            elif opcion == "3":
                self.buscar_facturas()
            elif opcion == "4":
                self.listar_clientes()
            elif opcion == "5":
                print("\n¡Hasta luego!")
                break
            else:
                print("\n✗ Opción inválida")
