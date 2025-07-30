import os
os.system("cls")
monto_total = float(input("Ingrese el monto total de la compra: "))


if monto_total > 5000:
    porcentaje_prestamo = 0.30
else:
    porcentaje_prestamo = 0.20

prestamo = monto_total * porcentaje_prestamo
interes = prestamo * 0.10
propio = monto_total - prestamo
total_con_interes = prestamo + interes


print("Monto que paga la empresa: $", propio)
print("Préstamo del banco: $", prestamo)
print("Interés del banco: $", interes)
print("Total a pagar al banco: $", total_con_interes)