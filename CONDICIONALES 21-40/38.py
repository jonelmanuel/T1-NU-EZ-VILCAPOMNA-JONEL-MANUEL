import os
os.system("cls")


dia = int(input("Día: "))
mes = int(input("Mes (1-12): "))
anio = int(input("Año: "))


nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
"Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):dias_por_mes[1] = 29  


nombre_mes = nombres_meses[mes - 1]
dias_del_mes = dias_por_mes[mes - 1]

dias_transcurridos = sum(dias_por_mes[:mes - 1]) + dia

print("Días del mes:", dias_del_mes)
print("Mes:", nombre_mes)
print("Días desde el 01 de enero:", dias_transcurridos)