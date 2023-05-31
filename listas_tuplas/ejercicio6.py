asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignaturasSuspendidas = asignaturas.copy();
for i in asignaturas:
    nota = int(input("Nota en la asignatura " + i +":"))
    if (nota >= 5):
        asignaturasSuspendidas.remove(i)
print("Asignaturas suspendidas "+str(asignaturasSuspendidas))

