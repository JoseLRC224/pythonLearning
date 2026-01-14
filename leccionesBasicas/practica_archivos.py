# 1. Creamos (o sobrescribimos) un archivo
with open("mi_archivo.txt", "w") as f:
    f.write("Esta es la línea original.\n")

# 2. Añadimos contenido sin borrar lo anterior
with open("mi_archivo.txt", "a") as f:
    f.write("Esta es una línea nueva que se añadió después.\n")

print("¡Archivo creado y actualizado!")
