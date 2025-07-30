import os
os.system("cls")

peso = float(input("Ingrese peso en kg: "))
estatura = float(input("Ingrese estatura en metros: "))


imc = peso / (estatura ** 2)


if imc < 20:
    clasificacion = "Delgado"
elif imc <= 25:
    clasificacion = "Normal"
elif imc <= 27:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"


print("IMC:", round(imc, 2))
print("Clasificación:",clasificacion)