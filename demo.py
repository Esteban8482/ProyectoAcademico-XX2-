"""Script de demostración del sistema de facturación."""

from modelo import Cliente, ControlPlagas, Fertilizante, Antibiotico
from crud import CRUDCliente

def main():
    """Ejecuta una demostración completa del sistema."""
    print("="*60)
    print("DEMOSTRACIÓN - SISTEMA DE FACTURACIÓN TIENDA AGRÍCOLA")
    print("="*60)
    
    # Inicializar CRUD
    crud = CRUDCliente()
    
    # 1. Crear clientes
    print("\n1. CREANDO CLIENTES...")
    cliente1 = crud.crear_cliente("Juan Pérez", "123456789")
    cliente2 = crud.crear_cliente("María López", "987654321")
    print(f"   ✓ {cliente1}")
    print(f"   ✓ {cliente2}")
    
    # 2. Crear productos
    print("\n2. CREANDO PRODUCTOS...")
    control1 = ControlPlagas("ICA001", "Insecticida X", 15, 50000, 7)
    control2 = ControlPlagas("ICA002", "Fungicida Y", 20, 60000, 10)
    fertilizante1 = Fertilizante("ICA003", "Abono Z", 30, 80000, "2023-04-01")
    fertilizante2 = Fertilizante("ICA004", "Fertilizante W", 25, 70000, "2023-04-15")
    antibiotico1 = Antibiotico("Penicilina", 500, "Bovinos", 120000)
    antibiotico2 = Antibiotico("Amoxicilina", 450, "Porcinos", 90000)
    
    print(f"   ✓ {control1}")
    print(f"   ✓ {control2}")
    print(f"   ✓ {fertilizante1}")
    print(f"   ✓ {fertilizante2}")
    print(f"   ✓ {antibiotico1}")
    print(f"   ✓ {antibiotico2}")
    
    # 3. Crear facturas para cliente1
    print(f"\n3. CREANDO FACTURAS PARA {cliente1.nombre}...")
    factura1 = crud.crear_factura("123456789", "2023-05-01")
    factura1.agregar_producto(control1)
    factura1.agregar_producto(fertilizante1)
    factura1.agregar_producto(antibiotico1)
    print(f"   ✓ {factura1}")
    print(f"     Productos: {len(factura1.productos)}")
    
    factura2 = crud.crear_factura("123456789", "2023-05-15")
    factura2.agregar_producto(control2)
    factura2.agregar_producto(antibiotico2)
    print(f"   ✓ {factura2}")
    print(f"     Productos: {len(factura2.productos)}")
    
    # 4. Crear factura para cliente2
    print(f"\n4. CREANDO FACTURA PARA {cliente2.nombre}...")
    factura3 = crud.crear_factura("987654321", "2023-05-10")
    factura3.agregar_producto(fertilizante2)
    factura3.agregar_producto(antibiotico1)
    print(f"   ✓ {factura3}")
    print(f"     Productos: {len(factura3.productos)}")
    
    # 5. Buscar facturas por cédula
    print("\n5. BUSCANDO FACTURAS POR CÉDULA...")
    print(f"\n   Búsqueda: Cédula {cliente1.cedula}")
    cliente_encontrado, facturas = crud.buscar_por_cedula("123456789")
    print(f"   ✓ Cliente: {cliente_encontrado.nombre}")
    print(f"   ✓ Total de facturas: {len(facturas)}")
    
    for i, factura in enumerate(facturas, 1):
        print(f"\n   Factura #{i}:")
        print(f"     Fecha: {factura.fecha}")
        print(f"     Valor Total: ${factura.valor_total:,.2f}")
        print(f"     Productos vendidos:")
        for j, producto in enumerate(factura.productos, 1):
            print(f"       {j}. {producto}")
    
    # 6. Verificar herencia
    print("\n6. VERIFICANDO HERENCIA...")
    from modelo import ProductoControl
    print(f"   ControlPlagas es ProductoControl: {isinstance(control1, ProductoControl)}")
    print(f"   Fertilizante es ProductoControl: {isinstance(fertilizante1, ProductoControl)}")
    
    # 7. Verificar composición
    print("\n7. VERIFICANDO COMPOSICIÓN...")
    print(f"   Cliente '{cliente1.nombre}' tiene {len(cliente1.facturas)} facturas")
    print(f"   Factura 1 contiene {len(factura1.productos)} productos")
    print(f"   Factura 2 contiene {len(factura2.productos)} productos")
    
    print("\n" + "="*60)
    print("DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
    print("="*60)

if __name__ == "__main__":
    main()
