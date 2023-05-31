
capital = int(input('Capital:'))
interes = float(input('interes:'))
num_anyos = int(input('Anios:'))
capital_final = str(round(capital * (interes / 100 + 1) ** num_anyos, 2))
print(capital_final)