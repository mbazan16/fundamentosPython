def aplicar_descuento(importe, descuento):
    return importe*(1 - descuento/100);


def aplicar_iva(importe, iva):
    return importe*(1 + iva/100);

def precio_final(cesta,funcion):
    sumaTotal=0;
    for precio,porcentaje in cesta.items():
        sumaTotal += funcion(precio,porcentaje)
    return sumaTotal;

cesta ={12:21,34:2,12:2}
print("Suma Total con Descuentos:", precio_final(cesta,aplicar_descuento))

print("Suma Total con IVA:", precio_final(cesta,aplicar_iva))