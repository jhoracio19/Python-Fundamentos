# Default parameter
def hello(greet = 'Hola', name = 'Invitado'):
    
    """
    Info: Esta es una función para devolver un saludo personalizado
    """
    print(f'{greet}, {name}')

# Keyword arguments
hello(name = 'Mauricio', greet = 'Que onda')

def multiply(a: float = 0, b: float = 0) -> float:
    """
    Info: Esta es una función para multiplicar dos números
    """
    return a * b

print(multiply(2,3))