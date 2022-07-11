def is_valid_num(n, ln):
    if ln.lower() == 'en':
        if n.isdigit():
            n = int(n)
            if 1 <= n <= 25:
                return True
            else:
                return False
        else:
            return False
    else:
        if n.isdigit():
            n = int(n)
            if 1 <= n <= 32:
                return True
            else:
                return False
        else:
            return False


def is_valid_lang(ch):
    if ch.isalpha() and (ch.lower() == 'en' or ch.lower() == 'ru'):
        return True
    else:
        return False


def is_valid_dir(ch):
    if ch.isalpha() and (ch.lower() == 'enc' or ch.lower() == 'dec'):
        return True
    else:
        return False


def encrypt(text, key, lan):
    lowercase_letters_en = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    uppercase_letters_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ru = len(lowercase_letters_ru)
    en = len(lowercase_letters_en)
    if lan == 'ru':
            for i in range(len(text)):
                for j in range(ru):
                    if text[i] == uppercase_letters_ru[j]:
                        x = (j + key) % ru
                        text[i] = uppercase_letters_ru[x]
                        x = 0
                        break
                    if text[i] == lowercase_letters_ru[j]:
                        x = (j + key) % ru
                        text[i] = lowercase_letters_ru[x]
                        x = 0
                        break
    else:
        for i in range(len(text)):
            for j in range(en):
                if text[i] == uppercase_letters_en[j]:
                    x = (j + key) % en
                    text[i] = uppercase_letters_en[x]
                    x = 0
                    break
                if text[i] == lowercase_letters_en[j]:
                    x = (j + key) % en
                    text[i] = lowercase_letters_en[x]
                    x = 0
                    break
    return ''.join(text)


def decrypt(text, key, lan):
    lowercase_letters_en = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    uppercase_letters_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ru = len(lowercase_letters_ru)
    en = len(lowercase_letters_en)
    if lan == 'ru':
            for i in range(len(text)):
                for j in range(ru):
                    if text[i] == uppercase_letters_ru[j]:
                        x = (j - key) % ru
                        if x < 0:
                            text[i] = uppercase_letters_ru[ru + x]
                        else:
                            text[i] = uppercase_letters_ru[x]
                        x = 0
                        break
                    if text[i] == lowercase_letters_ru[j]:
                        x = (j - key) % ru
                        if x < 0:
                            text[i] = lowercase_letters_ru[ru + x]
                        else:
                            text[i] = lowercase_letters_ru[x]
                        x = 0
                        break
    else:
        for i in range(len(text)):
            for j in range(en):
                if text[i] == uppercase_letters_en[j]:
                    x = (j - key) % en
                    if x < 0:
                        text[i] = uppercase_letters_en[en + x]
                    else:
                        text[i] = uppercase_letters_en[x]
                    x = 0
                    break
                if text[i] == lowercase_letters_en[j]:
                    x = (j - key) % en
                    if x < 0:
                        text[i] = lowercase_letters_en[en + x]
                    else:
                        text[i] = lowercase_letters_en[x]
                    x = 0
                    break
    return ''.join(text)


print('Do you want to encrypt the test or decrypt? (enc = encrypt, dec = decrypt)')
while True:
    dirt = input()
    if is_valid_dir(dirt):
        break
    else:
        print('Please enter (enc = encrypt, dec = decrypt)!!!')

print('Enter alphabet language (ru = russian, en = english)')
while True:
    lang = input()
    if is_valid_lang(lang):
        break
    else:
        print('Please enter (ru = russian, en = english)!!!')

print('Enter alphabet shift step:')
while True:
    k = input()
    if is_valid_num(k, lang):
        k = int(k)
        break
    else:
        if lang.lower() == 'ru':
            print('Enter the number 1 <= k <= 32!!!')
        else:
            print('Enter the number 1 <= k <= 25!!!')

txt = []
while True:
    txt.extend(input('Enter text: '))
    if len(txt) == 0:
        print('Enter any text!!!')
        continue
    else:
        break

if dirt == 'enc':
    print('Your ciphertext:', end=' ')
    print(encrypt(txt, k, lang))
else:
    print('Your decoded text:', end=' ')
    print(decrypt(txt, k, lang))
