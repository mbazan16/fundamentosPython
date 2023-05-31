def cuenta_palabras(frase):
    inf_palabras = {}
    palabras = frase.split();
    for palabra in palabras:
        inf_palabras[palabra] = len(palabra)
    return inf_palabras


def cuenta_palabras2(frase):
    palabras = frase.split()
    longitudes = map(len, palabras)
    return dict(zip(palabras, longitudes))


def cuenta_palabras3(frase):
    return {palabra:len(palabra) for palabra in frase.split()}

print(cuenta_palabras('Esto es una prueba de conteo de palabras de una frase'))
print(cuenta_palabras2('Esto es una prueba de conteo de palabras de una frase'))
print(cuenta_palabras3('Esto es una prueba de conteo de palabras de una frase'))
