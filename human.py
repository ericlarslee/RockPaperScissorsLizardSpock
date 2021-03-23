from player import Player


class Human(Player):
    def __init__(self, id):
        self.id = id
        super().__init__(entry)