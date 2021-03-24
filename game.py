import math
from human import Human
from computer import Computer


def game():
    print('Hello!\n--------------------\nWelcome to RPSLS!\n--------------------\n'
          'Here are the game Rules:\nRock crushes Scissors\nScissors cuts Paper\n'
          'Paper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\n'
          'Scissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\n'
          'Spock vaporizes Rock\n')
    player1 = Human()
    print(f'Welcome {player1.id}')
    opponent = input('\nDo you want to play against a computer, or a human?')
    if opponent == 'computer':
        player2 = Computer()
        print(f'Welcome {player2.id}\n')
    else:
        player2 = Human()
        print(f'Welcome {player2.id}\n')
    games = input('How many games would you like this series to be the best of?')
    games = int(games)
    games /= 2
    games = math.floor(games)
    games += 1
    player1_points = 0
    player2_points = 0
    while player1_points < games and player2_points < games:
        print(f'{player1.id} it is your turn\n')
        player1_turn = player1.gesture_choice()
        print(f'{player2.id} it is your turn\n')
        player2_turn = player2.gesture_choice()
        for beat in player2_turn.beats:
            if player1_turn.name == beat:
                print(f'{player2.id} wins this round')
                player2_points += 1
        for lose in player2_turn.loses:
            if player1_turn.name == lose:
                print(f'{player1.id} wins this round')
                player1_points += 1
        if player1_turn.name == player2_turn.ties:
            print('This one is a draw!')
    if player1_points == games:
        print(f'{player1.id} wins!')
    if player2_points == games:
        print(f'{player2.id} wins!')
