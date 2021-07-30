from dicecup import DiceCup
from .helpers import Combination, which_combination
from .player import Player

class Turn():
    def __init__(self) -> None:
        self.throw_count = 0
        self.ended = False
    
    def throw(self):
        self.throw_count += 1
        if self.throw_count == 3:
            self.ended = True
    
    def is_ended(self):
        return self.ended