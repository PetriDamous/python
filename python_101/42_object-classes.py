#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods

class Mavrick:
    def __init__(self, name, weakness, reward):
        self.name = name
        self.weakness = weakness
        self.reward = reward

    def print_mavrick(self):
        print("name: ", self.name)
        print("weakness: ", self.weakness)
        print("reward: ", self.reward)

mav_1 = Mavrick(name="Spark Mandrill", weakness="Shotgun Ice", reward="Electric Spark")

mav_1.print_mavrick()

Mavrick.print_mavrick(mav_1) # Same as mav_1.print_mavrick()