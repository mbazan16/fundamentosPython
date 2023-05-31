def funcion_booleana(numero):
    if numero % 2 == 0:
        return True
    return False


def conseguir_validos(lista, funcion):
    newLista=[]
    for elemento in lista:
        if funcion(elemento):
            newLista.append(elemento)
    return newLista;


lista = [1, 2, 3, 4, 5]

print(conseguir_validos(lista, funcion_booleana))
