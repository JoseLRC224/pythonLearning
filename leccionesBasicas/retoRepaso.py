correos_sucios = ["  USER1@gmail.com", "Admin@Backend.com  ", "  dev_python@Proyect.org"]

# Escribe aquí tu list comprehension
correos_limpios = [i.lower().strip() for i in correos_sucios]

print(correos_limpios)
# Resultado esperado: ['user1@gmail.com', 'admin@backend.com', 'dev_python@proyect.org']