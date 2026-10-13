import pytest
from src.ejercicio_03 import celsius_a_fahrenheit


def test_celsius_a_fahrenheit_punto_congelacion():
    celsius = 0
    esperado = 32.0
    resultado = celsius_a_fahrenheit(celsius)

    assert resultado == esperado


def test_celsius_a_fahrenheit_punto_ebullicion():
    celsius = 100
    esperado = 212.0
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == esperado


def test_celsius_a_fahrenheit_coincidencia_escalas():
    celsius = -40
    esperado = -40.0
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == esperado


def test_celsius_a_fahrenheit_precision_decimal():
    celsius = 37
    esperado = 98.6
    resultado = celsius_a_fahrenheit(celsius)
    assert resultado == pytest.approx(esperado)


def test_celsius_a_fahrenheit_por_debajo_cero_absoluto_lanza_value_error():
    celsius_invalido = -273.16
    with pytest.raises(ValueError):
        celsius_a_fahrenheit(celsius_invalido)