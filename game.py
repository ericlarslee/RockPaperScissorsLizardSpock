from human import Human


def game():
    print('Hello!\nWelcome to RPSLS!\nHere are the game Rules:'
          '\nRock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\n'
          'Rock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\n'
          'Scissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\n'
          'Spock vaporizes Rock')
    player1 = (Human(input('What is your name?')))
    print(player1)
