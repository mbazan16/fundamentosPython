monedas ={'Euro': '€', 'Dollar': '$', 'Yen': 'Y'}
moneda= input('Dame moneda: ')
print(monedas.get(moneda.title(), 'La divisa no está'));
