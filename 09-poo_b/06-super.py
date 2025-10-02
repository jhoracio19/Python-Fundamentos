
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self):
        print(f'{self.name} hace un sonido')
    
    def info(self):
        if self.age == 1:
            print(f"Soy {self.name}, tengo {self.age} año.")
        else:
            print(f"Soy {self.name}, tengo {self.age} años.")

class Dog(Animal):
    
    def __init__(self, name, age, breed):
        super().__init__(name,age)
        self.breed = breed
    
    
    def sound(self):
        super().sound()
        print(f'{self.name} dice: Guau!')
    
    def info(self):
        super().info()
        print(f"Soy de raza {self.breed}")

class Cat(Animal):
        def sound(self):
            super().sound()
            print(f'{self.name} dice: Miau!')

firulais = Dog('Bonnie', 1, "Beagle")
firulais.sound()
firulais.info()

