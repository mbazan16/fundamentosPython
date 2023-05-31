
inmuebles=[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def anadir_precio(inmueble):
    precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1-(2023 -inmueble['año'])/100)
    if inmueble['zona'] == 'B':
        precio *= 1.5
    inmueble['precio']=precio
    return inmueble


def inmuebles_objetivo(inmuebles, precio):
    def precio_menor(inmueble):
        return inmueble['precio'] <= precio
    return list(filter(precio_menor,map(anadir_precio, inmuebles)))


print(inmuebles_objetivo(inmuebles, 1000000))
