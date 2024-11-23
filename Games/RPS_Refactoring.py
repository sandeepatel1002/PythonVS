import random

choices = ('r','p','s')
emojis = {'r':'🪨','p':'📃','s':'✂️'}

def get_user_choice():
    while True:
        user_choice = input('Enter your choice...(r,p,s) ')

        if user_choice in choices:
            return user_choice
        else:
            print('please enter the valid choice...')

def print_choices(user_choice,computer_choice):
    print(f'user choice is {emojis[user_choice]}')
    print(f'computer choice is {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if computer_choice == user_choice:
        print('Tie')
    elif computer_choice == 'r' and user_choice == 'p':
        print('computer wins')
    elif computer_choice == 'p' and user_choice == 'r':
        print('computer wins')
    elif computer_choice == 's' and user_choice == 'p':
        print('computer wins')
    else:
        print('you wonn.')
 
def play_game():
    while True:
    
        computer_choice = random.choice(choices)

        user_choice = get_user_choice()

        print_choices(user_choice, computer_choice)

        determine_winner(user_choice,computer_choice)

        user_continue = input('do you want to play again.....(y/n)')
        if user_continue == 'n':
            break
   
play_game()