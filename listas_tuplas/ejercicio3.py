asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "?")
    notas.append(nota)

for i in range(len(asignaturas)):
    print("En la asignatura "+asignaturas[i]+" has sacado la nota "+notas[i])
