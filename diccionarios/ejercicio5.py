creditosAsignaturas ={'Matemáticas':6, 'Física': 4, 'Química': 5}
totalCreditos = 0
for asignatura, creditos in creditosAsignaturas.items():
    print("La asignatura ", asignatura," tiene ", str(creditos), " créditos");
    totalCreditos += creditos
print("Los creditos totales del curso son ", str(totalCreditos), " créditos")