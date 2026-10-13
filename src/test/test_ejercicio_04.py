import pytest
from src.ejercicio_04 import aplicar_descuento


def test_aplicar_descuento_caso_general():
    precio = 100000
    descuento = 20
    esperado = 80000.0

    resultado = aplicar_descuento(precio, descuento)
    assert resultado == esperado


def test_aplicar_descuento_limite_inferior():
    precio = 50000
    descuento = 0
    esperado = 50000.0

    resultado = aplicar_descuento(precio, descuento)
    assert resultado == esperado


def test_aplicar_descuento_limite_superior():
    precio = 75000
    descuento = 100
    esperado = 0.0

    resultado = aplicar_descuento(precio, descuento)
    assert resultado == esperado


def test_aplicar_descuento_porcentaje_menor_a_cero_lanza_value_error():
    precio = 50000
    descuento_invalido = -1
    with pytest.raises(ValueError):
        aplicar_descuento(precio, descuento_invalido)


def test_aplicar_descuento_porcentaje_mayor_a_cien_lanza_value_error():
    precio = 50000
    descuento_invalido = 101
    with pytest.raises(ValueError):
        aplicar_descuento(precio, descuento_invalido)