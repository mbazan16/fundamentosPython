from math import sin, cos, tan, exp, log
funciones = {'1': sin, '2': cos, '3': tan, '4': exp, '5': log}

def calcular(numero, funcion):
     return funcion(numero);

numero = int(input('Dame numero:'))
operacion = input('Operacion:\n 1- sin\n 2- cos\n 3- tan\n 4- exp\n 5-log\n Opción elegida:')

for valor in range(1,numero):
    print(valor,calcular(valor, funciones[operacion]))
