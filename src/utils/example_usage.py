"""
Ejemplo de uso del extracto de PDFs de forma programática
"""

from src.models.archivo import Archivo
from src.services.pdf_extractor import PDFExtractor
from config.settings import OUTPUT_DIR


def extract_pdf_example(pdf_path: str) -> None:
    """
    Ejemplo de extracción de imágenes de un PDF

    Args:
        pdf_path (str): Ruta del archivo PDF
    """
    try:
        # Crear instancia del extractor
        extractor = PDFExtractor()

        # Crear objeto archivo
        archivo = Archivo(pdf_path)

        # Verificar que la ruta sea válida
        if not archivo.is_valid():
            print("❌ Ruta de PDF inválida")
            return

        print(f"📄 Procesando: {pdf_path}")

        # Extraer imágenes
        image_count = extractor.extract(archivo, format="JPEG")

        print(f"✅ Extracción completada")
        print(f"📸 Imágenes extraídas: {image_count}")
        print(f"📁 Guardadas en: {extractor.get_output_dir()}")

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    # Ejemplo: cambiar por tu ruta de PDF
    # pdf_path = "C:/ruta/a/tu/archivo.pdf"
    # extract_pdf_example(pdf_path)
    print("Este módulo contiene ejemplos de uso del PDFExtractor")
    print("Descomenta la llamada a extract_pdf_example() y proporciona una ruta válida")
