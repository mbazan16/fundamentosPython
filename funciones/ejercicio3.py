
def factorial(numero):
    resultado = 1
    for valor in range(1, numero+1):
        resultado *= valor
    return resultado
numero = 5
print('El factorial de ', numero, ' es ', factorial(numero))
