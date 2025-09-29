# 1. Pida al usuario un numero limite
# 2. Use un ciclo for con range() desde 1 hasta ese numero
# 3. Imprima ada numero y diga si es par o impar

number = int(input('Ingrese un número límite: '))

for i in range(1 , number + 1):
    if i  % 2 == 0:
        print(f'{i} Numero par')
    else:
        print(f'{i} Numero impar')