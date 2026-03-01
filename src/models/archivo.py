"""
Modelo de datos para archivo PDF
"""


class Archivo:
    """Representa un archivo PDF a procesar"""

    def __init__(self, pdf_path: str = None):
        """
        Inicializa un archivo PDF.

        Args:
            pdf_path (str): Ruta del archivo PDF
        """
        self.pdf_path = self._normalize_path(pdf_path) if pdf_path else None

    @staticmethod
    def _normalize_path(path: str) -> str:
        """Normaliza la ruta del archivo (convierte / a \\)"""
        return path.replace("/", "\\") if path else None

    def is_valid(self) -> bool:
        """Verifica si la ruta es válida"""
        return self.pdf_path is not None and len(self.pdf_path) > 0

    def __str__(self) -> str:
        return f"PDF: {self.pdf_path}"

    def __repr__(self) -> str:
        return f"Archivo(pdf_path='{self.pdf_path}')"
