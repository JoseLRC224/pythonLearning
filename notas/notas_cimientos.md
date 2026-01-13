# Repaso: Fase 1 - Cimientos (De Cero a Backend)

## 1. Transformación de Strings
Fundamental para la limpieza de datos que recibimos de usuarios o bases de datos.
```python
texto = "  HOLA mundo  "
# .strip() quita espacios, .lower() pasa a minúsculas
limpio = texto.strip().lower() 
print(limpio) # Resultado: "hola mundo"
```

## 2. Slicing (Rebanado)
Extraer partes específicas de listas o cadenas.
```python
cadena = "Python"
# [inicio:fin]
print(cadena[:2]) # "Py"
print(cadena[-3:]) # "hon" (los últimos tres)
```

## 3. Diccionarios (JSON en Python)
Es la estructura base para enviar y recibir datos en una API.
```python
usuario = {
    "nombre": "Alex",
    "stack": "Python/FastAPI",
    "os": "Fedora"
}

# Uso de .get() para evitar errores si la clave no existe
print(usuario.get("nombre", "No encontrado"))
```

## 4. List Comprehensions
La forma elegante y eficiente de crear listas en Python.
```python
# [expresion for elemento in lista if condicion]
numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]
# Resultado: [2, 4, 6]
```

---

## 🛠️ Reto de Repaso
**Contexto:** Tienes una lista de correos que vienen de un formulario con errores de formato (espacios extra y mayúsculas mezcladas).

**Datos:**
```python
correos_sucios = ["  USER1@gmail.com", "Admin@Backend.com  ", "  dev_python@Proyect.org"]
```

**Tu misión:**
Crea una nueva lista llamada `correos_limpios` utilizando **List Comprehension** que:
1. Elimine los espacios en blanco.
2. Convierta todo a minúsculas.

**Espacio para tu solución:**
```python
# Escribe aquí tu list comprehension
correos_limpios = [### TU CÓDIGO AQUÍ ###]

print(correos_limpios)
```
