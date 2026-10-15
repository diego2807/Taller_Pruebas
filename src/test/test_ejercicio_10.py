import pytest
from src.ejercicio_10 import clasificar_nota


def test_clasificar_nota_limite_superior_maximo():
    # Arrange
    nota = 5.0
    esperado = "Excelente"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_borde_inferior_excelente():
    # Arrange
    nota = 4.5
    esperado = "Excelente"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_borde_superior_bueno():
    # Arrange
    nota = 4.4
    esperado = "Bueno"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_borde_inferior_aceptable():
    # Arrange
    nota = 3.0
    esperado = "Aceptable"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_borde_inmediatamente_reprobatorio():
    # Arrange
    nota = 2.9
    esperado = "Deficiente"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_limite_inferior_absoluto():
    # Arrange
    nota = 0.0
    esperado = "Deficiente"

    # Act
    resultado = clasificar_nota(nota)

    # Assert
    assert resultado == esperado


def test_clasificar_nota_fuera_de_escala_inferior_lanza_value_error():
    # Arrange
    nota_invalida = -0.1
    mensaje_esperado = "Nota fuera de la escala [0.0 - 5.0]"

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        clasificar_nota(nota_invalida)
    assert str(exc_info.value) == mensaje_esperado


def test_clasificar_nota_fuera_de_escala_superior_lanza_value_error():
    # Arrange
    nota_invalida = 5.1
    mensaje_esperado = "Nota fuera de la escala [0.0 - 5.0]"

    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        clasificar_nota(nota_invalida)
    assert str(exc_info.value) == mensaje_esperado