
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        self.__password = '1234' #name mangling _NOMBRECLASE__password
        # _Person__password
    
    def __generate_password(self):
        return f"$${self.name} {self.age} "




person1 = Person('Horacio', 29) 
print(person1.name)
print(person1._Person__password)
print(person1._Person__generate_password())