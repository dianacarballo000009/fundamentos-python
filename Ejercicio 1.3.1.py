monto_str = input("Ingresa el monto a pagar: ")
monto = float(monto_str)
propina = monto * 0.1
total = propina + monto
print(f"Total de la cuenta:{monto}")
print(f"Propina: {propina}")
print(f"Total de la cuenta con propina:{total}")