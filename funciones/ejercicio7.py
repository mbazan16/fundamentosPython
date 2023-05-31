
def fcuadrados(lista):
    cuadrados=[]
    for numero in lista:
        cuadrados.append(numero**2)
    return cuadrados

def fcuadrados_parametros(*lista):
    cuadrados = []
    for numero in lista:
        cuadrados.append(numero ** 2)
    return cuadrados
lista = [1,2,3]

print('La lista de los cuadros  de los numeros de ', str(lista), ' es ', fcuadrados(lista))

print('Los cuadrados de los numeros 1,2,3  es ', fcuadrados_parametros(1,2,3))