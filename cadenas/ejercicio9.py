fecha_nacimiento = input("Fecha nacimiento:")
dia = fecha_nacimiento[:fecha_nacimiento.find('/')]
mes = fecha_nacimiento[fecha_nacimiento.find('/')+1:fecha_nacimiento.find('/', fecha_nacimiento.find('/')+1)]
anyo = fecha_nacimiento[fecha_nacimiento.find('/', fecha_nacimiento.find('/')+1)+1:]
print("Dia:" + dia)
print("Mes:" + mes)
print("Anyo:" + anyo)