velocidad_cinta = 4.5
velocidad_maxima_segura = 5.0 
boton_parada = False
cinta_en_movimiento = velocidad_cinta > 0
sistema_seguro = velocidad_cinta <= velocidad_maxima_segura and boton_parada == False
print(sistema_seguro)