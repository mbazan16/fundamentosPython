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


def conseguir_calificaciones(notas):

    return list(map(calificacion, notas))


notas =[5, 3, 7, 10, 3, 8]

print(conseguir_calificaciones(notas))
