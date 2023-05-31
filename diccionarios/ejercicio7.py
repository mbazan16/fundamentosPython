cesta_compra = {}
continuar = True

while continuar:
    clave = input('Producto:').title();
    valor = float(input('Precio producto: '))
    cesta_compra[clave] = valor
    continuar = input('Añadir más productos (S/N)').upper() == 'S'

precio_total = 0;
for producto, precio in cesta_compra.items():
    print(producto, '\t', precio)
    precio_total += precio;

print('El precio total es:', str(precio_total))
