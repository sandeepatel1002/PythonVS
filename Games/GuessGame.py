import random

name = input('Please enter your name..')
print(f'Hello Mr. {name}, Welcome to the guessing game..')
print('Guess the random number between 0 to 10')

while True:
    computer_guess = random.randint(1,11)
    user_guess = int(input('please enter a number '))
    counter = 1
    while user_guess != computer_guess:
        if user_guess<computer_guess:
            print('you guessed a smaller number')
        else:
            print('you guessed a bigger number')
        counter = counter+1
        user_guess = int(input('guess the number again..'))
    print('Congratulations!! you have guessed the right number, the number was ',user_guess)
    print('you have guessed the right answer in ',counter, ' attempts.')
    user_choice = input('do you want to play again..(Y/N)')
    if user_choice != 'Y':
        print('thanks for playing, goodbye..')
        break


