#  letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numeros = "0123456789"
# caracteres = "!@#$%^&*()_+-=[]{}\:;,.<>?/"
# Formula simple: (item * 7 + 3) % len(caracteres)

# entrada  = 8
# salida = "&D#234SN"

import string
import random

def password_generator(length): 
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numers = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{}\:;,.<>?/"
    chars = string.ascii_letters + string.digits + string.punctuation
    password = []
    
    for item in range(length):
        index = random.choice(chars)
        password.append(index)
    
    return "".join(password)

length = int(input("Ingrese la longitud de la contraseña: "))
print("Tu contraseña es: ", password_generator(length))