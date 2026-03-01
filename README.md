# PDF Image Extractor

A professional Python application to extract images from PDF files with an intuitive graphical interface.

## Features

- 🎨 **GUI Interface** - User-friendly tkinter-based interface
- 📄 **Batch Processing** - Extract multiple images from PDFs
- 🖼️ **Multiple Formats** - Save as JPEG, PNG, or BMP
- ⚙️ **Configurable** - Centralized configuration management
- 🏗️ **Clean Architecture** - Well-organized project structure

## Project Structure

```
Extractor_de_imagen/
├── src/                          # Source code
│   ├── models/
│   │   └── archivo.py           # PDF file model
│   ├── services/
│   │   └── pdf_extractor.py     # PDF extraction logic
│   ├── ui/
│   │   └── main_window.py       # GUI application
│   └── utils/                    # Utility functions
├── config/
│   └── settings.py              # Centralized configuration
├── output/                       # Extracted images folder
├── main.py                       # Application entry point
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Installation

### Requirements
- Python 3.8+
- Poppler library (included in `poppler-24.08.0/`)

### Setup

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/BKMS94/Extractor_de_imagen.git
   cd Extractor_de_imagen
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the application

```bash
python main.py
```

### Using the GUI

1. Click **Browse** to select a PDF file
2. The file path will appear in the text field
3. Click **Extract Images** to process the PDF
4. Extracted images will be saved to the `output/` folder
5. A success message will display the number of extracted images

### Programmatic Usage

```python
from src.models.archivo import Archivo
from src.services.pdf_extractor import PDFExtractor

# Create extractor instance
extractor = PDFExtractor()

# Process PDF
archivo = Archivo("path/to/document.pdf")
image_count = extractor.extract(archivo, format="JPEG")

print(f"Extracted {image_count} images")
```

## Configuration

Edit `config/settings.py` to customize:
- Output directory
- Poppler path
- Window dimensions and colors
- Output image format

## Error Handling

The application handles:
- ✓ Invalid file paths
- ✓ Missing PDF files
- ✓ Poppler installation issues
- ✓ File permission errors

## Dependencies

- **pdf2image** - Convert PDF pages to images
- **Pillow** - Image processing
- **tkinter** - GUI (included with Python)

See `requirements.txt` for versions.

## Technologies

| Technology | Purpose |
|-----------|---------|
| Python 3 | Primary language |
| tkinter | GUI framework |
| pdf2image | PDF to image conversion |
| Poppler | PDF rendering engine |

## Architecture

The project follows a **3-layer architecture**:

```
┌─────────────────────────────────────┐
│   UI Layer (src/ui/)                │
│   - MainWindow, dialogs, events     │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│   Service Layer (src/services/)     │
│   - PDFExtractor, business logic    │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│   Model Layer (src/models/)         │
│   - Archivo, data classes           │
└─────────────────────────────────────┘
```

## Future Enhancements

- [ ] Batch processing multiple PDFs
- [ ] Progress bar during extraction
- [ ] Image format/quality options
- [ ] Folder organization by PDF name
- [ ] Command-line interface (CLI)
- [ ] Unit tests

## License

This project is open source and available under the MIT License.

## Author

**BKMS94** - [GitHub Profile](https://github.com/BKMS94)

## Support

For issues or questions:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include error messages and system information

---

**Version:** 2.0 (Restructured)  
**Last Updated:** March 2026
