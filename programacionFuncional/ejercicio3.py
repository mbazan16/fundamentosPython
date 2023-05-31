from math import sin, cos, tan, exp, log
funciones = {'1': sin, '2': cos, '3': tan, '4': exp, '5': log}


def aplicar_a_lista(lista, funcion):
    newLista=[]
    for elemento in lista:
        newLista.append(funcion(elemento))
    return newLista;


lista = [1, 2, 3, 4, 5]

print(aplicar_a_lista(lista, funciones['1']))
