from .player import Player

class Turn():
    def __init__(self) -> None:
        self.current_player = None
        self.throw_count = 0
        self.ended = False

    def next_player(self, player: Player) -> None:
        self.current_player = player
    
    def throw(self) -> None:
        self.throw_count += 1
        if self.throw_count == 3:
            self.ended = True
    
    def is_ended(self) -> bool:
        return self.ended