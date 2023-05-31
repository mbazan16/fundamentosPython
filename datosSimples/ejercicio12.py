PRECIO_NORMAL = 3.49
DESCUENTO = 0.6

num_barras_no_dia = int(input('Numero de barras vendidas que no son del dia:'))

costeNormal = round(num_barras_no_dia * PRECIO_NORMAL, 2)
print(costeNormal)

descuento = round(num_barras_no_dia * DESCUENTO, 2)
print(descuento)

costeFinal = costeNormal - descuento
print(costeFinal)

