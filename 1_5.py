pieza_actual = 1 
pieza_totales =20 
while pieza_actual <= pieza_totales:
    
    print('Procesando pieza ',pieza_actual)
    if pieza_actual == 13:
        
        print("¡ERROR CRÍTICO! Pieza 13 defectuosa. Parando la línea.")
        
        break
    pieza_actual = pieza_actual + 1
print('Lote de producción detenido.')