import random

while True:
    choices = ('r','p','s')
    emojis = {'r':'🪨','p':'📃','s':'✂️'}

    computer_choice = random.choice(choices)
    user_choice = input('Enter your choice...(r,p,s) ')

    if user_choice not in choices:
        print('please enter a valid choice')
        continue

    print(f'user choice is {emojis[user_choice]}')
    print(f'computer choice is {emojis[computer_choice]}')

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

    while True:
        user_continue = input('do you want to play again.....(y/n)')
        if user_continue not in ['y','n']:
            print('please enter the right choice..')
            continue
        else:
            break
    if user_continue == 'n':
        break

print('thanks for playing the game...')