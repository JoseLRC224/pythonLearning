try:
    edad = int(input("¿Cuántos años tienes?: "))
    print(f"En 10 años tendrás {edad + 10}")
except ValueError:
    # Este bloque SOLO se activa si el usuario no mete un número
    print("Error: Por favor, introduce números, no letras.")
