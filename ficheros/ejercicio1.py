n = int(input('Numero entre el 1 -10:'))
nombre_fichero = 'tabla-'+str(n)+'.txt'
fichero = open(nombre_fichero, 'w')
for i in range(1,11):
    multiplicacion = i * n;
    cadena = str(n) + ' * ' + str(i) + ' = ' + str(multiplicacion) + '\n'
    fichero.write(cadena)
fichero.close()
