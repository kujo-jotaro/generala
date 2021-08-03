from src.generala import Generala
from src.player import Player
from src.helpers import enter_players

def main():
    players_names = enter_players()
    players = []
    for player_name in players_names:
        players.append(Player(player_name))
    game = Generala(players)
    print(game.get_scorecard())

if __name__ == "__main__":
    main()