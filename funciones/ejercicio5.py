
def areaCirculo(radio):
    pi = 3.1416
    return 2*pi*radio
def volumenCilindro(radio,altura):
    return areaCirculo(radio)*altura

radio=3
altura=3
print('El area de un circulo con radio', radio, ' es ', areaCirculo(radio))
print('El volumen de un cilindro con radio', radio, 'y altura', altura, ' es ', volumenCilindro(radio,altura))