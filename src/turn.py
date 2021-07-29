from dicecup import DiceCup
from .helpers import Combination, which_combination
from .player import Player

class Turn():
    def __init__(self, players: "list[Player]") -> None:
        self.players = players
        self.current_player = players[0]
        self.dice_cup = DiceCup()

    def next_player(self):
        next_player_id = self.current_player.id + 1
        if next_player_id < len(self.players):
            self.current_player = self.players[self.current_player.id + 1]
        

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

    """
    def end(self, combination: Combination) -> None:
        self.player.scorecard[combination] = \
            which_combination(self.player.possible_combinations())
    """