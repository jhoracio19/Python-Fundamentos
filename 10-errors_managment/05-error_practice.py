
class InvalidAgeError(Exception):
    def __init__(self, age, message='La edad debe ser mayor o igual a 18.'):
        self.age = age
        self.message =message
        super().__init__(self.message)

class InvalidMailError(Exception):
    def __init__(self, mail, message="Mail con formato no válido."):
        self.mail = mail
        self.message = message
        super().__init__(self.message)

def register_user(name, age, mail):
    if "@" not in mail or '.' not in mail.split("@")[-1]:
        raise InvalidMailError(mail)
    if age < 18:
        raise InvalidAgeError(age)
    print(f'Usuario: {name} registrado con mail: {mail} y edad: {age}')


try:
    register_user("Horacio", 25, 'jhoracio19@hotmail.com')
except InvalidMailError as er:
    print(f'Error: {er}')
except InvalidAgeError as e:
    print(f'Error: {e}')