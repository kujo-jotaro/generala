from collections import defaultdict
from .helpers import Combination
from .sixsideddie import SixSidedDie
from .exceptions import IndicesOutOfBoundsError

class DiceCup:
    """
    Class for storing a variable length list of random numbers.

    This list of random numbers represent the dice inside a dice cup.
    These can harbor different combinations.
    """
    def __init__(self, dice_amount) -> None:
        self.dice_amount = dice_amount
        self.dice = self.roll()

    def roll(self):
        dice = []
        for i in range(self.dice_amount):
            dice.append(SixSidedDie())
        return dice
    
    def refill(self, dice_indexes: "list[int]") -> "list[SixSidedDie]":
        if range(0, len(self.dice) - 1) not in dice_indexes:
            raise IndicesOutOfBoundsError
        staying_dice = []
        dice_indexes.sort()
        dice_indexes.reverse()
        for die_index in dice_indexes:
            staying_dice.append(self.dice.pop(die_index))
        return staying_dice

    def possible_combinations(self) -> "dict[Combination, int]":
        dice_dict = defaultdict(int)
        dice_values: list[Combination]
        score_dict: dict[Combination, int]
        for die in self.dice:
            dice_dict[die] += 1
        for k, v in dice_dict.items:
            dice_values.append(Combination[k])
        for value in dice_values:
            score_dict[value] = dice_dict[value] * value
        if 5 in dice_dict.values:
            score_dict[Combination.GENERALA] = 50
        if 4 in dice_dict.values:
            score_dict[Combination.FOUR_OF_A_KIND] = 40
        if 3 in dice_dict.values and 2 in dice_dict.values:
            score_dict[Combination.FULL_HOUSE] = 30
        is_straight = True
        for die in self.dice:
            if dice_dict[die] > 1:
                is_straight = False
        if dice_dict[3] != 1 or \
           dice_dict[4] != 1 or \
           dice_dict[5] != 1:
            is_straight = False
        if is_straight:
            score_dict[Combination.STRAIGHT] = 20
        return score_dict