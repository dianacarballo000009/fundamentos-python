contraseña = input("Ingresa contraseña: ")
mayuscula = False
digito = False

for letra in contraseña:
    if letra.isupper():
        mayuscula = True
    elif letra.isdigit():
        digito = True

if mayuscula and digito and len(contraseña) >= 8:
    print("Contraseña segura")
else:
    print("Contraseña no segura")