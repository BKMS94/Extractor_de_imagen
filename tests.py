"""
Tests básicos para validar la estructura del proyecto
"""

from src.models.archivo import Archivo
from config.settings import OUTPUT_DIR, POPPLER_PATH, UI_CONFIG


def test_archivo_model():
    """Test del modelo Archivo"""
    print("🧪 Probando modelo Archivo...")

    # Test 1: Crear archivo con ruta
    archivo = Archivo("C:/test/documento.pdf")
    assert archivo.is_valid(), "Archivo debería ser válido"
    print("✓ Archivo con ruta válida")

    # Test 2: Crear archivo vacío
    archivo_vacio = Archivo()
    assert not archivo_vacio.is_valid(), "Archivo vacío debería ser inválido"
    print("✓ Archivo vacío es inválido")

    # Test 3: Validar normalización de ruta
    archivo_ruta = Archivo("C:/path/to/file.pdf")
    assert "\\\\" in archivo_ruta.pdf_path, "Ruta debería estar normalizada"
    print("✓ Rutas normalizadas correctamente")


def test_config():
    """Test de configuración"""
    print("\n🧪 Probando configuración...")

    # Test 1: OUTPUT_DIR existe
    assert OUTPUT_DIR.exists(), "Directorio de salida debería existir"
    print(f"✓ OUTPUT_DIR existe: {OUTPUT_DIR}")

    # Test 2: POPPLER_PATH configurado
    assert POPPLER_PATH.exists(), "Ruta de Poppler debería existir"
    print(f"✓ POPPLER_PATH existe: {POPPLER_PATH}")

    # Test 3: UI_CONFIG tiene configuraciones necesarias
    required_keys = ["window_width", "window_height", "bg_color", "app_title"]
    for key in required_keys:
        assert key in UI_CONFIG, f"UI_CONFIG debería contener '{key}'"
    print("✓ Configuración UI completa")


def run_all_tests():
    """Ejecuta todos los tests"""
    print("=" * 50)
    print("PRUEBAS DEL PROYECTO")
    print("=" * 50)

    try:
        test_archivo_model()
        test_config()
        print("\n" + "=" * 50)
        print("✅ TODAS LAS PRUEBAS PASARON")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n❌ PRUEBA FALLIDA: {e}")
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")


if __name__ == "__main__":
    run_all_tests()
