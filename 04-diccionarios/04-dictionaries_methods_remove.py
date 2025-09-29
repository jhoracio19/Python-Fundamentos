
user = {
    'name' : 'Horacio',
    'age' : 21,
    'greet' : 'Hola mundo',
    'numbers' : [1,2,3]
}

# .copy()

user_copy = user.copy()
user_copy['age'] = 29

# print(user_copy)


# .pop()

user.pop('age')


# .popitem()

user.popitem()
print(user)

# .update()

user.update({'name': 'José'})
user.update({'cat': 0})
print(user)


# append()
user['skills'] = user.get('skills', [])
user['skills'].append('Python')
user['skills'].append('Django')
print(user)