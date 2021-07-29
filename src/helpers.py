from defs import Combination
from collections import defaultdict
from re import split
from .sixsideddie import SixSidedDie
from .dicecup import DiceCup

def possible_combinations(hand: "list[SixSidedDie]") \
                          -> "dict[Combination, int]":
    dice_dict = defaultdict(int)
    dice_values: list[Combination]
    score_dict: dict[Combination, int]
    for die in hand:
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
    for die in hand:
        if dice_dict[die] > 1:
            is_straight = False
    if dice_dict[3] != 1 or \
        dice_dict[4] != 1 or \
        dice_dict[5] != 1:
        is_straight = False
    if is_straight:
        score_dict[Combination.STRAIGHT] = 20
    return score_dict

def choose_staying_dice(dice_cup: DiceCup) -> "list[int]":
    printable_dice = ""
    for die in dice_cup.dice:
        printable_dice += str(die) + '\t'
    print("Choose which dice stay \
(refer to them by their position: 1, 2, ...)")
    position = 1
    positions_string = ""
    for die in dice_cup.dice:
        _ = die
        positions_string += str(position) + '\t'
        position += 1
    print(positions_string)
    str_staying_dice_indexes = input(printable_dice)
    str_dice_indexes = split(',|, ', str_staying_dice_indexes)
    if str_dice_indexes == ['']:
        return []
    else:
        return [(int(index) - 1) for index in str_dice_indexes]

def enter_players() -> "list[str]":
    players_names = []
    name = None
    print("Enter player name (enter nothing to stop entering player)")
    while name == "" or name is None:
        name = input("Name: ")
        name.lower()
        if name != "":
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