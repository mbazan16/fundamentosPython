
def conIva(importe,iva=21):
    return importe*(1+iva/100)
importe = 1000
print('El iva de ', importe, ' es ', conIva(importe))
