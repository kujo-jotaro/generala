from .dicecup import DiceCup
from .helpers import Combination
from re import split

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
    
    def roll(self) -> None:
        for die in self.dice_cup.dice:
            die.roll()

    def choose_staying_dice(self) -> "list[int]":
        printable_dice = ""
        for die in self.dice_cup.dice:
            printable_dice += str(die) + '\t'
        print("Choose which dice stay \
(refer to them by their position: 1, 2, ...)")
        position = 1
        positions_string = ""
        for die in self.dice_cup.dice:
            _ = die
            positions_string += str(position) + '\t'
            position += 1
        print(positions_string)
        str_staying_dice_indexes = input(printable_dice)
        str_dice_indexes = split(',|, ', str_staying_dice_indexes)
        if str_dice_indexes == ['']:
            return []
        else:
            ret = [(int(index) - 1) for index in str_dice_indexes]
            ret.sort()
            ret.reverse()
            return ret

    def calculate_total_score(self) -> int:
        total_score = 0
        for score in self.scorecard.values:
            total_score += score
        return total_score