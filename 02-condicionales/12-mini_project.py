# Instrucciones

# Crearas un programa de evaluación de candidatos potenciales con conocimientos en Python para RH.
# Obtendras el nombre, años de experiencia y habilidades.

# Evaluaras: 
# * Si el candidato sabe Python/Django, tienes +3 años de experiencia: Candidato Optimo
# * Si el candidato sabe Python/Django, tiene +1 año de experiencia: Buen candidato
# * Si el candidato sabe Python/Django: Posible candidato
# * Si el candidato no sabe Python: No optimo, se guardara CV

# * Consejo: Ocupa los metodos .split()

name = input('Nombre del candidato: ')
experience = int(input('Años de experiencia: '))
skills = input('Ingrese sus habilidades separadas por comas: (ej. Python, Laravel, Golang, Django, etc.) ').split(',')

evaluate_skills = 'Python' in skills or 'Django' in skills

result = ''

if evaluate_skills:
    if experience >= 3:
        result = 'Candidato Optimo'
    elif experience >= 1:
        result = 'Buen Candidato'
    else:
        result = 'Posible Candidato'
else:
    result = 'No apto, se guardara CV para futuras ofertas'


print(f'El candidato {name} es: {result}')


