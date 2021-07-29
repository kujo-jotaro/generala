from .helpers import COMBINATIONS_INITIALS
from .turn import Turn
from .player import Player

class Generala:
    def __init__(self, players: "list[Player]") -> None:
        self.players = players
        self.turn: Turn
    
    def start_turn(self) -> None:
        self.turn = Turn(self.players[0])

    def print_scorecard(self) -> None:
        initials = ""
        for player in self.players:
            initials += player.get_initial().center(3) + '|'
        print('|'.rjust(3) + initials)
        dashes = "-" * (3 + 4 * len(self.players))
        print(dashes)
        for combination_key in COMBINATIONS_INITIALS:
            line = COMBINATIONS_INITIALS[combination_key].rjust(2) + '|'
            for player in self.players:
                if player.scorecard[combination_key] is not None:
                    line += (str)(player.scorecard[combination_key]).center(3)
                else:
                    line += ' '.center(3)
                line += '|'
            print(line)