
# Métodos de adición 

numbers_list = [1,2,3,4,5]
print(numbers_list)

# append() (ingresar datos al final de la lista)

numbers_list.append(100)
numbers_list.append(200)
# print(numbers_list)
# print(numbers_list.append(200))

# insert() (donde inserrtar datos especificamente)
numbers_list.insert(1, 200)
numbers_list.insert(3, 300)

# extends() (fusiona lista con otra lista)
numbers_list.extend([11,21,33])

print(numbers_list)

