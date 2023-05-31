precio = input("Precio (con dos decimales):")
euros = precio[:precio.find('.')]
centimos = precio[precio.find('.')+1:]

print("Euros:" + euros)
print("Centimos:" + centimos)