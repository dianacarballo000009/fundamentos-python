unidad = input("¿Cuántas unidades consumió?: ")
unidades = int(unidad)
total_de_impuesto = 0

if unidades < 100:
    print("No paga impuestos")
elif 101 <= unidades <= 200:
    total_de_impuesto = unidades * 0.5
elif unidades >= 201:
    total_de_impuesto = unidades * 0.7

print(f"El total de impuestos a pagar es {total_de_impuesto}" )