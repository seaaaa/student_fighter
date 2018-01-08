# First let's create our StudentFighter Class
class StudentFighter(object):

    # Let's define our constructor __init__ method
    def __init__(self, strength, health, name):
        self.strength = strength
        self.name = name
        self.health = health

# Then let's instantiate two student fighters
kalu = StudentFighter(strength=3, health=100, name="Kalu")
david = StudentFighter(strength=5, health=100, name="David")

# Let's print out our fighter's info
print(kalu.name, kalu.strength, kalu.health)
print(david.name, david.strength, david.health)