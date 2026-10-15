import pytest
from src.ejercicio_09 import es_palindromo


def test_es_palindromo_palabra_simple():
    # Arrange
    palabra = "radar"
    esperado = True

    # Act
    resultado = es_palindromo(palabra)

    # Assert
    assert resultado is esperado


def test_es_palindromo_frase_con_espacios_y_mayusculas():
    # Arrange
    frase = "Anita lava la tina"
    esperado = True

    # Act
    resultado = es_palindromo(frase)

    # Assert
    assert resultado is esperado


def test_es_palindromo_palabra_no_palindroma():
    # Arrange
    palabra = "software"
    esperado = False

    # Act
    resultado = es_palindromo(palabra)

    # Assert
    assert resultado is esperado


def test_es_palindromo_cadena_vacia_o_solo_espacios():
    # Arrange
    cadena_espacios = "   "
    esperado = False

    # Act
    resultado = es_palindromo(cadena_espacios)

    # Assert
    assert resultado is esperado


def test_es_palindromo_rechazo_tipo_numerico():
    # Arrange
    entrada_numerica = 1001
    mensaje_esperado = "El parámetro debe ser una cadena de texto"

    # Act & Assert
    with pytest.raises(TypeError) as exc_info:
        es_palindromo(entrada_numerica)
    assert str(exc_info.value) == mensaje_esperado