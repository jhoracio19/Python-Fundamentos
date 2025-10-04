try:
    with open("sinpermisos.txt", 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permisos para leer este archivo")
except Exception as err:
    print(f'Ocurrio un error: {err}')