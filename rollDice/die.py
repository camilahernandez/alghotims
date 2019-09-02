import random

class Die():
    def __init__(self,num_sides = 6):
        self.num_sides = num_sides
    
    def roll(self):
        """Return a random number between 1 and the number of sides"""
        return random.randint(1, self.num_sides)