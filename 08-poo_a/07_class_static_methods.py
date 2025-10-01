
class Person:
    species = 'Humano'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def change_species(cls,new_specie):
        cls.species = new_specie
    
    @staticmethod
    def is_older(age):
        return  age >= 18


# person1 = Person('Horacio', 21)
# print(person1.species)
# Person.change_species("Reptilianos")
# print(person1.species)

# person2 = Person('Horacio', 21)
# print(person2.species)

print(Person.is_older(16)) 
person1 = Person('Horacio', 21)
print(Person.is_older(person1.age)) 