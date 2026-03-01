"""
PDF Image Extractor - Aplicación Principal
Extrae imágenes de archivos PDF usando interfaz gráfica

Estructura del proyecto:
- src/models/        Modelos de datos
- src/services/      Lógica de negocio
- src/ui/            Interfaz gráfica
- config/            Configuración centralizada
- output/            Imágenes extraídas
"""

import sys
from pathlib import Path

# Añadir directorio raíz al path para imports
root_dir = Path(__file__).parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from src.ui.main_window import MainWindow


def main():
    """Función principal"""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
