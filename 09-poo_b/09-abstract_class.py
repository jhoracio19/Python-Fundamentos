
from abc import ABC, abstractmethod

# Clase abstracta
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
    
    def sleep(self):
        print("zzz..")

animal = Animal()