# Generala

## Generala sim written in Python
---

This is my first attempt at following good OOP principles and project file management. Just for fun and learning.

### Classes:

#### Generala
The main game class. It contains the players and the info needed to keep a scorecard of all the players involved.

#### Turn
The turn class. Encompasses all the logic involved in a turn (rolling a dice, rotating players, etc.)

#### Player
The player class. A player has a name, and an id (Multiple player can have the same name). They also hold a hand of dice whenever they make a play.

#### SixSidedDie
A random number generator from 1 to 6, just like a fair six-sided die. Players roll these in order to determine their next move.

#### DiceCup
A container for the amount of dice in game. Starts with 5, and may decrease in number as players start keeping dice for their combinations.

### Helpers:

#### Combination
An Enum sub-class which holds the possible combinations a player can attain during the game. Also serve as indices for the scorecard of the game.

#### DICE_STRINGS
A nice, Unicode representation of dice. Might break on incompatible terminals.

#### COMBINATION_INITIALS
For scorecard annotation.
