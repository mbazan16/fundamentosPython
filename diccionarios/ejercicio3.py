preciosFruta ={'platano': 1.35, 'manzana': 0.8, 'pera': 0.85, 'naranja': 0.7}
fruta = input('Dame fruta: ')

if fruta.lower() in preciosFruta:
    kgFruta = float(input('Dame kg de fruta: '))
    print('El precio es:' + str(preciosFruta.get(fruta.lower()) * kgFruta))
else:
    print('La fruta no esta en el diccionario')