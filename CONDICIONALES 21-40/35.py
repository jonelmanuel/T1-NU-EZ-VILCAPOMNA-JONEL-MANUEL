import os
os.system("cls")

codigo = int(input("Ingrese el código del empleado (3 cifras): "))


div2 = codigo % 2 == 0
div3 = codigo % 3 == 0
div5 = codigo % 5 == 0


if div2 and div3 and div5:
    tipo = "Administrativo"
elif not div2 and div3 and div5:
    tipo = "Directivo"
elif div2 and not div3 and not div5:
    tipo = "Vendedor"
elif not div2 and not div3 and not div5:
    tipo = "Seguridad"
else:
    tipo = "Otro tipo (no cumple ninguna condición específica)"

print("Tipo de empleado:",tipo)