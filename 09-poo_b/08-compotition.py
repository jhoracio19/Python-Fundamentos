
class Flyer:
    def fly(self):
        print("Puedo volar.")
    
    def do_something(self):
        print("FLY FLY")

class Swimmer:
    def swim(self):
        print("Puedo nadar.")
    
    def do_something(self):
        print("Swim Swim")

class Duck:
    
    def __init__(self):
        self.flyer = Flyer()
        self.swimer = Swimmer()
    
    def quack(self):
        print("Quack!")
    
    def start_fly(self):
        self.flyer.fly() 
    
    def star_swim(self):
        self.swimer.swim()

donald = Duck()
donald.start_fly()
donald.star_swim()
donald.quack()
# donald.do_something()

# MRO (Method Resolution Order)
# print(Duck.__mro__)