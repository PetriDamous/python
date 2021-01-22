class Person:
    def move(self):
        print("moves 4 paces")

class Healer(Person):
    def heal(self):
        print("heals 10 HP")

class Fighter(Person):
    def fight(self):
        print("10 HP damage")
    
    def move(self):
        print("moves 10 paces")

# class Wizard(Fighter, )