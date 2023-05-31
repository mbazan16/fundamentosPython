correo = input("Correo:")
correo_sin_dominio = correo[:correo.find('@')]
correo = correo_sin_dominio + "@ceu.es"

print("Correo:" + correo)