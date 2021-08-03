from .sixsideddie import SixSidedDie
from .exceptions import IndicesOutOfBoundsError, DiceAmountExceededError

class DiceCup:
    """
    Class for storing a variable length list of random numbers.

    This list of random numbers represent the dice inside a dice cup.
    These can harbor different combinations.
    """
    def __init__(self, dice_amount) -> None:
        self.dice_amount = dice_amount
        self.dice = self.roll(self.dice_amount)

    def roll(self, dice_amount):
        if dice_amount > self.dice_amount:
            raise DiceAmountExceededError
        dice = []
        for i in range(dice_amount):
            dice.append(SixSidedDie())
        return dice

    def get_dice(self) -> "list[str]":
        dice = []
        for die in self.dice:
            dice.append(str(die))
    
    def choose_dice(self, dice_indexes: "list[int]") -> "list[SixSidedDie]":
        if range(0, len(self.dice) - 1) not in dice_indexes:
            illegal_indexes = [i for i \
                in dice_indexes if i > len(self.dice) or i < 0]
            raise IndicesOutOfBoundsError(illegal_indexes)
        staying_dice = []
        dice_indexes.sort()
        dice_indexes.reverse()
        for die_index in dice_indexes:
            staying_dice.append(self.dice.pop(die_index))
        self.dice_amount = len(self.dice)
        return staying_dice