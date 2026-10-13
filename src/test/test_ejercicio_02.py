import pytest
from src.ejercicio_02 import es_par


def test_es_par_numero_positivo_par():
    # Arrange (Preparar)
    numero = 8

    # Act (Actuar)
    resultado = es_par(numero)

    # Assert (Afirmar)
    assert resultado is True


def test_es_par_numero_positivo_impar():
    # Arrange (Preparar)
    numero = 7

    # Act (Actuar)
    resultado = es_par(numero)

    # Assert (Afirmar)
    assert resultado is False


def test_es_par_cero_es_par():
    # Arrange (Preparar)
    numero = 0

    # Act (Actuar)
    resultado = es_par(numero)

    # Assert (Afirmar)
    assert resultado is True


def test_es_par_enteros_negativos_pares_e_impares():
    # Arrange (Preparar)
    numero_par_negativo = -4
    numero_impar_negativo = -9

    # Act (Actuar)
    resultado_par = es_par(numero_par_negativo)
    resultado_impar = es_par(numero_impar_negativo)

    # Assert (Afirmar)
    assert resultado_par is True
    assert resultado_impar is False


def test_es_par_decimal_lanza_type_error():
    # Arrange (Preparar)
    numero_decimal = 4.0

    # Act & Assert (Actuar y Afirmar)
    with pytest.raises(TypeError):
        es_par(numero_decimal)