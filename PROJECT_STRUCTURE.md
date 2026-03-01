"""
GUÍA DE ESTRUCTURA DEL PROYECTO
================================

Este documento explica la organización y razón de cada carpeta/archivo del proyecto.

ESTRUCTURA DEL PROYECTO
=======================

Extractor_de_imagen/
│
├── src/                          # Código fuente principal
│   ├── __init__.py
│   ├── models/                   # Modelos de datos
│   │   ├── __init__.py
│   │   └── archivo.py           # Representa un archivo PDF a procesar
│   │
│   ├── services/                 # Lógica de negocio
│   │   ├── __init__.py
│   │   └── pdf_extractor.py     # Servicio principal de extracción
│   │
│   ├── ui/                       # Interfaz gráfica
│   │   ├── __init__.py
│   │   └── main_window.py       # Ventana principal (GUI)
│   │
│   └── utils/                    # Utilidades y herramientas
│       ├── __init__.py
│       └── example_usage.py     # Ejemplos de uso programático
│
├── config/                       # Configuración centralizada
│   ├── __init__.py
│   └── settings.py              # Configuración de rutas, estilos, etc.
│
├── output/                       # Carpeta de salida (imágenes extraídas)
│ │                              # Se genera automáticamente
│
├── proyecto_extraer_img_pdf/     # Código antiguo (para referencia)
│   ├── app_extraer_imagen_pdf.py
│   ├── archivo.py
│   ├── archivoDAO.py
│   └── README.md
│
├── poppler-24.08.0/              # Librería Poppler (no commits a git)
│
├── main.py                       # PUNTO DE ENTRADA PRINCIPAL
├── tests.py                      # Pruebas básicas
├── requirements.txt              # Dependencias Python
├── README.md                     # Documentación
└── .gitignore                    # Archivos a ignorar en git


BENEFICIOS DE ESTA ESTRUCTURA
==============================

1. SEPARACIÓN DE RESPONSABILIDADES
   - models/    → Solo definen estructuras de datos
   - services/  → Contienen lógica de negocio
   - ui/        → Solo interfaz gráfica
   - config/    → Configuración centralizada

2. MANTENIBILIDAD
   - Fácil encontrar código por su función
   - Cambios en un área no afectan otras

3. ESCALABILIDAD
   - Agregar nuevas features no complica la estructura
   - Fácil agregar tests

4. REUTILIZACIÓN
   - Código backend (services) se puede usar en CLI, API, etc.
   - UI es independiente de la lógica


CÓMO USAR EL PROYECTO
======================

1. EJECUTAR LA APLICACIÓN GUI
   python main.py

2. USAR LA LÓGICA DESDE OTRO SCRIPT
   from src.services.pdf_extractor import PDFExtractor
   from src.models.archivo import Archivo
   
   extractor = PDFExtractor()
   archivo = Archivo("mi_pdf.pdf")
   images = extractor.extract(archivo)

3. EJECUTAR PRUEBAS
   python tests.py

4. PERSONALIZAR CONFIGURACIÓN
   Editar: config/settings.py


COMPARACIÓN: ANTES vs DESPUÉS
===============================

ANTES (no escalable):
├── proyecto_extraer_img_pdf/
│   ├── app_extraer_imagen_pdf.py  (UI + lógica + datos)
│   ├── archivo.py                 (Modelo simple)
│   ├── archivoDAO.py              (Todo mezclado)
│   └── README.md


DESPUÉS (profesional y escalable):
├── src/
│   ├── models/     (solo datos)
│   ├── services/   (solo lógica)
│   ├── ui/         (solo interfaz)
│   └── utils/      (helpers)
├── config/         (centralizado)
├── main.py         (punto único de entrada)


PRÓXIMAS MEJORAS SUGERIDAS
===========================

- [ ] Agregar CLI (command-line interface)
- [ ] Implementar tests unitarios con pytest
- [ ] Agregar logging a todas las clases
- [ ] Crear API REST con Flask/FastAPI
- [ ] Agregar soporte para más formatos
- [ ] Mejorar UI (PyQt, PySimpleGUI)
- [ ] Crear ejecutable con PyInstaller

"""
