from player import Player
import random


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.id = 'computer'

    def gesture_choice(self):
        i = random.randint(0, len(self.gestures) - 1)
        return self.gestures[i]
