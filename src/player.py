from .dicecup import DiceCup
from .helpers import Combination

class Player:
    def __init__(self, name: str) -> None:
        self.scorecard = self.init_scorecard()
        self.name = name
        self.hand = None
        self.dice_cup = DiceCup()

    def init_scorecard(self) -> "dict[Combination, int]":
        scorecard = {}
        for combination in Combination:
            scorecard[combination] = None
        return scorecard

    def get_initial(self) -> str:
        return self.name[0]

    def calculate_total_score(self) -> int:
        total_score = 0
        for score in self.scorecard.values:
            total_score += score
        return total_score