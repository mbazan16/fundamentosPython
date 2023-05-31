n = int(input('Numero entre el 1 -10:'))
m = int(input('Numero entre el 1 -10:'))
nombre_fichero = 'tabla-'+str(n)+'.txt'
try:
    with open(nombre_fichero, 'r') as fichero:
        lineas = fichero.readlines()
    print(lineas[m - 1])
except:
    print('El fichero '+nombre_fichero+' no existe')

