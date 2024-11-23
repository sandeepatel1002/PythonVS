import random

def user_choice(msg):
    x = input('enter you name....')
    return print(msg, x)

def computer_choice(msg):
    x = random.randint(1,5)
    return print(msg*x)

def play_game():

    msg = input('enter the msg...')
    user_choice(msg)
    computer_choice(msg)

play_game()