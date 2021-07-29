from src.dicecup import DiceCup
from src.exceptions import IndicesOutOfBoundsError

def pass_extra_indices():
    indices = [1, 2, 3, 4, 5, 6]
    dice_cup = DiceCup()
    try:
        dice_cup.refill(indices)
    except IndicesOutOfBoundsError:
        exit()
