import pytest
from src.ejercicio_01 import sumar

def test_sumar_enteros_positivos():
    a = 2
    b = 3
    resultado_esperado = 5

    resultado = sumar(a, b)

    assert resultado == resultado_esperado

def test_sumar_positivo_y_negativo():
    a = 10
    b = -4
    resultado_esperado = 6

    resultado = sumar(a, b)

    assert resultado == resultado_esperado

def test_sumar_argumento_string_lanza_type_error():
    a = "5"
    b = 3

    with pytest.raises(TypeError):
        sumar(a, b)

def test_sumar_argumento_booleano_lanza_type_error():
    a = True
    b = 3

    with pytest.raises(TypeError):
        sumar(a, b)