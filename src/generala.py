from random import randint
from collections import defaultdict
from .dicecup import DiceCup
from .helpers import *
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

def enter_players() -> "list[str]":
    players_names = []
    name = None
    print("Enter player name (enter nothing to stop entering player)")
    while name == "" or name is None:
        name = input("Name: ")
        name.lower()
        if name != "" and name not in players_names:
            players_names.append(name)
        if name == "" and len(players_names) < 2:
            choice = ""
            while choice == "":
                choice = input("You didn't enter enough players. \
Quit game? (y/n): ")
            if choice == 'y':
                exit()
            elif choice == 'n':
                name = None
                continue
        elif name == "" and len(players_names) >= 2:
            break
        name = None
    players_names = [name[0].upper() for name in players_names]
    return players_names

def which_combination(combinations: "dict[Combination, int]") -> Combination:
    choice = ""
    print("Which combination do you want? Write it down verbatim: ")
    print(combinations)
    while choice not in combinations.keys:
        choice = input("")
    return combinations[choice]

def main():
    players_names = enter_players()
    players = []
    for player_name in players_names:
        players.append(Player(player_name))
    game = Generala(players)
    game.print_scorecard()
    game.start_turn()
    game.turn.play()

if __name__ == "__main__":
    main()