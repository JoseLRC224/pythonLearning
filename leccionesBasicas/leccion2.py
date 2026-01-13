# Pedimos datos al usuario
nombre_cliente = input("¿Cuál es tu nombre? ")
total_cuenta = input("¿Cuánto fue el total de la cuenta? ")

# Convertimos la cuenta de texto a número decimal (float)
total_float = float(total_cuenta)

# Calculamos una propina del 15%
propina = total_float * 0.15
total_con_propina = total_float + propina

# El Booleano: ¿Es una cuenta grande? (Más de 500)
es_cuenta_grande = total_con_propina > 500

print(f"\n--- Resumen para {nombre_cliente} ---")
print(f"Propina (15%): ${propina}")
print(f"Total a pagar: ${total_con_propina}")
print(f"¿Es cuenta premium?: {es_cuenta_grande}")