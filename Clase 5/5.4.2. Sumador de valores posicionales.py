num = input("Ingresa un número: ")
print(f"Proceso de reducción para {num}:")
lista1 = []
for i in num:
    digito_entero = int(i)
    lista1.append(digito_entero)
suma = sum(lista1)
print(f"{num} = {suma}")

num1 = str(suma)
lista2 = []
for a in num1:
    if len(num1) >= 2:
        lista2 = [] 
        for j in num1: 
            lista2.append(int(j))
        suma1 = sum(lista2)
print(f"{num1} = {suma1}") 


num2 = str(suma1)
lista3 = []
for b in num2:
    if len(num2) >= 2:
        lista3 = [] 
        for k in num2: 
            lista3.append(int(k))
        suma2 = sum(lista3)
print(f"{num2} = {suma2}")


