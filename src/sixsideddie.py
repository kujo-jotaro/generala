from random import randint
from .helpers import DICE_STRINGS

class SixSidedDie:
    """
    This class represents a pseudo-random six-sided die.
    
    Every initialization "rolls" a die.
    """
    def __init__(self):
        self.current_value = self.roll()

    def roll(self):
        self.current_value = randint(1, 6)
        return self.current_value
    
    def __str__(self):
        return f'{DICE_STRINGS[self.current_value]}'

    def __repr__(self):
        return f'Die: {self.__str__}'