
class Person:
    species = "Humano"
    def __init__(self, name):
        self.name = name # atributos de 
        self._energy = 100 # _ representa que es una variable protected
    
    def _waste_energy(self, quantity):
        self._energy -= quantity
    
    



person1 = Person('Horacio') 
print(person1.name)
print(person1._energy)
print(person1._waste_energy(20))
print(person1._energy)
