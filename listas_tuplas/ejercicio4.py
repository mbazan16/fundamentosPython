numerosLoteria = []

for i in range(1, 7):
    numerosLoteria.append(int(input("Número "+str(i)+" loteria:")))

numerosLoteria.sort();

print("Los números de la lotería elegidos son:")
print(str(numerosLoteria))
