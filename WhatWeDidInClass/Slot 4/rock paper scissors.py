# Constants, you should use these in your implementation
ROCK = 1
PAPER = 2
SCISSORS = 3

PLAYER_WINS = 'Player wins!! Woop woop!'
COMPUTER_WINS = 'Robocop wins :-('
TIE = "It's a tie!"

from random import randint

# Your implementation here
def rock_paper_scissors(num):
  computer_choice = randint(1, 3)
  if num == computer_choice:
    return TIE
  if num == 1:
    if computer_choice == 2:
      return COMPUTER_WINS
    elif computer_choice == 3:
      return PLAYER_WINS
  elif num == 2:
    if computer_choice == 1:
      return PLAYER_WINS
    elif computer_choice == 3:
      return COMPUTER_WINS
  elif num == 3:
    if computer_choice == 1:
      return COMPUTER_WINS
    elif computer_choice == 2:
      return PLAYER_WINS
	  
	  
def play_rps():
    print('Welcome to play rock-paper-scissors')
    print('The options are:\nrock: 1\npaper: 2\nscissors: 3')

    result = TIE
    while result == TIE:
        player_choice = input('Give your choice\n')
        
        if not player_choice in ['1', '2', '3']:
            print('Invalid choice')
            continue
            
        result = rock_paper_scissors(int(player_choice))
        print(result)
if __name__ == '__main__':
    play_rps()