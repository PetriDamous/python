# pass - allows python to skip an empty block of code

if "dog":
    pass

print("I passed")

# Simple inheritance

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

person1 = Person()
healer1 = Healer()
fighter1 = Fighter()

person1.move() # moves 4 paces

healer1.heal() # heals 10 HP 
healer1.move() # moves 4 paces (inherites from person class)

fighter1.fight() # 10 HP damage
fighter1.move() # moves 10 paces (fighters move method overwrites the person move method)