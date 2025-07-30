import os
os.system("cls")

pamela = int(input("Votos para Pamela: "))
carol = int(input("Votos para Carol: "))
fanny = int(input("Votos para Fanny: "))


total = pamela + carol + fanny
ganador = (total // 2) + 1


if pamela >= ganador:
    print("Ganadora: Pamela")
elif carol >= ganador:
    print("Ganadora: Carol")
elif fanny >= ganador:
    print("Ganadora: Fanny")
else:

 if pamela == carol == fanny:
    print("Elección anulada: Empate triple")
 else:
  votos = [("Pamela", pamela), ("Carol", carol), ("Fanny", fanny)]

  votos.sort(key=lambda x: x[1], reverse=True)

if votos[1][1] == votos[2][1]:
    print("Elección anulada: Empate por el segundo lugar")
else:
    print("Segunda vuelta entre:", votos[0][0], "y",votos[1][0])