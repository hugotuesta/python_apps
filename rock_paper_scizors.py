import random

def play():
    user = input('What is you choice? \n\'r\' for rock, \'p\' for paper and \'s\' for scizors\n').lower()
    computer = random.choice(['r', 'p', 's'])
    print(f'Computer chose {computer}\n')

    if user == computer:
        return 'It\'s a tie!'

    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

print(play())
