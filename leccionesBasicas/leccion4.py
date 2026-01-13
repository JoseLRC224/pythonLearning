# Ya sabes que hay 3 elementos, dará 3 vueltas.
for i in [1, 2, 3]:
    print(f"Vuelta número {i}")
    
# No sabemos cuándo el usuario se cansará
comando = ""
while comando != "salir":
    comando = input("Escribe algo (o 'salir' para terminar): ")
    print(f"Escribiste: {comando}")