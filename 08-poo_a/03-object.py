
class Person:
    def __init__(self, name, age):
        if (age > 18):
            self.name = name
            self.age = age

person1 = Person('Horacio', 21)

print(person1)
print(person1.name)
print(person1.age)

person2 = Person('Naomi', 20)

print(person2)
print(person2.name)
print(person2.age)