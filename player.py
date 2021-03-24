from gesture import Gesture
#


def generate_gestures_list():
    rock = Gesture('Rock', 'Scissors', 'Lizard', 'Paper', 'Spock', 'Rock')
    paper = Gesture('Paper', 'Rock', 'Spock', 'Scissors', 'Lizard', 'Paper')
    scissors = Gesture('Scissor', 'Paper', 'Lizard', 'Rock', 'Spock', 'Scissors')
    lizard = Gesture('Lizard', 'Spock', 'Paper', 'Rock', 'Scissors', 'Lizard')
    spock = Gesture('Spock', 'Scissors', 'Rock', 'Paper', 'Lizard', 'Spock')
    gestures = [rock, paper, scissors, lizard, spock]
    return gestures


class Player:
    def __init__(self):
        self.gestures = generate_gestures_list()
