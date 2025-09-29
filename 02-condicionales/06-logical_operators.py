
# Evaluar condiciones

# AND (Todos los valores sean verdaderos)

# print( True and True) # True
# print( True and False) # False
# print( False and True) # False
# print( False and False) # False

# # OR (Al menos uno debe ser verdadero)

# print( True or True) # True
# print( True or False) # True
# print( False or True) # True
# print( False or False) # False

# # NOT (negar)

# print( not True) # False
# print(not False) # True


# AND

age = 25
is_licensed = True

if age >= 18 and is_licensed:
    print('Puedes conducir')
    
# OR

is_student = False
membership = True

if is_student or membership:
    print('Obtienes un descuento especial')
    
# NOT

is_admin = False

if not is_admin:
    print('Acceso Denegado')