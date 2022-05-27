# En este segundo ejercicios tendréis que crear un script que nos diga si es
# la hora de ir a casa. Tendréis que hacer uso del modulo time.
# Necesitaréis la fecha del sistema y poder comprobar la hora.

# En el caso de que sean más de las 7, se mostrará un mensaje y en caso
# contrario, haréis una operación para calcular el tiempo que queda de trabajo.

from datetime import datetime



ahora = datetime.now()
salida = datetime(ahora.year, ahora.month, ahora.day, hour=23, minute=00)



if ahora >= salida:
    print("Es hora de irse a casa")
else:
    horas_salida = int((salida - ahora).total_seconds() // 3600)
    minutos_salida = int(((salida - ahora).total_seconds() % 3600) // 60)
    print("Quedan {} hora {} minutos de trabajo".
            format(horas_salida, minutos_salida))
