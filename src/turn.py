from .helpers import Combination, which_combination
from .player import Player

class Turn():
    turn_number = 0

    def __init__(self, player: Player) -> None:
        self.player = player

    def play(self) -> None:
        self.player.roll()
        choice = ''
        while choice != 'y' and choice != 'n':
            choice = input("Do you want to stay? (y/n)")
        if choice == 'y':
            self.end()
        else:
            staying_dice = self.player.choose_staying_dice()
            self.player.dice_cup.refill(staying_dice)
            self.play()

    def end(self, combination: Combination) -> None:
        self.player.scorecard[combination] = \
            which_combination(self.player.possible_combinations())
    
    def increase() -> None:
        Turn.turn_number += 1