# 1. Crea una lista llamada 'usuarios'
# 2. Dentro, agrega 3 diccionarios. Cada uno debe tener: "id", "nombre" y "rol" (admin o user).
# 3. Usa un bucle 'for' para recorrer la lista e imprimir solo el nombre de los que son "admin".

usuarios = [
    {"id": 1, "nombre": "Jose", "rol": "admin"},
    {"id": 2, "nombre": "Juan", "rol": "user"},
    {"id": 3, "nombre": "Rick", "rol": "admin"}    
    # ... agrega dos más aquí
]

# Tu lógica para imprimir solo admins aquí:

for admin in usuarios:
    if admin["rol"] == "admin":
        print(f"admin encontrado: {admin['nombre']}")
    
