# Sistema de Facturación - Tienda Agrícola

Sistema de facturación desarrollado en Python para una tienda agrícola que maneja productos de control (fertilizantes y control de plagas) y antibióticos para animales de granja.

## Estructura del Proyecto

```
proyecto_tienda_agricola/
├── modelo/                 # Componente Modelo - Clases del dominio
│   ├── __init__.py
│   ├── cliente.py
│   ├── factura.py
│   ├── producto_control.py
│   ├── control_plagas.py
│   ├── fertilizante.py
│   └── antibiotico.py
├── crud/                   # Componente CRUD - Operaciones de persistencia
│   ├── __init__.py
│   └── crud_cliente.py
├── test/                   # Componente Test - Pruebas unitarias
│   ├── __init__.py
│   └── test_relaciones.py
├── ui/                     # Componente UI - Interfaz de usuario
│   ├── __init__.py
│   └── menu.py
├── main.py                 # Punto de entrada del sistema
└── README.md               # Este archivo
```

## Características

### Clases del Modelo

**Cliente**
- Atributos: nombre, cédula
- Relación: Un cliente puede tener múltiples facturas (1:N)

**Factura**
- Atributos: fecha, valor_total
- Relación: Pertenece a un cliente, contiene múltiples productos

**ProductoControl** (Clase Base)
- Atributos: registro_ica, nombre, frecuencia_aplicacion, valor
- Subclases:
  - **ControlPlagas**: añade periodo_carencia
  - **Fertilizante**: añade fecha_ultima_aplicacion

**Antibiotico**
- Atributos: nombre, dosis (400-600 Kg), tipo_animal, precio
- Validación: La dosis debe estar entre 400 y 600 Kg

### Funcionalidades

1. Registrar clientes
2. Crear facturas con productos
3. Buscar facturas por cédula del cliente
4. Listar todos los clientes
5. Agregar productos a facturas (Control de Plagas, Fertilizantes, Antibióticos)

## Requisitos

- Python 3.6 o superior

## Instalación

1. Extraer el archivo comprimido
2. Navegar al directorio del proyecto

## Ejecución

### Ejecutar el sistema interactivo

```bash
python main.py
```

### Ejecutar las pruebas unitarias

```bash
python -m unittest test.test_relaciones
```

O de forma más detallada:

```bash
python -m unittest test.test_relaciones -v
```

## Pruebas Unitarias

El sistema incluye pruebas exhaustivas que verifican:

- **Herencia**: ControlPlagas y Fertilizante heredan de ProductoControl
- **Relación Cliente-Factura**: Un cliente puede tener múltiples facturas
- **Relación Factura-Producto**: Una factura puede contener múltiples productos
- **Validación**: Dosis de antibióticos entre 400-600 Kg
- **Búsqueda**: Función buscar_por_cedula() retorna todas las facturas de un cliente

## Arquitectura

El proyecto sigue una arquitectura por capas con separación de responsabilidades:

- **Modelo**: Contiene las clases del dominio
- **CRUD**: Gestiona operaciones de persistencia y búsqueda
- **Test**: Contiene pruebas unitarias
- **UI**: Interfaz de usuario

## Conceptos Aplicados

- **Herencia**: ProductoControl → ControlPlagas, Fertilizante
- **Composición**: Cliente → Factura (1:N), Factura → Productos (1:N)
- **Modularidad**: Cada clase en un archivo separado
- **NameSpace**: Uso de módulos y paquetes Python
- **Validación**: Restricciones en atributos (dosis de antibióticos)

## Autor

Proyecto académico - Programación Orientada a Objetos
Universidad Tecnológica de Pereira
