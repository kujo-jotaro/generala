from enum import Enum

DICE_STRINGS = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

class Combination(Enum):
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    STRAIGHT = 20
    FULL_HOUSE = 30
    FOUR_OF_A_KIND = 40
    GENERALA = 50
    DOUBLE_GENERALA = 100

COMBINATIONS_INITIALS = { Combination.ONES:             '1',
                          Combination.TWOS:             '2',
                          Combination.THREES:           '3',
                          Combination.FOURS:            '4',
                          Combination.FIVES:            '5',
                          Combination.SIXES:            '6',
                          Combination.STRAIGHT:         'E',
                          Combination.FULL_HOUSE:       'F',
                          Combination.FOUR_OF_A_KIND:   'P',
                          Combination.GENERALA:         'G',
                          Combination.DOUBLE_GENERALA:  'DG' }