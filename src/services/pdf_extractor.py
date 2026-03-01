"""
Servicio de extracción de imágenes de PDF
Contiene la lógica principal para procesar PDFs
"""

import os
import shutil
from pathlib import Path
from pdf2image import convert_from_path
from config.settings import OUTPUT_DIR, POPPLER_PATH
from src.models.archivo import Archivo


class PDFExtractor:
    """Servicio encargado de extraer imágenes de archivos PDF"""

    def __init__(self, output_dir: Path = None, poppler_path: Path = None):
        """
        Inicializa el extractor.

        Args:
            output_dir (Path): Directorio de salida para las imágenes
            poppler_path (Path): Ruta a la librería Poppler
        """
        self.output_dir = output_dir or OUTPUT_DIR
        self.poppler_path = str(poppler_path or POPPLER_PATH)
        self._ensure_output_dir()

    def _ensure_output_dir(self):
        """Asegura que el directorio de salida existe"""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def extract(self, archivo: Archivo, format: str = "JPEG") -> int:
        """
        Extrae imágenes de un archivo PDF.

        Args:
            archivo (Archivo): Objeto con la ruta del PDF
            format (str): Formato de salida (JPEG, PNG, BMP)

        Returns:
            int: Número de imágenes extraídas

        Raises:
            ValueError: Si la ruta del PDF no es válida
            FileNotFoundError: Si el archivo PDF no existe
        """
        if not archivo.is_valid():
            raise ValueError("Ruta PDF inválida")

        if not os.path.exists(archivo.pdf_path):
            raise FileNotFoundError(f"Archivo no encontrado: {archivo.pdf_path}")

        try:
            pages = convert_from_path(
                pdf_path=archivo.pdf_path, poppler_path=self.poppler_path
            )

            image_count = 0
            for page_num, page in enumerate(pages, 1):
                img_name = f"page-{page_num:04d}.{format.lower()}"
                img_path = self.output_dir / img_name
                page.save(str(img_path), format)
                image_count += 1

            return image_count

        except Exception as e:
            raise Exception(f"Error al extraer imágenes: {str(e)}")

    def get_output_dir(self) -> Path:
        """Retorna el directorio de salida"""
        return self.output_dir

    def clear_output(self):
        """Limpia el directorio de salida"""
        self._ensure_output_dir()
