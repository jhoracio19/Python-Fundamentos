
shopping_cart = [
    'Camisas', #0
    'Tenis', #1 
    'Calcetas', #2
    'Pantalones' #3
]

# [inicio: fin]

# print(shopping_cart[3])

# new_list = shopping_cart[1:4]
# new_list[0] = 'Zapatos' 
# new_list[1] = 'Collar' 

# print(new_list) # Crea una lista nueva
# print(shopping_cart)


# TODO: Copiar una lista

new_cart = shopping_cart [:]
new_cart[0] = 'Playeras'
shopping_cart[1] = 'Zapatos'

print(shopping_cart)
print(new_cart)