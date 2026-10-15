import pytest
from src.ejercicio_07 import factorial


def test_factorial_caso_base_cero():
    # Arrange
    numero = 0
    esperado = 1

    # Act
    resultado = factorial(numero)

    # Assert
    assert resultado == esperado


def test_factorial_caso_base_uno():
    # Arrange
    numero = 1
    esperado = 1

    # Act
    resultado = factorial(numero)

    # Assert
    assert resultado == esperado


def test_factorial_caso_tipico_cinco():
    # Arrange
    numero = 5
    esperado = 120

    # Act
    resultado = factorial(numero)

    # Assert
    assert resultado == esperado


def test_factorial_numero_mayor_siete():
    # Arrange
    numero = 7
    esperado = 5040

    # Act
    resultado = factorial(numero)

    # Assert
    assert resultado == esperado


def test_factorial_numero_negativo_lanza_value_error():
    # Arrange
    numero_invalido = -3
    mensaje_esperado = "El factorial no está definido para números negativos"

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        factorial(numero_invalido)
    assert str(exc_info.value) == mensaje_esperado


def test_factorial_tipo_invalido_lanza_type_error():
    # Arrange
    entrada_invalida = 4.5
    mensaje_esperado = "El argumento debe ser un número entero"

    # Act & Assert
    with pytest.raises(TypeError) as exc_info:
        factorial(entrada_invalida)
    assert str(exc_info.value) == mensaje_esperado