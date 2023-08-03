ROCK = 0
PAPER = 1
SCISSORS = 2

choices_names = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
        _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

import random
def get_computer_choice():
    return random.randint(0, 2)

def user_wins(user_choice, computer_choice):
    return (user_choice == ROCK and computer_choice == SCISSORS) \
    or (user_choice == PAPER and computer_choice == ROCK) \
    or (user_choice == SCISSORS and computer_choice == PAPER)

def game():
    print('--------------Rock Paper Scissors----------------------')
    print('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.')
    user_choice = int(input())

    if user_choice not in {0, 1, 2}:
        print('Invalid choice')
        return

    computer_choice = get_computer_choice()
    print('You chose: ' + choices_names[user_choice])
    print('Computer chose: ' + choices_names[computer_choice])

    
    if user_choice == computer_choice:
        print('It\'s a draw!')
        return
    if user_wins(user_choice, computer_choice):
        print('You win')
        return 
    print('You Lose')
    

def main():
    game()
main()
