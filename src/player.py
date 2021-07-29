from .dicecup import DiceCup
from .helpers import Combination
from .sixsideddie import SixSidedDie

class Player:
    """
    Class representing a player.

    A player has a name, a hand, and on their turn (!), they roll the dice
    and choose what to make part of their hand.
    """
    def __init__(self, name: str) -> None:
        self.scorecard = self.init_scorecard()
        self.name = name
        self.hand = self.empty_hand()
        self.dice_cup = DiceCup()

    def init_scorecard(self) -> "dict[Combination, int]":
        scorecard = {}
        for combination in Combination:
            scorecard[combination] = None
        return scorecard
    
    def empty_hand(self):
        self.hand = []
        return self.hand

    def get_initial(self) -> str:
        return self.name[0]

    def calculate_total_score(self) -> int:
        total_score = 0
        for score in self.scorecard.values:
            total_score += score
        return total_score

    def choose_dice(self, dice_numbers: "list[int]") -> "list[SixSidedDie]":
        self.hand += self.dice_cup.get_dice(dice_numbers)