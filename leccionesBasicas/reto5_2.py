def limpiar_texto(original):
    limpio = original.strip().lower()
    return limpio





while True:
    texto_sucio = input("Ingrese texto sucio -->")
    if texto_sucio == "salir":
        break
    print(limpiar_texto(texto_sucio))
    
    