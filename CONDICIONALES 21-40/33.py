import os
os.system("cls")

tardanza = int(input("Minutos de tardanza: "))
observaciones = int(input("Cantidad de observaciones: "))


if tardanza == 0:
    puntaje_puntualidad = 10
elif tardanza <= 2:
    puntaje_puntualidad = 8
elif tardanza <= 5:
    puntaje_puntualidad = 6
elif tardanza <= 9:
    puntaje_puntualidad = 4
else:
    puntaje_puntualidad = 0


if observaciones == 0:
    puntaje_rendimiento = 10
elif observaciones == 1:
    puntaje_rendimiento = 8
elif observaciones == 2:
    puntaje_rendimiento = 5
elif observaciones == 3:
    puntaje_rendimiento = 1
else:
    puntaje_rendimiento = 0


puntaje_total = puntaje_puntualidad + puntaje_rendimiento


if puntaje_total < 11:
    bonificacion = puntaje_total * 2.5
elif puntaje_total <= 13:
    bonificacion = puntaje_total * 5.0
elif puntaje_total <= 16:
    bonificacion = puntaje_total * 7.5
elif puntaje_total <= 19:
    bonificacion = puntaje_total * 10.0
else:
    bonificacion = puntaje_total * 12.5


print("Puntaje total:", puntaje_total)
print("Bonificación: S/.",bonificacion)