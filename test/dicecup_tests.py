from src.dicecup import DiceCup
from src.exceptions import IndicesOutOfBoundsError, DiceAmountExceededError

passed = True

def pass_extra_indices():
    global passed
    dice_cup = DiceCup(5)
    indices = [1, 2, 3, 4, 5, 6]
    try:
        dice_cup.choose_dice(indices)
        passed &= False
    except IndicesOutOfBoundsError as e:
        print(e)

def illegal_roll():
    global passed
    dice_cup = DiceCup(5)
    try:
        dice_cup.roll(6)
        passed &= False
    except DiceAmountExceededError as e:
        print(e)

def main():
    global passed
    pass_extra_indices()
    illegal_roll()
    return passed

if __name__ == '__main__':
    main()