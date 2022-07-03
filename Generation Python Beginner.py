# Python is awesome
# for i in range(10):
#     print('Python is awesome!')

# Последовательность чисел 1
# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     print(i)

# Последовательность чисел 2
# m = int(input())
# n = int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)

# Последовательность чисел 3
# m = int(input())
# n = int(input())
# for i in range(m % 2 + m - 1, n - 1, -2):
#     print(i)

# Последовательность чисел 4
# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0:
#         print(i)
#     elif i % 10 == 9:
#         print(i)
#     elif i % 3 == 0 and i % 5 == 0:
#         print(i)

# Таблица умножения
# n = int(input())
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)

# Наибольшие числа
# На вход программе подается натуральное число n,
# а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и
# второе наибольшее число последовательности.
# n = int(input())
# mx = -1
# ms = -1
# for i in range(n):
#     x = int(input())
#     if x > mx:
#         ms = mx
#         mx = x
#     else:
#         if x > ms:
#             ms = x
# print(mx)
# print(ms)

# До КОНЦА 1
# text = input()
# while text != 'КОНЕЦ':
#     print(text)
#     text = input()

# До КОНЦА 2
# text = input()
# while text != 'КОНЕЦ' and text != 'конец':
#     print(text)
#     text = input()

# Количество членов
# text = input()
# s = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     s += 1
#     text = input()
# print(s)

# Пока делимся
# x = int(input())
# while x % 7 == 0:
#     print(x)
#     x = int(input())

# Сумма чисел
# x = int(input())
# s = 0
# while x >= 0:
#     s += x
#     x = int(input())
# print(s)

# Количество пятерок
# x = int(input())
# c = 0
# while 5 >= x >= 1:
#     if x == 5:
#         c += 1
#     x = int(input())
# print(c)

# Ведьмаку заплатите чеканной монетой
# x = int(input())
# c = 0
# while x >= 25:
#     c += 1
#     x -= 25
# while x >= 10:
#     c += 1
#     x -= 10
# while x >= 5:
#     c += 1
#     x -= 5
# while x >= 1:
#     c += 1
#     x -= 1
# print(c)

# Обратный порядок
# n = int(input())
# while n != 0:
#     print(n % 10)
#     n //= 10

# Обратный порядок 2
# n = int(input())
# while n != 0:
#     print(n % 10, end='')
#     n //= 10

# max и min
# n = int(input())
# mx = -1
# mn = 10
# while n != 0:
#     if n % 10 > mx:
#         mx = n % 10
#     if n % 10 < mn:
#         mn = n % 10
#     n //= 10
# print('Максимальная цифра равна', mx)
# print('Минимальная цифра равна', mn)

# Все вместе
# n = int(input())
# nc = n
# s = 0
# c = 0
# p = 1
# ld = n % 10
# while n != 0:
#     s += n % 10
#     c += 1
#     p *= (n % 10)
#     n //= 10
# print(s)
# print(c)
# print(p)
# print(s / c)
# print(nc // (10 ** (c - 1)))
# print(ld + nc // (10 ** (c - 1)))

# Вторая цифра
# n = int(input())
# nc = n
# c = 0
# while n != 0:
#     c += 1
#     n //= 10
# print((nc // (10 ** (c - 2))) % 10)

# Одинаковые цифры
# n = int(input())
# c1 = 0
# c2 = 0
# ld = n % 10
# while n != 0:
#     c1 += 1
#     if n % 10 == ld:
#         c2 += 1
#     n //= 10
# if c1 == c2:
#     print('YES')
# else:
#     print('NO')

# Упорядоченные цифры
# n = int(input())
# c1 = 0
# c2 = 0
# while n != 0:
#     c1 += 1
#     if n % 10 <= n // 10 % 10:
#         c2 += 1
#     n //= 10
#
# if c1 == c2 + 1:
#     print('YES')
# else:
#     print('NO')

# Наименьший делитель
# n = int(input())
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break

# Следуй правилам
# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9:
#         continue
#     elif 17 <= i <= 37:
#         continue
#     elif 78 <= i <= 87:
#         continue
#     else:
#         print(i)

# Таблица-1
# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()

# Таблица-2
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# Таблица-3
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()

# Звездный треугольник
# n = int(input())
# for i in range(n // 2 + 1):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# for i in range(n):
#     j = i
#     while j < n // 2:
#         j += 1
#         print('*', end='')
#     print()

# Численный треугольник 1
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()

# Уравнение
# total = 0
# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print('Общее количество натуральных решений =', total)

# Старинная задача
# 10x + 5y + 0.5z = 100
# total = 0
# for n in range(1, 11):
#     for k in range(1, 21):
#         for m in range(1, 201):
#             if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
#                 total += 1
#                 print('бык =', n, 'корова =', k, 'теленок =', m)
# print('Общее количество натуральных решений =', total)

# Гипотеза Эйлера о сумме степеней
# for a in range(1, 151):
#     for b in range(1, 151):
#         for c in range(1, 151):
#             for d in range(1, 151):
#                 for e in range(1, 151):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print(a + b + c + d + e)

# Численный треугольник 3
# n = int(input())
# tmp = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(tmp, end=' ')
#         tmp += 1
#     print()

# Делители-2
# n = int(input())
# for i in range(1, n + 1):
#     print(i, end='')
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print('+', end='')
#     print()

# Сумма факториалов
# from math import *
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += factorial(i)
# print(s)

# n = int(input())
# s = 0
# p = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         p *= j
#         print(p)
#     s += p
# print(s)

#
# n = int(input()) # приведение к int
# s = 0
# while n > 0:# был > нужен >=
#     if (n % 10) % 2 == 0:# если число четное
#         s += n % 10# сумма последней цифры и s
#     n //= 10
# print(s)

#
# n = 4
# count = 0
# maximum = -1 * (10 ** 8) - 1# для корректного сравнения нужно число -100 000 001
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
#             #break # break тут не нужен
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# Звездная рамка
# n = int(input())
# s = '*'
# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print(s * 19)
#     else:
#         print(s, ' ' * 17, s, sep='')

# Третья цифра
# n = int(input())
# while n > 999:
#     n //= 10
# print(n % 10)

# Все вместе 2
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
# n = int(input())
# c3 = 0
# cld = 0
# cev = 0
# s5 = 0
# p7 = 1
# c05 = 0
# ld = n % 10
# while n != 0:
#     if n % 10 == 3:
#         c3 += 1
#     if n % 10 == ld:
#         cld += 1
#     if n % 10 % 2 == 0:
#         cev += 1
#     if n % 10 > 5:
#         s5 += n % 10
#     if n % 10 > 7:
#         p7 *= n % 10
#     if n % 10 == 0 or n % 10 == 5:
#         c05 += 1
#     n //= 10
# print(c3)
# print(cld)
# print(cev)
# print(s5)
# print(p7)
# print(c05)

# Числа Рамануджана
# Цифра .... = 2^3 + 16.0^3 = 9^3 + 15.0^3
# Цифра .... = 2^3 + 24.0^3 = 18^3 + 20.0^3
# Цифра .... = 10^3 + 27.0^3 = 19^3 + 24.0^3
# Цифра .... = 4^3 + 32.0^3 = 18^3 + 30.0^3
# print(2 ** 3 + 16 ** 3)
# print(2 ** 3 + 24 ** 3)
# print(10 ** 3 + 27 ** 3)
# print(4 ** 3 + 32 ** 3)

# Самый частотный символ
# s = input()
# mx = -1
# ch = ''
# for i in range(len(s)):
#     if s.count(s[i]) >= mx:
#         mx = s.count(s[i])
#         ch = s[i]
# print(ch)

# Первое и последнее вхождение
# s = input()
# if s.count('f') > 0:
#     if s.count('f') == 1:
#         print(s.find('f'))
#     else:
#         print(s.find('f'), end=' ')
#         print(s.rfind('f'))
# else:
#     print('NO')

# Удаление фрагмента
# s = input()
# print(s[:s.find('h')], s[s.rfind('h') + 1:], sep='')

# format
# s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(2010, '10k', 'Bitcoin ')
# print(s)

# Символы в диапазоне
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# Простой шифр
# s = input()
# for i in range(len(s)):
#     print(ord(s[i]), end=" ")

# Шифр Цезаря
# k = int(input())
# n = 26
# s = input()
# x = -1000
# for i in range(len(s)):
#     x = ((ord(s[i]) - 97) - k) % n
#     if x < 0:
#         print(chr(n - x + 97), end='')
#     else:
#         print(chr(x + 97),end='')

# Каждый третий
# s = input()
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end='')

# Замени меня полностью
# s = input()
# print(s.replace('1', 'one'))

# Удали меня полностью
# s = input()
# print(s.replace('@', ''))

# Второе вхождение
# s = input()
# c = s.count('f')
# f = s.find('f')
# if c > 0:
#     if c == 1:
#         print(-1)
#     else:
#         for i in range(len(s)):
#             if s[i] == 'f' and i > f:
#                 print(i)
#                 break
# else:
#     print(-2)

# Переворот
# s = input()
# f = s.find('h')
# sc = s.rfind('h')
# print(s[:f + 1], s[sc - 1: f: -1], s[sc:], sep='')

# Список чисел
# print(list(range(1, int(input()) + 1)))

# Список букв
# n = int(input())
# ls = []
# for i in range(97, n + 97):
#     ls += chr(i)
# print(ls)

# Список строк
# n = int(input())
# ls = []
# for i in range(n):
#     ls.append(input())
# print(ls)

# Алфавит
# ls = []
# for i in range(0, 26):
#     ls.append(chr(i + 97) * (i + 1))
# print(ls)

# Список кубов
# n = int(input())
# ls = []
# for i in range(n):
#     x = int(input())
#     ls.append(x ** 3)
# print(ls)

# Список делителей
# n = int(input())
# ls = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         ls.append(i)
# print(ls)

# Суммы двух
# n = int(input())
# ls = []
# f = int(input())
# s = 0
# for i in range(n - 1):
#     x = int(input())
#     s = f + x
#     ls.append(s)
#     f = x
# print(ls)

# Удалите нечетные индексы
# n = int(input())
# ls = []
# for i in range(n):
#     ls.append(int(input()))
# del ls[1::2]
# print(ls)

# k-ая буква слова
# n = int(input())
# ls = []
# for i in range(n):
#     ls.append(input())
# k = int(input())
# for j in range(len(ls)):
#     if len(ls[j]) >= k:
#         s = ls[j]
#         print(s[k - 1], end='')

# Символы всех строк
# n = int(input())
# ls = []
# for i in range(n):
#     ls.extend(input())
# print(ls)

# Remove outliers
# n = int(input())
# ls = []
# res = []
# for i in range(n):
#     ls.append(int(input()))
# mx = max(ls)
# mn = min(ls)
# for j in range(n):
#     if ls[j] != mn and ls[j] != mx:
#         res.append(ls[j])
# print(*res, sep='\n')

# Google search - 2
# n = int(input())
# ls = []
# for i in range(n):
#     ls.append(input())
# k = int(input())
# lsk = []
# for j in range(k):
#     lsk.append(input())
# res = []
# c = 0
# for l in range(n):
#     for g in range(k):
#         if lsk[g].upper() in ls[l].upper():
#             c += 1
#     if c == k:
#         res.append(ls[l])
#     c = 0
# print(*res, sep='\n')

# Negatives, Zeros and Positives
# n = int(input())
# lsn = []
# lsz = []
# lsp = []
# for i in range(n):
#     x = int(input())
#     if x > 0:
#         lsp.append(x)
#     elif x < 0:
#         lsn.append(x)
#     else:
#         lsz.append(x)
# print(*(lsn + lsz + lsp), sep='\n')

# Построчный вывод
# s = input()
# ls = s.split()
# print(*ls, sep='\n')

# Инициалы
# s = input()
# ls = s.split()
# print(ls[0][0], ls[1][0], ls[2][0], sep='.', end='.')

# Windows OS
# s = input()
# print(*(s.split('\\')), sep='\n')

# Диаграмма
# ls = input().split()
# for i in range(len(ls)):
#     ls[i] = int(ls[i])
#     for j in range(ls[i]):
#         print('+', end='')
#     print()

# Корректный ip-адрес
# ls = input().split('.')
# c = 0
# for i in range(len(ls)):
#     ls[i] = int(ls[i])
#     if 0 <= ls[i] <= 255:
#         c += 1
# if c == 4:
#     print('ДА')
# else:
#     print('НЕТ')

# Добавь разделитель
# ls = []
# ls.extend(input())
# n = input()
# print(n.join(ls))

# Количество совпадающих пар
# ls = input().split()
# c = 0
# for i in range(len(ls)):
#     ls[i] = int(ls[i])
# for i in range(len(ls)):
#     for j in range(i + 1, len(ls)):
#         if ls[i] == ls[j]:
#             c += 1
# print(c)

# Тимур и его числа
# from math import *
# print(ceil(log(int(input()), 2)))
