import os
os.system("cls")

hora = int(input("Ingrese la hora (formato 24h): "))


if hora < 0 or hora > 23:
    print("Error: Hora inválida")
else:
    if hora == 0:
        print("12 AM")
    elif hora < 12:
        print(hora, "AM")
    elif hora == 12:
        print("12 PM")
    else:
        print(hora - 12, "PM")