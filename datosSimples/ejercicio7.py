peso = int(input('Peso (Kg):'))
altura = float(input('Altura (metros):'))
imc = str(round(((peso / altura) ** 2), 2))
print('Tu índice de masa corporal es ' + imc + ' donde ' + imc +
      ' es el índice de masa corporal calculado redondeado con dos decimales')
