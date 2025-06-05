import heapq
numeros = input("Ingrese valores para su lista: ").split(" ")
lista = []
for numero in numeros:
    if numero not in lista:
       lista.append(numero)
    else: 
        continue

cuatro_mayores = heapq.nlargest(4, lista)
print(cuatro_mayores)
