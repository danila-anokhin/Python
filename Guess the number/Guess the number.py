from random import *

def is_valid(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 100:
            return True
        else:
            return False
    else:
        return False

print('Welcome to number guessing game!!!')

print('Enter right bound for random number selection: ', end='')

c = 0
again = 'y'
rb = int(input())
num = randint(1, rb)  # number to be guessed

while again.lower() == 'y':
    print('Enter a number from 1 to', rb, ': ', end='')
    c += 1
    n = input()
    if is_valid(n):
        n = int(n)
        if n < num:
            print('Your number is less than expected, please try again')
            continue
        elif n > num:
            print('Your number is higher than expected, please try again')
            continue
        else:
            print('You guessed the number on', c, 'attempts, congratulations!')
            again = input('Do you want to play again? (y = yes, n = no): ')
            if again.lower() == 'y':
                print('Enter right bound for random number selection: ', end='')
                rb = int(input())
                num = randint(1, rb)
                c = 0
                continue
            else:
                print('Thanks for playing the number guessing game. See you...')
                break
    else:
        print('Or maybe still enter an integer from 1 to ', rb, '?')
        continue






