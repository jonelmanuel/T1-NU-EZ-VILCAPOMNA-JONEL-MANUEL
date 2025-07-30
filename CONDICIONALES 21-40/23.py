import os
os.system("cls")

nota_matematicas = float(input("Ingrese la nota de matemáticas: "))
nota_fisica = float(input("Ingrese la nota de física: "))


if nota_matematicas > 17:
    dinero_matematicas = 3 * nota_matematicas
else:
    dinero_matematicas = 1 * nota_matematicas


if nota_fisica > 15:
    dinero_fisica = 2 * nota_fisica
else:
    dinero_fisica = 0.5 * nota_fisica


promedio = (nota_matematicas + nota_fisica) / 2


regalo_reloj = promedio > 16


print(f"Dinero por matemáticas: S/ {dinero_matematicas:.2f}")
print(f"Dinero por física: S/ {dinero_fisica:.2f}")
if regalo_reloj:
    print("¡Le regaló un reloj!")
else:
    print("No le regaló un reloj.")
