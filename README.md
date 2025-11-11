# Sistema de Facturación - Tienda Agrícola

Sistema de facturación desarrollado en Python para una tienda agrícola que maneja productos de control (fertilizantes y control de plagas) y antibióticos para animales de granja.

## Ejecución

```bash
python main.py
```

### Ejecutar las pruebas unitarias

```bash
python -m unittest test.test_relaciones
```

### Ejecutar demostracion

```bash
python demo.py
```

## Pruebas Unitarias

El sistema incluye pruebas que verifican:

- **Herencia**: ControlPlagas y Fertilizante heredan de ProductoControl
- **Relación Cliente-Factura**: Un cliente puede tener múltiples facturas
- **Relación Factura-Producto**: Una factura puede contener múltiples productos
- **Validación**: Dosis de antibióticos entre 400-600 Kg
- **Búsqueda**: Función buscar_por_cedula() retorna todas las facturas de un cliente

### Ejecucion Pruebas Unitarias
```bash
python -m unittest test.test_relaciones -v
```

## Arquitectura

- **Modelo**: Contiene las clases del dominio
- **CRUD**: Gestiona operaciones de persistencia y búsqueda
- **Test**: Contiene pruebas unitarias
- **UI**: Interfaz de usuario

## Autor

J. Esteban Salazar
