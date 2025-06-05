numeros = input("Ingrese valores para su lista: ").split(" ")
lista = []
for numero in numeros:
    if numero not in lista:
       lista.append(numero)
    else: 
        continue

str_lista = ""
for i in lista:
    str_lista += str(i) 
print(str_lista)