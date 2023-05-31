def calificacion(nota):
    if nota < 5:
        return 'Suspenso'
    if nota < 7:
        return 'Bien'
    if  nota < 9:
        return 'Notable'
    if nota < 10:
        return 'Sobresaliente'
    return 'Matricula Honor'


def asignatura_aprobada(asignatura):
    return (asignatura[1] >= 5)


def conseguir_calificaciones(notas):
    aprobadas = dict(filter(asignatura_aprobada, notas.items()))
    asignaturas = map(str.upper, aprobadas.keys())
    calificaciones = map(calificacion, aprobadas.values())
    return dict(zip(asignaturas, calificaciones))


print(conseguir_calificaciones({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))


