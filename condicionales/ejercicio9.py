edad = int(input("Dame edad:"))

if edad < 4:
    precio = 0
elif edad < 18:
    precio = 5
else:
    precio = 10

print("Tienes que pagar ", precio, "€", sep='')
