INTERES = 0.04
capital = int(input('Capital:'))

capital_primer_anio = round((capital + capital*INTERES), 2)
print(capital_primer_anio)

capital_segundo_anio = round((capital_primer_anio + capital_primer_anio*INTERES), 2)
print(capital_segundo_anio)

capital_tercer_anio = round((capital_segundo_anio + capital_segundo_anio*INTERES), 2)
print(capital_tercer_anio)