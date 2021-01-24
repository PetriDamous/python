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

# Inheritance chain

class Person:
    def move(self):
        print("moves 4 paces")

    def jump(self):
        print("jump 10 meters")

class Healer(Person):
    def heal(self):
        print("heals 10 HP")

    def first_aid(self):
        print("heal party 10 HP")

class Fighter(Person):
    def fight(self):
        print("10 HP damage")
    
    def move(self):
        print("moves 10 paces")

    def first_aid(self):
        print("heal self 5 HP")

class Wizard(Fighter, Healer):
    def fire(self):
        print("55 HP fire damage")

    def heal(self):
        print("heals 20 HP")

wizard = Wizard()

# Own wizard method
wizard.fire() # 55 HP fire damage

# Overides Healer class heal and uses own
wizard.heal() # heals 20 HP

# Will inherit the Figher class move method because it is closer in inheritance
wizard.move() # moves 10 paces

# Inherites from Fighter class since Fighter class comes before Healer class in Wizard class argument
wizard.first_aid() # heal self 5 HP

# Inherited passed down from grand parent (Person) to parent (Fighter, Healer)
wizard.jump() # jump 10 meters