import random
for i in range(100):
    num_alea = random.randint(1, 100)
    opcion = int(input("Ingresa un número aleatorio entre 1 y 100: "))
    if num_alea > opcion:
        print("El número secreto es mayor")
    if num_alea < opcion:
        print("El número sercreto es menor")
    if num_alea == opcion:
        print(f"¡Felicidades! Has adivinado el numero secreto:{num_alea} ")
        print("Fin del juego")
        break