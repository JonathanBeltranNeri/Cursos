def analizar_fuerza(fuerza):
    if fuerza == 0:
        # No imprimimos, ¡retornamos!
        return "Estado: Pinza abierta, sin objeto."
    elif fuerza < 5:
        # Corregí tu typo de "detectato" a "detectado" ;)
        return "Estado: Objeto ligero detectado. Sujetando."
    elif fuerza <= 10:
        return "Estado: Objeto firme detectado. Sujeción estable."
    else:
        # ¡Aquí está la magia!
        return "¡PELIGRO! Fuerza excesiva. Soltando objeto."

# --- Programa Principal ---

# 1. Llamamos a la función con 11.
# 2. La función entra al 'else'.
# 3. La función RETORNA el texto "¡PELIGRO!..."
# 4. 'estado_actual' ATRAPA ese texto.
estado_actual = analizar_fuerza(11)

# 5. AHORA SÍ, el programa principal imprime el texto.
print(estado_actual)