# Sistema de calificaciones
# 1. Pida al usuario el número de estudiantes a registrar
# 2. Por cada estudiante: Pida su nombre y calificación (0-100)
# 3. Guarde los datos en un diccionario, donde la clave sea el nombre y el valor la calificación
# 4. Al final:
#       - Muestre todos los estudiantes con su calificación
#       - Diga cuantos aprobaron (>= 70) y cuantos reprobaron (<70)
#       - Muestre la calificación más alta y a quién pertenece

students = {}

count = int(input('Cuantos estudiantes quiere registrar? '))

for i in range(count):
    name = input('Nombre: ')
    score = int(input('Calificación: '))
    students[name] = score

print(students)
