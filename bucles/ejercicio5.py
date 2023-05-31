capital = float(input("Dame capital a invertir:"))
interes = int(input("Dame interes:"))
anios = int(input("Dame anios:"))
for i in range(anios):
    capital *= (1+interes/100)
    print("Año "+str(i)+":"+str(round(capital, 2)))

