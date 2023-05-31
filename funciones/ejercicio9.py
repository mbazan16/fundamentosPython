def mcd(numero1, numero2):
    rest = 0
    while (numero2 > 0):
        rest = numero2
        numero2 = numero1 % numero2
        numero1 = rest
    return rest

    return numero
def mcm(numero1,numero2):
    if numero1 > numero2:
        grande = numero1
    else:
        grande = numero2
    while (grande % numero1 != 0) or (grande % numero2 != 0):
        grande += 1
    return grande

numero1 = int(input('Dame numero1: '))
numero2 = int(input('Dame numero2: '))
print('El máximo común divisor es :'+ str(mcd(numero1,numero2)))
print('El mínimo común múltiplo es :'+ str(mcm(numero1,numero2)))