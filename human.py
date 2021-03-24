from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
        self.id = input('What is your name?')

    def gesture_choice(self):
        i = 0
        while i < len(self.gestures):
            print((i + 1), ' ', self.gestures[i].name)
            i += 1
        choice = input('Which number would you like to use for your gesture?')
        choice = int(choice)
        choice -= 1
        return self.gestures[choice]
