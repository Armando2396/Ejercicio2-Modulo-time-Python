import time 
import datetime

hora_actual = time.strftime('%H:%M:%S')
hora_salida = time.strftime('19:00:00')

h1 = datetime.datetime.strptime(hora_actual, '%H:%M:%S')
h2 = datetime.datetime.strptime(hora_salida, '%H:%M:%S')

if h1 >= h2:
    print("Es Hora de Salir")
else:
    tiempoFaltante = h2 - h1
    print("Faltan :", tiempoFaltante, "para la salida")