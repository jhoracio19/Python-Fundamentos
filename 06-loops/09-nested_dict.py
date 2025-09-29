
nested_dict = {
    'Persona1' : {'Nombre' : 'Gerardo', 'Edad' : 21 , 'Ciudad' : 'CDMX'},
    'Persona2' : {'Nombre' : 'Horacio', 'Edad' : 21 , 'Ciudad' : 'Tlaxcala'},
    'Persona3' : {'Nombre' : 'Naomi', 'Edad' : 20 , 'Ciudad' : 'Puebla'}
}

for key, value in nested_dict.items():
    print(f'{key}: ')
    for sub_key, sub_value in value.items():
        print(f'   {sub_key}: {sub_value}')