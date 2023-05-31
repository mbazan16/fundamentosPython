
PESO_MUÑECAS = 75
PESO_PAYASOS = 112
num_muñecas = int(input('Número de muñecas:'))
num_payasos = int(input('Número de payasos:'))

peso_pedido = ((num_muñecas * PESO_MUÑECAS) + (num_payasos * PESO_PAYASOS))/1000

print(peso_pedido)