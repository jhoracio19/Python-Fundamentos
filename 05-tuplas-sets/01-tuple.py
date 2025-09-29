
my_tuple = (1,2,3,4,"Hola", True, "Hi", 5, 4, 3,2,2)
print(my_tuple)

# Ordenada 
# Inmutables (no se pude cambiar despues de su creacion)
# Permite duplicados
# Indexadas

# Métodos

print(my_tuple.count(2)) # count() dice cuantas veces esta el valor en la tupla


print(my_tuple.index("Hola")) # index() me va a dar el indice del primer valor

# my_tuple[4] = "Mundo" # Esto no se puede

new_tuple = my_tuple[4]
print(new_tuple)

week = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

