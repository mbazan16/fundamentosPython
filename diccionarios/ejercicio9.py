facturas={'2023001':900.90,'2023044':89.5}
opcion=0;
cantidad_cobrada=0;
cantidad_pendiente_cobro =0;

for factura in facturas:
    cantidad_pendiente_cobro += facturas[factura]

while opcion != 3:
    if opcion == 1:
        print('Añadir factura:')
        num_factura = input('Número de factura: ')
        facturas[num_factura] = float(input('Importe factura: '))
        cantidad_pendiente_cobro += facturas[num_factura]
    elif opcion == 2:
        print('Pagar factura:')
        print(facturas)
        num_factura = input('Número de factura: ')
        cantidad_cobrada += facturas[num_factura]
        cantidad_pendiente_cobro -= facturas[num_factura]
        facturas.pop(num_factura)
    print('Cantidad cobrada:', cantidad_cobrada, '€')
    print('Cantidad pendiente de cobro:', cantidad_pendiente_cobro, '€')
    opcion = int(input('Menú:\n 1.Añadir Factura \n 2.Pagar Factura \n 3.Terminar\n Opción:'))


