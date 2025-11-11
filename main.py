"""Punto de entrada principal del Sistema de Facturación - Tienda Agrícola."""

from ui import Menu

def main():
    """Función principal que inicia el sistema."""
    menu = Menu()
    menu.ejecutar()

if __name__ == "__main__":
    main()
