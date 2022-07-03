from random import *

def generate_password(length, chars):


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
c = 'il1Lo0O'
chars = ''

print('How many passwords to generate?')
n = int(input())
print('What is the length of the password?')
l = int(input())
while True:
    ans = input('Should the numbers 0123456789 be included? (y = yes, n = no): ')
    if ans.lower() == 'y':
        chars += digits
    ans = input('Should uppercase ABCDEFGHIJKLMNOPQRSTUVWXYZ be included? (y = yes, n = no): ')
    if ans.lower() == 'y':
        chars += uppercase_letters
    ans = input('Should lowercase abcdefghijklmnopqrstuvwxyz be included? (y = yes, n = no): ')
    if ans.lower() == 'y':
        chars += lowercase_letters
    ans = input('Should the characters !#$%&*+-=?@^_ be included? (y = yes, n = no): ')
    if ans.lower() == 'y':
        chars += punctuation
    ans = input('Should il1Lo0O ambiguous characters be excluded? (y = yes, n = no): ')
    if ans.lower() == 'y':
        chars = chars.replace('i', '')
        chars = chars.replace('l', '')
        chars = chars.replace('1', '')
        chars = chars.replace('L', '')
        chars = chars.replace('o', '')
        chars = chars.replace('0', '')
        chars = chars.replace('O', '')
    if chars != '':
        break






