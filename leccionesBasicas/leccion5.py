#Este es el paso más importante antes de saltar a la Fase 2. 
#Las funciones nos permiten reutilizar código. En lugar de escribir 
#la lógica de "limpiar correos" o "validar contraseñas" mil veces, creamos 
#una función y la llamamos cuando la necesitemos.

def saludar(nombre): # 'nombre' es el parámetro (la entrada)
    return f"Hola, {nombre}!" # 'return' es lo que la función nos devuelve


while True:
    n = input("Cual es tu nombre? ")
    if n == "salir":
        break
    mensaje = saludar(n)
    print(mensaje)
    
    
    


