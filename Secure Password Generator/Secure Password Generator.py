from random import *

def generate_password(length, chars):
    res = []
    while len(res) != length:
        for i in range(len(chars)):
            res += choice(chars[i])
            if len(res) == length:
                break
    shuffle(res)
    return ''.join(res)

def is_valid_num(n):
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 100:
            return True
        else:
            return False
    else:
        return False

def is_valid_ch(ch):
    if ch.isalpha() and (ch.lower() == 'y' or ch.lower() == 'n'):
        return True
    else:
        return False

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exception = 'il1Lo0O'
chars = ''


print('How many passwords to generate?')
while True:
    n = input()
    if is_valid_num(n):
        n = int(n)
        break
    else:
        print('Enter the correct number of passwords (from 1 to 100)!!!')
        continue

print('What is the length of the password?')
while True:
    lgh = input()
    if is_valid_num(lgh):
        lgh = int(lgh)
        break
    else:
        print('Enter the correct password length (from 1 to 100)!!!')
        continue

while True:
    while True:
        ans = input('Should the numbers 0123456789 be included? (y = yes, n = no): ')
        if is_valid_ch(ans):
            if ans.lower() == 'y':
                chars += digits + ' '
            break
        else:
            print('Please enter (y=yes, n=no)!!!')
            continue

    while True:
        ans = input('Should uppercase ABCDEFGHIJKLMNOPQRSTUVWXYZ be included? (y = yes, n = no): ')
        if is_valid_ch(ans):
            if ans.lower() == 'y':
                chars += uppercase_letters + ' '
            break
        else:
            print('Please enter (y=yes, n=no)!!!')
            continue

    while True:
        ans = input('Should lowercase abcdefghijklmnopqrstuvwxyz be included? (y = yes, n = no): ')
        if is_valid_ch(ans):
            if ans.lower() == 'y':
                chars += lowercase_letters + ' '
            break
        else:
            print('Please enter (y=yes, n=no)!!!')
            continue

    while True:
        ans = input('Should the characters !#$%&*+-=?@^_ be included? (y = yes, n = no): ')
        if is_valid_ch(ans):
            if ans.lower() == 'y':
                chars += punctuation + ' '
            break
        else:
            print('Please enter (y=yes, n=no)!!!')
            continue

    while True:
        ans = input('Should il1Lo0O ambiguous characters be excluded? (y = yes, n = no): ')
        if is_valid_ch(ans):
            if ans.lower() == 'y':
                for i in range(len(exception)):
                    chars = chars.replace(exception[i], '')
            break
        else:
            print('Please enter (y=yes, n=no)!!!')
            continue

    if chars != '':
        break
    else:
        print('Choose at least one group to generate passwords!')
        continue

chars = chars.split()

for i in range(1, n + 1):
    print('Password №',  i, ': ', generate_password(lgh, chars), sep='')





