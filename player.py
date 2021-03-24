from gesture import Gesture


class Player:
    def __init__(self):
        self.gestures = []
        self.generate_gestures_list()

    def generate_gestures_list(self):
        rock = Gesture('Rock', 'Scissors', 'Lizard', 'Paper', 'Spock', 'Rock')
        paper = Gesture('Paper', 'Rock', 'Spock', 'Scissors', 'Lizard', 'Paper')
        scissors = Gesture('Scissor', 'Paper', 'Lizard', 'Rock', 'Spock', 'Scissors')
        lizard = Gesture('Lizard', 'Spock', 'Paper', 'Rock', 'Scissors', 'Lizard')
        spock = Gesture('Spock', 'Scissors', 'Rock', 'Paper', 'Lizard', 'Spock')
        self.gestures = [rock, paper, scissors, lizard, spock]
