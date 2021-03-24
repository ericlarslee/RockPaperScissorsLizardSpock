from player import generate_gestures_list
from human import Human
from computer import Computer

gestures = generate_gestures_list()


def turn_cycle(player1, player2):
    player1_points = 0
    player2_points = 0
    while player1_points < 2 and player2_points < 2:
        player1_turn = player1.Human.gesture_choice()
        player2_turn = player2.type().gesture_choice()

def game():
    print('Hello!\n--------------------\nWelcome to RPSLS!\n--------------------\n'
          'Here are the game Rules:\nRock crushes Scissors\nScissors cuts Paper\n'
          'Paper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\n'
          'Scissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\n'
          'Spock vaporizes Rock')
    player1 = Human()
    print(f'Welcome {player1.id}')
    opponent = input('\nDo you want to play against a computer, or a human?')
    if opponent == 'computer':
        player2 = Computer()
        print(f'Welcome {player2.id}')
    if opponent == 'human':
        player2 = Human()
        print(f'Welcome {player2.id}')
    #else:
    #    while opponent != 'computer' or opponent != 'human':
    #        opponent = input('It looks like your last answer was not "human" or "computer"\n'
    #                         '. We are currently working on compatibility to play RPSLS with\n'
    #                         'animals, but it is not here yet. For now, please enter a valid answer.')
    #        if opponent == 'computer':
    #            player2 = Computer()
    #            print(f'Welcome {player2.id}')
    #        elif opponent == 'human':
    #            player2 = Human()
    #            print(f'Welcome {player2.id}')
