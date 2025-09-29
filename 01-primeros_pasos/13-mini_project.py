
# Registro
# Recibas de forma dinamica nombre, año nacimiento, correo y contraseña

'''
    Nombre: Horacio
    Email: jhoracio19@hotmail.com
    Tendras 55 años en el 2050
    Tu contraseña es: ****
'''

name = input('Introduce tu nombre: ')
email = input('Introduce tu email: ')
birth_year = int(input('Introduce tu año de nacimiento: '))  
password = input('Introduce tu password: ')

# Calculamos la edad
age_2025 = 2050 - birth_year

print(f'Nombre: {name}')
print(f'Email: {email}')
print(f'Tendras {age_2025} en el 2050')
print(f'Tu contraseña es: {"*" * len(password)}')