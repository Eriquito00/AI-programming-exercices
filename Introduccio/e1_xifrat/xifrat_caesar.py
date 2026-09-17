dato = input("Por favor, ingresa un dato: ")
espacios = int(input("Por favor, ingresa el número de espacios a desplazar: "))

caesar = []
for caracter in dato:
    if (caracter.isspace()):
        caesar.append(caracter)
    else:
        caesar.append(chr(ord(caracter) + espacios))

print("".join(caesar))