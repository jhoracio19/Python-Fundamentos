
students = {
    "Ana": [8, 7, 9],
    "Luis": [6, 5, 7],
    "Sofía": [10, 9, 10]
}


# Agregar nuevo estudiante 
students.update({'Horacio': [8,7,10]})
print(students)

# Sacar el promedio de un estudiante existente
# print(students['Luis'])

notes_luis = students['Luis']
promedio_luis = sum(notes_luis) / len(notes_luis)
print('Promedio de Luis es de: ',promedio_luis)

# El promedio del estudiante nuevo
notes_horacio = students['Horacio']
promedio_horacio = sum(notes_horacio) / len(notes_horacio)
print('Promedio de Horacio es de: ',promedio_horacio)
