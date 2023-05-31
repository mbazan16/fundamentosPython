def aDecimal(numero):

    numero = list(numero)
    numero.reverse()
    decimal = 0
    for i in range(len(numero)):
        decimal += int(numero[i]) * 2 ** i
    return decimal

def aBinario(numero):

    binario = []
    while numero > 0:
        binario.append(str(numero % 2))
        numero //= 2
    binario.reverse()
    return ''.join(binario)

numero = 22
binario = '10110'
print('El binario de ', numero, ' es :', aBinario(numero))
print('El numero  de ', binario, ' es :', aDecimal(binario))
