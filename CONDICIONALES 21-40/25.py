import os
os.system("cls") 

sueldo = float(input("Ingrese el sueldo bruto: "))


hijos = int(input("Ingrese la cantidad de hijos: "))

bono_fijo = 0.125 * sueldo

if hijos > 1:
    bono_total = bono_fijo + (40 * hijos)
else:
    bono_total = bono_fijo


sueldo_neto = sueldo + bono_total

print("Bonificación total: S/", bono_total)
print("Sueldo neto a pagar: S/", sueldo_neto)
