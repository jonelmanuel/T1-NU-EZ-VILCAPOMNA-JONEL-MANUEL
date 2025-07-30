import os
os.system("cls")

precio_a = 25
descuento_a = 0.15

precio_b = 30
descuento_b = 0.10 


unidades_a = int(input("Ingrese la cantidad de unidades del producto A: "))
unidades_b = int(input("Ingrese la cantidad de unidades del producto B: "))


importe_bruto_a = unidades_a * precio_a
importe_bruto_b = unidades_b * precio_b


descuento_a_total = 0
if unidades_a > 50:
    descuento_a_total = importe_bruto_a * descuento_a

descuento_b_total = 0
if unidades_b > 60:
    descuento_b_total = importe_bruto_b * descuento_b


importe_bruto_total = importe_bruto_a + importe_bruto_b
descuento_total = descuento_a_total + descuento_b_total
total_a_pagar = importe_bruto_total - descuento_total


print(f"Importe bruto del producto A: S/ {importe_bruto_a:.2f}")
print(f"Importe bruto del producto B: S/ {importe_bruto_b:.2f}")
print(f"Descuento total por producto A: S/ {descuento_a_total:.2f}")
print(f"Descuento total por producto B: S/ {descuento_b_total:.2f}")
print(f"Total a pagar: S/ {total_a_pagar:.2f}")
