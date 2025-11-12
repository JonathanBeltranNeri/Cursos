fuerza_sensor = 8.2

if fuerza_sensor == 0:
    print('Estado: Pinza abierta, sin objecto')
elif fuerza_sensor < 5 :
    print('Estado: Objecto ligero detectato . Sujetando ')
elif fuerza_sensor <= 10:
    print('Estado: Objecto firme detectado. Sujecion estable')
else:
    print("¡PELIGRO! Fuerza excesiva. Soltando objeto.")
    