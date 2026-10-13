def sumar(a, b):
    # Validamos que el tipo exacto sea int o float para excluir bool (subclase de int)
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Ambos argumentos deben ser estrictamente numéricos (int o float)")
    return a + b