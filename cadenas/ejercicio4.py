numero_telefono = input("Dame numero teléfono (+pp-nnnnnnnnn-ee):")

print("Prefijo:" + numero_telefono[:3])
print("Numero:" + numero_telefono[4:-3])
print("Extension:" + numero_telefono[-3:])