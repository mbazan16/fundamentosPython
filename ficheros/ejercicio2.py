n = int(input('Numero entre el 1 -10:'))
nombre_fichero = 'tabla-'+str(n)+'.txt'
try:
    fichero = open(nombre_fichero, 'r')
except:
    print('El fichero '+nombre_fichero+' no existe')
else:
    print(fichero.read())
    fichero.close()
