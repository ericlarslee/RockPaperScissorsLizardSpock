from player import Player
import random


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.id = 'computer'

    def gesture_choice(self):
        i = random.randint(1, len(self.gestures))
        print(self.gestures[i])
        return self.gestures[i]
