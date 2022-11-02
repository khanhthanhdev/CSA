
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def print_sound(self):
        print(self.name,self.sound)

class Dog(Animal):
    def __init__(self,name,sound):
        Animal.__init__(self,name,sound)
    def print_sound(self):
        print("Gâu gâu")

dog = Dog()
dog.print_sound()
        
