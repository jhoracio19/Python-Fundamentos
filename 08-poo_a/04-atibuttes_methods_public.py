
class Person:
    species = "Humano"
    def __init__(self, name, age):
        self.name = name # atributos de instancia
        self.age = age # 
    
    def work(self):
        return(f"{self.name} está trabajando muy duro.")
    
    def eat(self, food):
        if food.lower() == 'tacos':
            return 'SuperPower'
        else:
            return '+Energía'



person1 = Person('Horacio', 21) 
print(person1.name)
print(person1.age)
print(person1.species)
print(person1.work())
print(person1.eat('tacos'))