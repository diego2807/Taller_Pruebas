def validar_longitud_password(password):
    if not isinstance (password, str):
        raise TypeError (" La contraseña debe ser de una cadena de caracteres")
    return 8 <= len(password) <= 20 