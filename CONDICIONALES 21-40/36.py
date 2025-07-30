import os
os.system("cls")

cuadernos = int(input("Ingrese número de cuadernos comprados: "))


lucas = 0
faber = 0
pilot = 0


if cuadernos < 12:
    print("No hay obsequio.")
elif cuadernos < 24:
    lucas = cuadernos // 4
elif cuadernos < 36:
    faber = (cuadernos // 4) * 2
else:
    pilot = (cuadernos // 4) * 2
    faber = cuadernos // 6
    lucas = cuadernos // 12


if cuadernos >= 12:
    print("Lapiceros obsequiados:")
    if lucas > 0:
        print("Lucas:", lucas)
    if faber > 0:
        print("Faber:", faber)
    if pilot > 0:
        print("Pilot:",pilot)