# Concatenación

name = 'Horacio'
lastname = 'Ahuactzin'
age = 21

# full_name = name + ' ' + lastname # Esto sirve pero no es una buena practica

full_name = f'{name} {lastname}' # Esto es la forma correcta
message = f'{full_name}, tienes {age}'

print(full_name) # Horacio Ahuactzin
print(message)

print( name + " " + lastname)