import pytest
from src.ejercicio_12 import procesar_usuario


def test_usuario_valido():
    # Arrange
    usuario = {"id": 1, "nombre": "Alejandro", "activo": True}
    esperado = {
        "id": 1,
        "nombre": "Alejandro",
        "activo": True,
        "estado_registro": "VALIDADO",
    }

    # Act
    resultado = procesar_usuario(usuario)

    # Assert
    assert resultado == esperado


@pytest.mark.parametrize(
    "usuario_invalido",
    [
        {"id": 1, "nombre": "Alejandro"},                 # 2. Clave "activo" faltante
        {"id": 0, "nombre": "Alejandro", "activo": True},  # 3. Límite inválido id = 0
        {"id": -1, "nombre": "Alejandro", "activo": True}, # 3. Límite inválido id negativo
        {"id": 1, "nombre": "   ", "activo": True},        # 4. Nombre solo con espacios
    ]
)
def test_usuario_errores_valor(usuario_invalido):
    # Arrange
    datos = usuario_invalido

    # Act & Assert
    with pytest.raises(ValueError):
        procesar_usuario(datos)


def test_usuario_tipo_invalido():
    # Arrange: Paso de una lista en vez de dict
    entrada_invalida = ["id", "nombre", "activo"]

    # Act & Assert
    with pytest.raises(TypeError):
        procesar_usuario(entrada_invalida)