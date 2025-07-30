import os
os.system("cls")

cuota = float(input("Ingrese el monto de la cuota: "))
dia = int(input("Ingrese el día de pago (1 al 31): "))


if dia < 1 or dia > 31:
    print("Día inválido")
else:
    if dia <= 10:
        descuento = max(5, cuota * 0.02)
        total_pagar = cuota - descuento
        print("Descuento aplicado: $", descuento)
    elif dia <= 20:
        descuento = 0
        total_pagar = cuota
        print("No hay descuento ni recargo.")
    else:
        recargo = max(10, cuota * 0.03)
        total_pagar = cuota + recargo
        print("Recargo aplicado: $", recargo)

    print("Total a pagar: $",total_pagar)