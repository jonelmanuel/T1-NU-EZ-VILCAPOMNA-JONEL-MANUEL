import os
os.system("cls")

monto_vendido = float(input("Ingrese el monto total vendido: "))


sueldo_base = 0.10 * monto_vendido


exceso = max(0, monto_vendido - 5000)


veces_exceso = exceso // 500


bono_exceso = 25 * veces_exceso

sueldo_total = sueldo_base + bono_exceso


print(f"El sueldo total del vendedor es: S/ {sueldo_total:.2f}")
