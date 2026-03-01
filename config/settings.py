"""
Configuración centralizada de la aplicación
"""

from pathlib import Path

# Directorio raíz del proyecto
BASE_DIR = Path(__file__).parent.parent

# Rutas de salida
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Configuración de Poppler (para PDF a imagen)
# Ajusta esta ruta según tu instalación
POPPLER_PATH = BASE_DIR / "poppler-24.08.0" / "Library" / "bin"

# Configuración de UI
UI_CONFIG = {
    "window_width": 500,
    "window_height": 300,
    "bg_color": "#221831",
    "fg_color": "#d3d7e7",
    "accent_color": "#465779",
    "app_title": "PDF Image Extractor",
}

# Formatos de imagen soportados
SUPPORTED_FORMATS = ["JPEG", "PNG", "BMP"]

# Configuración de logs (opcional para futuro)
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
