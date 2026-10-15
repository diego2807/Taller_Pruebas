import pytest
from src.ejercicio_05 import es_mayor_de_edad


def test_es_mayor_de_edad_inmediatamente_inferior_frontera():
    # Arrange (Preparar)
    edad = 17

    # Act (Actuar)
    resultado = es_mayor_de_edad(edad)

    # Assert (Afirmar)
    assert resultado is False


def test_es_mayor_de_edad_frontera_exacta():
    # Arrange (Preparar)
    edad = 18

    # Act (Actuar)
    resultado = es_mayor_de_edad(edad)

    # Assert (Afirmar)
    assert resultado is True


def test_es_mayor_de_edad_inmediatamente_superior_frontera():
    # Arrange (Preparar)
    edad = 19

    # Act (Actuar)
    resultado = es_mayor_de_edad(edad)

    # Assert (Afirmar)
    assert resultado is True


def test_es_mayor_de_edad_limite_biologico_inferior_invalido_lanza_value_error():
    # Arrange (Preparar)
    edad_invalida = -1

    # Act & Assert (Actuar y Afirmar)
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad_invalida)


def test_es_mayor_de_edad_limite_biologico_superior_invalido_lanza_value_error():
    # Arrange (Preparar)
    edad_invalida = 126

    # Act & Assert (Actuar y Afirmar)
    with pytest.raises(ValueError):
        es_mayor_de_edad(edad_invalida)