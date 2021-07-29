from .helpers import Combination
from .sixsideddie import SixSidedDie
from itertools import count, next

class Player:
    """
    Class representing a player.

    A player has a name, a hand, and on their turn (!), they roll the dice
    and choose what to make part of their hand.
    """
    id_iter = count()

    def __init__(self, name: str) -> None:
        self.id = next(self.id_iter)
        self.name = name
        self.scorecard = self.init_personal_scorecard()
        self.hand = self.empty_hand()

    def init_personal_scorecard(self) -> "dict[Combination, int]":
        scorecard = {}
        for combination in Combination:
            scorecard[combination] = None
        return scorecard

    def add_die_to_hand(self, die: SixSidedDie) -> None:
        self.hand.append(die)

    def add_dice_to_hand(self, dice: "list[SixSidedDie]") -> None:
        for die in dice:
            self.add_die_to_hand(die)
    
    def empty_hand(self) -> list:
        self.hand = []
        return self.hand

    def calculate_total_score(self) -> int:
        total_score = 0
        for score in self.scorecard.values:
            total_score += score
        return total_score