import os
os.system("cls")

curso = input("Curso (matematica, fisica o quimica): ")


pc1 = float(input("Nota PC1: "))
pc2 = float(input("Nota PC2: "))
pc3 = float(input("Nota PC3: "))
ep = float(input("Examen Parcial: "))
ef = float(input("Examen Final: "))


promedio = 0

if curso == "matematica":
    promedio = pc1*0.1 + pc2*0.2 + pc3*0.1 + ep*0.3 + ef*0.3
elif curso == "fisica":
    promedio = pc1*0.2 + pc2*0.2 + pc3*0.2 + ep*0.2 + ef*0.2
elif curso == "quimica":
    promedio = pc1*0.1 + pc2*0.3 + pc3*0.1 + ep*0.25 + ef*0.25
else:
    print("Curso no válido")


if promedio > 0:
    print("Promedio final:", round(promedio, 2))
    if promedio >= 13:
        print("Aprobado")
    else:
        print("Desaprobado")