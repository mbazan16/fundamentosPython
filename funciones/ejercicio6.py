
def media(lista):
    return sum(lista)/ len(lista)

def mediaConParametros(*lista):
    return sum(lista)/ len(lista)
lista = [1,2,3]
print('La media de los numeros de ', str(lista), ' es ', media(lista))

print('La media de los numeros 1,2,3  es ', mediaConParametros(1,2,3))