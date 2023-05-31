datosUsuario = {}
continuar = True

while continuar:
    clave = input('Dato a introducir:').title();
    valor = input(clave +": ")
    datosUsuario[clave] = valor
    print(datosUsuario)
    continuar = input('Añadir más datos (S/N)').upper() == 'S'
