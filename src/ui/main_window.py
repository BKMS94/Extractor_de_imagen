"""
Interfaz gráfica principal de la aplicación
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from src.models.archivo import Archivo
from src.services.pdf_extractor import PDFExtractor
from config.settings import UI_CONFIG


class MainWindow(tk.Tk):
    """Ventana principal de la aplicación"""

    def __init__(self):
        super().__init__()
        self.extractor = PDFExtractor()
        self._configure_window()
        self._configure_grid()
        self._build_ui()

    def _configure_window(self):
        """Configura los parámetros de la ventana"""
        config = UI_CONFIG
        self.geometry(f"{config['window_width']}x{config['window_height']}")
        self.resizable(False, False)
        self.title(config["app_title"])
        self.configure(background=config["bg_color"])

        # Configurar estilos
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self._apply_custom_styles()

    def _apply_custom_styles(self):
        """Aplica estilos personalizados a los componentes"""
        config = UI_CONFIG
        self.style.configure(
            "TButton", background=config["accent_color"], foreground=config["fg_color"]
        )
        self.style.map(
            "TButton",
            background=[("active", config["fg_color"])],
            foreground=[("active", config["bg_color"])],
        )
        self.style.configure(
            "TLabel", background=config["bg_color"], foreground=config["fg_color"]
        )

    def _configure_grid(self):
        """Configura la distribución del grid"""
        self.grid_columnconfigure(0, weight=1)

    def _build_ui(self):
        """Construye la interfaz gráfica"""
        self._build_title()
        self._build_form()

    def _build_title(self):
        """Construye el título de la aplicación"""
        title = ttk.Label(self, text="PDF IMAGE EXTRACTOR", font=("Arial", 18, "bold"))
        title.grid(column=0, row=0, pady=20)

    def _build_form(self):
        """Construye el formulario principal"""
        # Label de instrucción
        instruction_label = ttk.Label(self, text="Select PDF file to extract images:")
        instruction_label.grid(column=0, row=1, pady=10)

        # Campo de entrada de ruta
        self.path_entry = ttk.Entry(self, width=60)
        self.path_entry.grid(column=0, row=2, pady=5)

        # Botón de búsqueda
        search_button = ttk.Button(self, text="Browse", command=self._on_browse)
        search_button.grid(column=0, row=3, pady=5)

        # Botón de procesamiento
        process_button = ttk.Button(
            self, text="Extract Images", command=self._on_process
        )
        process_button.grid(column=0, row=4, pady=20)

    def _on_browse(self):
        """Maneja el evento del botón Buscar"""
        file_path = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )
        if file_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, file_path)

    def _on_process(self):
        """Maneja el evento del botón Procesar"""
        pdf_path = self.path_entry.get()

        if not pdf_path:
            messagebox.showerror("Error", "Please select a PDF file")
            return

        try:
            archivo = Archivo(pdf_path)
            image_count = self.extractor.extract(archivo)
            messagebox.showinfo(
                "Success",
                f"Extracted {image_count} images successfully!\n"
                f"Saved to: {self.extractor.get_output_dir()}",
            )
            self._clear_path()
        except FileNotFoundError as e:
            messagebox.showerror("File Error", str(e))
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract images:\n{str(e)}")
            self._clear_path()

    def _clear_path(self):
        """Limpia el campo de entrada de ruta"""
        self.path_entry.delete(0, tk.END)


def main():
    """Punto de entrada para la interfaz gráfica"""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
