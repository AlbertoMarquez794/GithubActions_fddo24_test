import pytest
from text_utils import contar_palabras

def test_texto_vacio():
    texto = ""
    assert contar_palabras(texto) == 0, "El resultado debería ser 0 para un texto vacío."

def test_una_palabra():
    texto = "Hola"
    assert contar_palabras(texto) == 1, "El resultado debería ser 1 para un texto con una sola palabra."

def test_varias_palabras():
    texto = "Este es un ejemplo de texto con varias palabras."
    assert contar_palabras(texto) == 9, "El resultado debería ser 9 para este texto."

def test_espacios_adicionales():
    texto = "   Este texto    tiene    espacios extras   "
    assert contar_palabras(texto) == 5, "El resultado debería ser 6 para un texto con espacios adicionales."

def test_tipo_invalido():
    with pytest.raises(ValueError, match="El argumento debe ser una cadena de texto."):
        contar_palabras(12345)
