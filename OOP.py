import random

class Person:
    
    def __init__(self, name, dumb_level):
        self.name = name
        self.dumb_level = dumb_level
        
    def desc(self):
        print (f"{self.name} is on the {self.dumb_level}th plane of stupidity.")
    
    def sound(self, noise):
        print(f"{self.name} says {noise}")
    
    
reid = Person("Reid", 420)
graden = Person("Graden", 69)

reid.desc()

graden.desc()

reid.sound("duh")

graden.sound("woof")