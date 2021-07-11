import random

def guess():
    upper_limit = int(input('Define an upper limit: '))
    random_number = random.randint(1, upper_limit)
    guess = 0

    while (guess != random_number):
        guess = int(input(f'Guess a number between 1 and {upper_limit}: '))
        
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Congratulations. You have guessed the number {random_number}!!!')

def computer_guess():
    lower_limit = 1
    upper_limit = int(input('Define an upper limit: '))
    feedback = ''

    while (feedback != 'c'):
        guess = random.randint(lower_limit, upper_limit) if lower_limit != upper_limit else lower_limit

        feedback = input(f'Is {guess} too high (H), too low (L), or correct(C)? ').lower()

        if feedback == 'h':
            upper_limit = guess - 1
        elif feedback == 'l':
            lower_limit = guess + 1
        
    print(f'I have guessed the number {guess}')

def select_option():
    option = input('Please select option \nA. You guess number \nB. Computer guesses number \nEnter option: ').lower()
    if option == 'a':
        guess()
    elif option == 'b':
        computer_guess()

select_option()
