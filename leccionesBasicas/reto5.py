def limpiar_texto(original):
    limpio = original.strip().lower()
    return limpio

texto_sucio = " PYTHON_BACKEND "
print(limpiar_texto(texto_sucio))