nombre = input("Dame nombre :").upper()
sexo = input("Dame sexo (H/M) :").upper()
grupo="Ninguno"
if nombre < "M" and sexo == "M":
   grupo ="A"
elif nombre > "N" and sexo == "H":
    grupo = "A"
else:
    grupo="B"

print("El grupo es "+grupo)