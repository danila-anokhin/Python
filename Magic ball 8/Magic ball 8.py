from random import *
from time import *


answers = [
    'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes — definitely',
    'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
    'Signs point to yes', 'Yes', 'Reply hazy, try again', 'Ask again later',
    'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don’t count on it',
    'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
]

again = 'y'
name = input('Enter your name: ')
print('Hello ', name, ', I am a magic ball and I know the answer to any of your questions.', sep='')

while again.lower() == 'y':
    input('Enter your question: ')
    print('Magic ball thinks', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    print(choice(answers))
    again = input('Would you like to ask another question? (y = yes, n = no): ')
    if again.lower() == 'y':
        continue
    else:
        again = 'n'
        print('Come back if you have any questions!')
