import os
import sys
sys.path.insert(0, os.path.abspath('../src'))  # Ruta al código fuente

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

html_context = {
    "display_github": True,  # Mostrar enlace a GitHub
    "github_user": "tu_usuario",  # Nombre de usuario
    "github_repo": "tu_repositorio",  # Nombre del repositorio
    "github_version": "main",  # Rama principal
    "conf_py_path": "/docs/",
}

templates_path = ['_templates']
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]


# Configuración general
project = 'Documentación'
author = 'Alberto'
release = '1.0'
language = 'es'

# Tema de la documentación
html_theme = 'alabaster'
