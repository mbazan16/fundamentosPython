frase = input("Dame frase:")
letra = input("Dame letra:")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("Numero de coincidencias:"+str(contador))


