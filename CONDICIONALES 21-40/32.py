import os
os.system("cls")

categoria = input("Ingrese la categoría del estudiante (A, B, C, D): ")
promedio = float(input("Ingrese el promedio del ciclo anterior: "))


if categoria == "A":
    pension = 550
elif categoria == "B":
    pension = 500
elif categoria == "C":
    pension = 450
elif categoria == "D":
    pension = 400
else:
    print("Categoría inválida")
    pension = 0


if promedio < 14:
    descuento = 0
elif promedio < 16:
    descuento = pension * 0.10
elif promedio < 18:
    descuento = pension * 0.12
else:
    descuento = pension * 0.15

nueva_pension = pension - descuento


print("Pensión original: S/.", pension)
print("Descuento: S/.", descuento)
print("Nueva pensión: S/.",nueva_pension)