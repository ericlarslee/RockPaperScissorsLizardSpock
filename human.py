from player import Player


class Human(Player):
    def __init__(self):
        self.id = 'human'
        super().__init__()