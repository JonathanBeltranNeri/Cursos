def simular_sensor_peso():
    return 10.2


def simular_sensor_vision():
    return True
    
def analizar_pieza(peso ,vision_ok):
    if vision_ok == False:
        return 'Rechazada por Vision'
    elif peso < 9.5 or peso > 10.5:
        return 'Rechazada por Peso'
    else:
        return 'Aceptada'
# --- Programa Principal ---
total_aceptadas = 0
pieza_actual = 1

while pieza_actual <= 20:
    simular_sensor_peso()
    peso = simular_sensor_peso()
    vision_ok = simular_sensor_vision()
    resultado = analizar_pieza(peso, vision_ok)
    print(f'Pieza {pieza_actual}: {resultado}')
    if resultado == 'Aceptada':
        total_aceptadas += 1                    
    pieza_actual += 1   
print(f'Total de piezas aceptadas: {total_aceptadas}')

    

