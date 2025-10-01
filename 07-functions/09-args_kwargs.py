
def big_function(*args, **kwargs): # odo lo que pasa en *args pasan como tupla
    print(args) # returna una tupla
    print(kwargs) # returna un diccionario
    total = 0
    
    for item in kwargs.values():
        total += item
    
    return sum(args) + total

print(big_function(1,2, num1=23, num2=45))