# 1. Definimos una lista de usuarios que ya existen (nuestra mini "Base de Datos")
usuarios_registrados = ["admin", "root", "dev_user"]

# 2. Tu misión: Completa esta función
def validar_registro(datos_usuario: dict) -> str:
    username = datos_usuario.get("username")
    edad = datos_usuario.get("edad")
    
    # REGLAS:
    # - Si el username ya está en 'usuarios_registrados', retornar: "Error: Usuario ya existe"
    # - Si la edad es menor a 18, retornar: "Error: Debes ser mayor de edad"
    # - Si todo está bien, retornar: "Registro exitoso para [username]"
    
    # Escribe tu lógica aquí:
    
    if username in usuarios_registrados:
        return "Error: Usuario ya registrado"
    if edad < 18:
        return "Error: Debes ser mayor de edad"
    else:
        return f"Registro exitoso para {username}"
    


# 3. Prueba tu función con estos datos
nuevo_usuario = {"username": "alex_backend", "edad": 22}
nuevo_usuario = {"username": "admin", "edad": 22}
nuevo_usuario = {"username": "Caiman", "edad": 12}
resultado = validar_registro(nuevo_usuario)
print(resultado)