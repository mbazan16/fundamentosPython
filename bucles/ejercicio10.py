numero = int(input("Dame numero entero positivo:"))
i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print(str(numero) + " es primo")
else:
    print(str(numero) + " no es primo")
