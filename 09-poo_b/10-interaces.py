
from abc import ABC, abstractmethod

# Clase abstracta
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def sleep(self):
        print("zzz..")

class Dog(Animal):
    def sound(self):
        return "Woof Woof!"

    def sleep(self):
        return "zzz.."

class Cat(Animal):
    def sound(self):
        return "Miau Miau!"

    def sleep(self):
        return "zzz.."

bonnie = Dog()
gatita = Cat()

print(bonnie.sound())
print(bonnie.sleep())

print(gatita.sound())
print(gatita.sleep())