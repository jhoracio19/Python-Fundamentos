
# numbers = [1,2,3,4,5]

# # Iterables: Iterables, listas, diccionarios, set, tuplas
# # Iterador: Objeto que recuerda su posicion

# for number in numbers:
#     print(number)
    
# iterator = iter(numbers)
# print(iterator)
# print(next(iterator))

user = {
    'name' : 'Horacio',
    'age' : 21,
    'can_swim' : True
}

for key, value in user.items():
    print(key ,value)