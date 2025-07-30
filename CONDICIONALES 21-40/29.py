import os
os.system("cls")

horas = float(input("Ingrese horas trabajadas: "))
pago_hora = float(input("Ingrese pago por hora: "))


if horas <= 48:
    sueldo_bruto = horas * pago_hora
else:
    horas_normales = 48
    horas_extras = horas - 48
    sueldo_bruto = (horas_normales * pago_hora) + (horas_extras * pago_hora * 1.20)


if sueldo_bruto > 1500:
    descuento = sueldo_bruto * 0.11
else:
    descuento = 0


sueldo_neto = sueldo_bruto - descuento


print("Horas trabajadas:", horas)
print("Pago por hora: S/.", pago_hora)
print("Sueldo bruto: S/.", sueldo_bruto)
print("Descuento: S/.", descuento)
print("Total a pagar: S/.",sueldo_neto)