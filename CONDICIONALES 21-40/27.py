import os
os.system("cls")

venta = float(input("Ingrese el monto vendido: "))


sueldo_basico = 600
comision = venta * 0.15
sueldo_bruto = sueldo_basico + comision

if sueldo_bruto > 1800:
    descuento = sueldo_bruto * 0.10
else:
    descuento = sueldo_bruto * 0.05

sueldo_neto = sueldo_bruto - descuento


if venta > 1000:
    polos = 3
else:
    polos = 1

print("Sueldo bruto: S/.", sueldo_bruto)
print("Descuento: S/.", descuento)
print("Sueldo neto: S/.", sueldo_neto)
print("Polos obsequiados:",polos)