palabra = input("Deme una palabra: ")
letras = list(palabra)
letrasReves = list(palabra)
letrasReves.reverse()
if letras == letrasReves:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")


