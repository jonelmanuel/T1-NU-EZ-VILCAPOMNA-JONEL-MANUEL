import os
os.system("cls")
horas = float(input("Ingrese horas trabajadas: "))
categoria = input("Ingrese categoría del trabajador (A, B, C, D): ")


if categoria == "A":
    tarifa = 21.00
elif categoria == "B":
    tarifa = 19.50
elif categoria == "C":
    tarifa = 17.00
elif categoria == "D":
    tarifa = 15.50
else:
    print("Categoría inválida")
    tarifa = 0


sueldo_bruto = horas * tarifa


if sueldo_bruto > 2500:
    descuento = sueldo_bruto * 0.20
else:
    descuento = sueldo_bruto * 0.15


sueldo_neto = sueldo_bruto - descuento


print("Sueldo bruto: S/.", sueldo_bruto)
print("Descuento: S/.", descuento)
print("Sueldo neto: S/.",sueldo_neto)