class Gesture:
    def __init__(self, name, beats1, beats2, loses1, loses2, ties1):
        self.name = name
        self.beats = [beats1, beats2]
        self.loses = [loses1, loses2]
        self.ties = ties1
