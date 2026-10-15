import pytest
from src.ejercicio_06 import validar_longitud_password


def test_validar_longitud_password_longitud_7_borde_invalido_inferior():
    # Arrange (Preparar) - Cadena de 7 caracteres
    password = "a" * 7

    # Act (Actuar)
    resultado = validar_longitud_password(password)

    # Assert (Afirmar)
    assert resultado is False


def test_validar_longitud_password_longitud_8_borde_valido_inferior():
    # Arrange (Preparar) - Cadena de 8 caracteres
    password = "a" * 8

    # Act (Actuar)
    resultado = validar_longitud_password(password)

    # Assert (Afirmar)
    assert resultado is True


def test_validar_longitud_password_longitud_20_borde_valido_superior():
    # Arrange (Preparar) - Cadena de 20 caracteres
    password = "a" * 20

    # Act (Actuar)
    resultado = validar_longitud_password(password)

    # Assert (Afirmar)
    assert resultado is True


def test_validar_longitud_password_longitud_21_borde_invalido_superior():
    # Arrange (Preparar) - Cadena de 21 caracteres
    password = "a" * 21

    # Act (Actuar)
    resultado = validar_longitud_password(password)

    # Assert (Afirmar)
    assert resultado is False


def test_validar_longitud_password_tipo_invalido_lanza_type_error():
    # Arrange (Preparar) - Caso con None y con un valor numérico
    password_none = None
    password_numero = 12345678

    # Act & Assert (Actuar y Afirmar)
    with pytest.raises(TypeError):
        validar_longitud_password(password_none)

    with pytest.raises(TypeError):
        validar_longitud_password(password_numero)