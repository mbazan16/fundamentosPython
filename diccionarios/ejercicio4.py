meses ={'01': 'Enero', '02': 'Febrero', '03': 'Marzo', '04': 'Abril',
               '05': 'Mayo', '06': 'Junio', '07': 'Julio', '08': 'Agosto',
               '09': 'Septiembre', '10': 'Octubre', '11': 'Noviembre', '12': 'Diciembre'}
fecha = input('Dame fecha (formato dd/mm/aaaa):')

fechaList = fecha.split("/");

print('La fecha es el '+fechaList[0] + ' de ' + meses.get(fechaList[1]) + ' del ' + fechaList[2])
