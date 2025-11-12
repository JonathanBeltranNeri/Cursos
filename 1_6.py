temperatura_actual = 60.0 
temperatura_objetivo = 85.0 
temperatura_maxima_peligro = 100.0 
enfriador_activo = False
ciclo = 1 

while True:
    
    print('Ciclo:',ciclo,'Temp=',temperatura_actual,'Enfriador:',enfriador_activo)
    
    if temperatura_actual >= temperatura_maxima_peligro:
        print("¡EMERGENCIA! TEMPERATURA CRÍTICA. PARANDO REACTOR.")
        break
    
    elif temperatura_actual > temperatura_objetivo:
        enfriador_activo = True
        temperatura_actual = temperatura_actual - 5 
        print("Temp alta. Activando enfriador.")
        
    elif temperatura_actual < temperatura_objetivo:
        enfriador_activo = False
        temperatura_actual = temperatura_actual + 5
        print("Temp baja. Activando calentador.")
        
    elif temperatura_actual == temperatura_objetivo:
        print("Temperatura estable en 85.0. Misión cumplida.")
        break
    
    ciclo = 1 + ciclo

        
        