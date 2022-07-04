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


# N - ый член арифметической прогрессии
# a = int(input())
# d = int(input())
# n = int(input())
# print(a + d * (n - 1))

# Последовательность чисел x, 2x, 3x, 4x, 5x разделённых тремя черточками
# x = int(input())
# print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')

# Геометрическая прогрессия
# b = int(input())
# q = int(input())
# n = int(input())
# print(b * q ** (n - 1))

# Расстояние в метрах
# x = int(input())
# print(x // 100)

# Мандарины
# x = int(input())
# y = int(input())
# print(y // x)
# print(y % x)

# Сама неотвратимость
# n = int(input())
# print((n // -2) * -1)

# Номер купе
# x = int(input())
# print(1 + (x - 1) // 4)

# Пересчет временного интервала
# x = int(input())
# print(x, 'мин', '-', 'это', x // 60, 'час', x % 60, 'минут.')

# Трехзначное число
# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# x = int(input())
# print('Сумма цифр =', x % 10 + x // 100 + x // 10 % 10)
# print('Произведение цифр =', (x % 10) * (x // 100) * (x // 10 % 10))

# Перестановка цифр
# a = int(input())
# b = a // 10 % 10
# c = a % 10
# a = a // 100
# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')

# Четырёхзначное число
# x = int(input())
# print('Цифра в позиции тысяч равна', x // 1000)
# print('Цифра в позиции сотен равна', x // 100 % 10)
# print('Цифра в позиции десятков равна', x // 10 % 10)
# print('Цифра в позиции единиц равна', x % 10)

# Пароль
# x = input()
# y = input()
# if x == y:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# Четное или нечетное?
# x = int(input())
# if x % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# Соотношение
# x = int(input())
# sum = x // 1000 + x % 10
# dif = x // 100 % 10 - x // 10 % 10
# if sum == dif:
#     print('ДА')
# else:
#     print('НЕТ')

# Роскомнадзор
# x = int(input())
# if x >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

# Арифметическая прогрессия
# x = int(input())
# y = int(input())
# z = int(input())
# if y - x == z - y:
#     print('YES')
# else:
#     print('NO')

# Наименьшее из двух чисел
# x = int(input())
# y = int(input())
# if x - y < 0:
#     print(x)
# else:
#     print(y)

# Наименьшее из четырёх чисел
# x = int(input())
# y = int(input())
# z = int(input())
# v = int(input())
# if x > y:
#     x = y
# if z > v:
#     z = v
# if x < z:
#     print(x)
# else:
#     print(z)

# Возрастная группа
# x = int(input())
# if x <= 13:
#     print('детство')
# else:
#     if 14 <= x <= 24:
#         print('молодость')
#     else:
#         if 25 <= x <= 59:
#             print('зрелость')
#         else:
#             print('старость')

# Только +
# x = int(input())
# y = int(input())
# z = int(input())
# s = 0
# if x > 0:
#     s = s + x
# if y > 0:
#     s = s + y
# if z > 0:
#     s = s + z
# print(s)

# Принадлежность 1
# x = int(input())
# if -1 < x < 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# Принадлежность 2
# x = int(input())
# if -3 >= x or x >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# Принадлежность 3
# x = int(input())
# if -30 < x <= 2 or 7 < x <= 25:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# Красивое число
# x = int(input())
# if 1 <= x // 1000 < 10 and (x % 7 == 0 or x % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# Неравенство треугольника
# x = int(input())
# y = int(input())
# z = int(input())
# if x < y + z and y < x + z and z < x + y:
#     print('YES')
# else:
#     print('NO')

# Високосный год
# x = int(input())
# if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# Ход ладьи
# x = int(input())
# y = int(input())
# z = int(input())
# v = int(input())
# if x == z or y == v:
#     print('YES')
# else:
#     print('NO')

# Ход короля m
# x = int(input())
# y = int(input())
# z = int(input())
# v = int(input())
# if (z - 1 <= x <= z + 1) and (v - 1 <= y <= v + 1):
#     print('YES')
# else:
#     print('NO')

# Гонка спидстеров
# n = int(input())
# k = int(input())
# if n > k:
#     print('NO')
# elif k > n:
#     print('YES')
# else:
#     print("Don't know")

# Вид треугольника
# x = int(input())
# y = int(input())
# z = int(input())
# if x != y and x != z and y != z:
#     print('Разносторонний')
# elif (x == y and x != z and y != z) or (z == y and z != x and y != x) or (z == x and z != y and z != y):
#     print('Равнобедренный')
# else:
#     print('Равносторонний')

# Среднее число
# x = int(input())
# y = int(input())
# z = int(input())
# if y < x < z or z < x < y:
#     print(x)
# elif x < y < z or z < y < x:
#     print(y)
# else:
#     print(z)

# Количество дней
# x = int(input())
# if x == 2:
#     print(28)
# elif (x % 2 == 0 and x < 7) or (x % 2 != 0 and x > 8):
#     print(30)
# else:
#     print(31)

# Церемония взвешивания
# x = int(input())
# if 0 <= x < 60:
#     print('Легкий вес')
# elif 60 <= x < 64:
#     print('Первый полусредний вес')
# else:
#     print('Полусредний вес')

# Самописный калькулятор
# a = int(input())
# b = int(input())
# x = input()
# if x == '+':
#     print(a + b)
# elif x == '-':
#     print(a - b)
# elif x == '*':
#     print(a * b)
# elif x == '/':
#     if b != 0:
#         print(a / b)
#     else:
#         print('На ноль делить нельзя!')
# else:
#     print('Неверная операция')

# Цветовой микшер
# a = input()
# b = input()
# if a == 'красный':
#     if b == 'красный':
#         print('красный')
#     elif b == 'синий':
#         print('фиолетовый')
#     elif b == 'желтый':
#         print('оранжевый')
#     else:
#         print('ошибка цвета')
# elif a == 'желтый':
#     if b == 'желтый':
#         print('желтый')
#     elif b == 'синий':
#         print('зеленый')
#     elif b == 'красный':
#         print('оранжевый')
#     else:
#         print('ошибка цвета')
# elif a == 'синий':
#     if b == 'синий':
#         print('синий')
#     elif b == 'желтый':
#         print('зеленый')
#     elif b == 'красный':
#         print('фиолетовый')
#     else:
#         print('ошибка цвета')
# else:
#     print('ошибка цвета')

# Цвета колеса рулетки
# x = int(input())
# if x == 0:
#     print('зеленый')
# elif 1 <= x <= 10:
#     if x % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 11 <= x <= 18:
#     if x % 2 == 0:
#         print('красный')
#     else:
#         print('черный ')
# elif 19 <= x <= 28:
#     if x % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 29 <= x <= 36:
#     if x % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# else:
#     print('ошибка ввода')

# Пересечение отрезков
# a = int(input())
# b = int(input())
# x = int(input())
# y = int(input())
# ma = max(a, x)
# mb = min(b, y)
# if ma == mb:
#     print(ma)
# elif mb > ma:
#     print(ma, mb)
# else:
#     print('пустое множество')

# Начало столетия
# x = int(input())
# if x % 100 == 0:
#     print('YES')
# else:
#     print('NO')

# Шахматная доска
# a = int(input())
# b = int(input())
# x = int(input())
# y = int(input())
# if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
#     if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
#         print('YES')
#     else:
#         print('NO')
# elif (a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2 != 0):
#     if (x % 2 != 0 and y % 2 == 0) or (x % 2 == 0 and y % 2 != 0):
#         print('YES')
#     else:
#         print('NO')

# Girls only
# x = int(input())
# y = input()
# if 10 <= x <= 15 and y == 'f':
#     print('YES')
# else:
#     print('NO')

# Римские цифры
# x = int(input())
# if 1 <= x <= 10:
#     if x == 1:
#         print('I')
#     elif x == 2:
#         print('II')
#     elif x == 3:
#         print('III')
#     elif x == 4:
#         print('IV')
#     elif x == 5:
#         print('V')
#     elif x == 6:
#         print('VI')
#     elif x == 7:
#         print('VII')
#     elif x == 8:
#         print('VIII')
#     elif x == 9:
#         print('IX')
#     elif x == 10:
#         print('X')
# else:
#     print('ошибка')

# YES or NO вот в чем вопрос
# x = int(input())
# if x % 2 != 0:
#     print('YES')
# else:
#     if 2 <= x <= 5:
#         print('NO')
#     elif 6 <= x <= 20:
#         print('YES')
#     elif x > 20:
#         print('NO')

# Ход слона
# a = int(input())
# b = int(input())
# x = int(input())
# y = int(input())
# if abs(a - x) == abs(b - y):
#     print('YES')
# else:
#     print('NO')

# Ход коня
# a = int(input())
# b = int(input())
# x = int(input())
# y = int(input())
# if abs(a - x) == 1 and abs(b - y) == 2:
#     print('YES')
# elif abs(a - x) == 2 and abs(b - y) == 1:
#     print('YES')
# else:
#     print('NO')

# Ход ферзя
# a = int(input())
# b = int(input())
# x = int(input())
# y = int(input())
# if abs(a - x) == abs(b - y):
#     print('YES')
# elif a == x or b == y:
#     print('YES')
# else:
#     print('NO')

# Площадь треугольника
# a = float(input())
# b = float(input())
# print(0.5 * a * b)

# Две старушки
# s = float(input())
# v1 = float(input())
# v2 = float(input())
# print(s / (v1 + v2))

# Обратное число
# x = float(input())
# if x == 0:
#     print('Обратного числа не существует')
# else:
#     print(x ** -1)

# 451 градус по Фаренгейту
# x = float(input())
# print(5 / 9 * (x - 32))

# Dog age
# x = int(input())
# if x - 2 > 0:
#     print(2 * 10.5 + (x - 2) * 4)
# else:
#     print(x * 10.5)

# Первая цифра после точки
# x = float(input())
# x = int(x * 10)
# print(x % 10)

# Дробная часть
# x = float(input())
# print(x - int(x))

# Наибольшее и наименьшее
# x1 = int(input())
# x2 = int(input())
# x3 = int(input())
# x4 = int(input())
# x5 = int(input())
# print('Наименьшее число =', min(x1, x2, x3, x4, x5))
# print('Наибольшее число =', max(x1, x2, x3, x4, x5))

# Сортировка трёх
# x1 = int(input())
# x2 = int(input())
# x3 = int(input())
# print(max(x1, x2, x3))
# print((x1 + x2 + x3) - min(x1, x2, x3) - max(x1, x2, x3))
# print(min(x1, x2, x3))

# Интересное число
# x = int(input())
# x1 = x // 100
# x2 = x // 10 % 10
# x3 = x % 10
# mx = max(x1, x2, x3)
# mn = min(x1, x2, x3)
# avg = x1 + x2 + x3 - mx - mn
# if mx - mn == avg:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# Абсолютная сумма
# a1 = abs(float(input()))
# a2 = abs(float(input()))
# a3 = abs(float(input()))
# a4 = abs(float(input()))
# a5 = abs(float(input()))
# print(a1 + a2 + a3 + a4 + a5)

# Манхэттенское расстояние
# x1 = int(input())
# x2 = int(input())
# x3 = int(input())
# x4 = int(input())
# print(abs(x1 - x3) + abs(x2 - x4))

# What's Your Name?
# s1 = input()
# s2 = input()
# print('Hello ' + s1, s2 + '! You just delved into Python')

# Футбольная команда
# s = input()
# print('Футбольная команда ' + s, 'имеет длину', len(s), 'символов')

# Три города
# x1 = input()
# x2 = input()
# x3 = input()
# mx = max(len(x1), len(x2), len(x3))
# mn = min(len(x1), len(x2), len(x3))
# if len(x1) == mn:
#     print(x1)
# elif len(x2) == mn:
#     print(x2)
# else:
#     print(x3)
# if len(x1) == mx:
#     print(x1)
# elif len(x2) == mx:
#     print(x2)
# else:
#     print(x3)

# Арифметические строки
# x1 = len(input())
# x2 = len(input())
# x3 = len(input())
# if (2 * x1 - x2 - x3) * (2 * x2 - x1 - x3) * (2 * x3 - x1 - x2) == 0:
#     print('YES')
# else:
#     print('NO')

# Цвет настроения синий
# s = input()
# if 'синий' in s:
#     print('YES')
# else:
#     print('NO')

# Отдыхаем ли?
# s = input()
# if 'суббота' in s or 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')

# Корректный email
# s = input()
# if '@' in s and '.' in s:
#     print('YES')
# else:
#     print('NO')

#Евклидово расстояние
# from math import *
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# print(sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2)))

# Площадь и длина
# from math import *
# r = float(input())
# print(pi * r * r)
# print(pi * r * 2)

# Средние значения
# from math import *
# a = float(input())
# b = float(input())
# print((a + b) / 2) # среднее арифметическое
# print(sqrt(a * b)) # среднее геометрическое
# print((2 * a * b) / (a + b)) # среднее гармоническое
# print(sqrt((a * a + b * b) / 2)) # среднее квадратичное

# Тригонометрическое выражение
# from math import *
# x = float(input())
# xr = radians(x)
# print(sin(xr) + cos(xr) + pow(tan(xr), 2))

# Пол и потолок
# from math import *
# x = float(input())
# print(ceil(x) + floor(x))

# Квадратное уравнение
# from math import *
# a = float(input())
# b = float(input())
# c = float(input())
# d = b * b - 4 * a * c
# if d > 0:
#     x1 = (-1 * b - sqrt(d)) / (2 * a)
#     x2 = (-1 * b + sqrt(d)) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))
# elif d == 0:
#     print((-1 * b) / (2 * a))
# else:
#     print('Нет корней')

# Правильный многоугольник
# from math import *
# n = int(input())
# a = float(input())
# s = (n * a * a) / (4 * tan(pi / n))
# print(s)

# Квадрат числа
# n = int(input())
# for i in range(n + 1):
#     print('Квадрат числа', i, 'равен', i * i)

# Звездный треугольник
# n = int(input())
# s = '*'
# for i in range(n):
#     print(s * abs(n - i))

# Популяция
# m = int(input())
# p = int(input())
# n = int(input())
# x = m
# print(1, m)
# for i in range(n - 1):
#     x = x + x * (p / 100)
#     print(i + 2, x)

# Количество чисел
# a = int(input())
# b = int(input())
# cnt = 0
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         cnt += 1
# print(cnt)

# Сумма чисел
# n = int(input())
# s = 0
# for i in range (n):
#     x = int(input())
#     s += x
# print(s)

# Асимптотическое приближение
# from math import *
# n = int(input())
# s = 1
# for i in range(2, n + 1):
#     s += 1 / i
# print(s - log(n))

# Сумма чисел 2
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     if i * i % 10 == 2 or i * i % 10 == 5 or i * i % 10 == 8:
#         s += i
# print(s)

# Факториал
# n = int(input())
# mpn = 1
# for i in range(1, n + 1):
#     mpn *= i
# print(mpn)

# Без нулей
# mpn = 1
# for i in range(10):
#     x = int(input())
#     if x != 0:
#         mpn *= x
# print(mpn)

# Сумма делителей
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         s += i
# print(s)

# Знакочередующаяся сумма
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += i * pow(-1, i + 1)
# print(s)

# Наибольшие числа
# n = int(input())
# mx = -1
# for i in range(n):
#     x = int(input())
#     if x > mx:
#         mx = x
# print(mx)

# Only even numbers
# c = 0
# for i in range(10):
#     x = int(input())
#     if x % 2 == 0:
#         c += 1
# if c == 10:
#     print('YES')
# else:
#     print('NO')

# Последовательность Фибоначчи
# n = int(input())
# f1 = 0
# f2 = 1
# for i in range(1, n + 1):
#     print(f2, end=' ')
#     f1, f2 = f2, f1 + f2

# Численный треугольник 4
# n = int(input())
# for j in range(1, n + 1):
#     for i in range(1, j * 2):
#         if i <= j:
#             print(i, end='')
#         else:
#             print(2 * j - i, end='')
#     print()

# Делители-1
# a = int(input())
# b = int(input())
# s = 0
# mx = -1
# mxd = -1
# for i in range(a, b + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             s += j
#     if s >= mx:
#         mx = s
#         if i > mxd:
#             mxd = i
#     s = 0
# print(mxd, mx)

# Цифровой корень
# n = int(input())
# while n > 9:
#     s = 0
#     while n > 0:
#         ld = n % 10
#         s += ld
#         n //= 10
#     else:
#         n = s
# else:
#     print(n)

# Простые числа
# a = int(input())
# b = int(input())
# c = 0
# for i in range(a, b + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             c += 1
#     if c <= 2:
#         if i != 1:
#             print(i)
#     c = 0

# В столбик 1
# s = input()
# for i in range(0, len(s), 2):
#     print(s[i])

# В столбик 2
# s = input()
# for i in range((len(s) - 1), -1, -1):
#     print(s[i])

# ФИО
# fn = input()
# ln = input()
# mn = input()
# print(ln[0], fn[0], mn[0], sep='')

# Цифра 1
# s = input()
# sm = 0
# for i in range(len(s)):
#     sm += int(s[i])
# print(sm)

# Цифра 2
# s = input()
# for i in range(10):
#     if str(i) in s:
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')

# Сколько раз?
# s = input()
# c1 = 0
# c2 = 0
# for i in range(len(s)):
#     if s[i] == '*':
#         c1 += 1
#     if s[i] == '+':
#         c2 += 1
# print('Символ + встречается', c2, 'раз')
# print('Символ * встречается', c1, 'раз')

# Одинаковые соседи
# s = input()
# c = 0
# for i in range(len(s) - 1):
#     if s[i] == s[i + 1]:
#         c += 1
# print(c)

# Гласные и согласные
# s = input()
# sg = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
# ss = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
# cg = 0
# cs = 0
# for i in range(len(s)):
#     for j in range(len(sg)):
#         if s[i] == sg[j]:
#             cg += 1
#     for k in range(len(ss)):
#         if s[i] == ss[k]:
#             cs += 1
# print('Количество гласных букв равно', cg)
# print('Количество согласных букв равно', cs)

# Decimal to Binary
# n = int(input())
# s = ''
# while n != 0:
#     s += str(n % 2)
#     n //= 2
# # for i in range(len(s) - 1, -1, -1):
# #     print(s[i], end='')
# print(s[::-1])

# Палиндром
# s = input()
# if s == s[::-1]:
#     print('YES')
# else:
#     print('NO')

# Делаем срезы 1
# s = input()
# print(len(s))
# print(s * 3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])

# Делаем срезы 2
# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-1::-2])

# Две половинки
# from math import *
# s = input()
# if len(s) % 2 == 0:
#     print(s[int(len(s) / 2):], s[:int(len(s) / 2)], sep='')
# else:
#     print(s[ceil(len(s) / 2):], s[:floor(len(s) / 2) + 1], sep='')

# Заглавные буквы
# s = input()
# if s == s.title():
#     print('YES')
# else:
#     print('NO')

# sWAP cASE
# print(input().swapcase())

# Хороший оттенок
# s = input().upper()
# if 'ХОРОШ' in s:
#     print('YES')
# else:
#     print('NO')

# Нижний регистр
# s = input()
# a = 'abcdefghijklmnopqrstuvwxyz'
# c = 0
# for i in range(len(s)):
#     for j in range(len(a)):
#         if s[i] == a[j]:
#             c += 1
# print(c)

# s = input()
# s1 = s.upper()
# c = 0
# for i in range(len(s)):
#     if s[i] != s1[i]:
#         c += 1
# print(c)

# Количество слов
# s = input()
# print(s.count(' ') + 1)

# Минутка генетики
# s = input()
# print('Аденин:', s.count('а') + s.count('А'))
# print('Гуанин:', s.count('г') + s.count('Г'))
# print('Цитозин:', s.count('ц') + s.count('Ц'))
# print('Тимин:', s.count('т') + s.count('Т'))

# Очень странные дела
# n = int(input())
# c = 0
# for i in range(n):
#     s = input()
#     if s.count('11') >= 3:
#         c += 1
# print(c)

# Количество цифр
# s = input()
# c = 0
# for j in range(10):
#     c += s.count(str(j))
# print(c)

# .com or .ru
# s = input()
# if s.endswith('.com') or s.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')

# Значение функции
# n = int(input())
# ls = []
# res = []
# for i in range(n):
#     ls.append(int(input()))
#     res.append(ls[i] ** 2 + 2 * ls[i] + 1)
# print(*ls, sep='\n')
# print()
# print(*res, sep='\n')

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

# Без дубликатов
# n = int(input())
# ls = []
# for i in range(n):
#     x = input()
#     if x not in ls:
#         ls.append(x)
# print(*ls, sep='\n')

# Google search - 1
# n = int(input())
# ls = []
# for i in range(n):
#     ls.append(input())
# x = input()
# for i in range(n):
#     if x.upper() in ls[i].upper():
#         print(ls[i])

# Google search - 2
# n = int(input())
# ls = []
# for i in range(n):
#     ls.append(input())
# k = int(input())
# for
# for i in range(n):
#     if x.upper() in ls[i].upper():
#         print(ls[i])

# Все сразу 2
# numbers = [8, 9, 10, 11]
# numbers.pop(1)
# numbers.insert(1, 17)
# numbers.extend([4, 5, 6])
# numbers.remove(8)
# n_c = numbers.copy()
# numbers.extend(n_c)
# numbers.insert(3, 25)
# print(numbers)

# Переставить min и max
# ls = input().split()
# for i in range(len(ls)):
#     ls[i] = int(ls[i])
# mx = max(ls)
# mn = min(ls)
# mxi = ls.index(mx)
# mni = ls.index(mn)
# if mxi > mni:
#     ls.remove(mx)
#     ls.insert(mxi, mn)
#     ls.remove(mn)
#     ls.insert(mni, mx)
# else:
#     ls.remove(mn)
#     ls.insert(mni, mx)
#     ls.remove(mx)
#     ls.insert(mxi, mn)
# for i in range(len(ls)):
#     ls[i] = str(ls[i])
# print(' '.join(ls))

# Количество артиклей
# ls = input().split()
# c = 0
# for i in range(len(ls)):
#     if ls[i] == 'a' or ls[i] == 'an' or ls[i] == 'the' or ls[i] == 'A' or ls[i] == 'An' or ls[i] == 'The':
#         c += 1
# print('Общее количество артиклей:', c)

# Взлом Братства Стали
# s = input()
# s = s[1:]
# n = int(s)
# ls = []
# res = []
# for i in range(n):
#     ls.append(input())
#     for j in range(len(ls[i])):
#         if ls[i][j] == '#':
#             res.append(ls[i][:ls[i].index('#')].rstrip())
#             break
#     else:
#         res.append(ls[i])
# print(*res, sep='\n')

# Сортировка чисел
# ls = input().split()
# for i in range(len(ls)):
#     ls[i] = int(ls[i])
# ls.sort()
# print(*ls)
# ls.sort(reverse=True)
# print(*ls)

# Удаление 1-х символов
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [keywords[i][1:] for i in range(len(keywords))]
# print(new_keywords)

# Длины строк
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(keywords[i]) for i in range(len(keywords))]
# print(lengths)

# Длина >= 5 символов
# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [keywords[i] for i in range(len(keywords)) if len(keywords[i]) >= 5]
# print(new_keywords)

# Палиндром
# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
# print(palindromes)

# Списочное выражение 1
# ls = [i ** 2 for i in range(1, int(input()) + 1)]
# print(*ls, sep='\n')

# Списочное выражение 2
# ls = input().split()
# ls = [int(ls[i]) ** 3 for i in range(len(ls))]
# print(*ls)

# В одну строку 1
# print(*input().split(), sep='\n')

# В одну строку 2
# print(*[i for i in input() if '0' <= i <= '9'] , sep='')

# В одну строку 3
# print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])

# Сортировка Пузырьком по возрастанию (оптимизированная)
# ls = input().split()
# n = len(ls)
# f = True
# for i in range(n):
#     ls[i] = int(ls[i])
# for i in range(n - 1):
#     f = False
#     for j in range(n - i - 1):
#         if ls[j] > ls[j + 1]:
#             ls[j], ls[j + 1] = ls[j + 1], ls[j]
#             f = True
#     if not f:
#         break
# print(*ls)

# Сортировка Выбором по возрастанию
# ls = input().split()
# n = len(ls)
# for i in range(n):
#     ls[i] = int(ls[i])
# for i in range(n - 1):
#     mxi = i
#     for j in range(i + 1, n):
#         if ls[j] > ls[mxi]:
#             mxi = j
#     if mxi != i:
#         ls[i], ls[mxi] = ls[mxi], ls[i]
# print(*ls)

# Список четных
# print([i for i in range(2, int(input()) + 1, 2)])

# Сумма двух списков
# ls1 = input().split()
# ls2 = input().split()
# res = []
# n = len(ls1)
# for i in range(n):
#     ls1[i] = int(ls1[i])
#     ls2[i] = int(ls2[i])
#     res.append(ls1[i] + ls2[i])
# print(*res)

# Сумма чисел
# ls = input().split()
# for i in range(len(ls)):
#     ls[i] = int(ls[i])
# print(*ls, sep='+', end='=')
# print(sum(ls))

# Самый длинный
# print(max([len(i) for i in input().split()]))

# Молодежный жаргон
# print(*[i[1:] + i[0] + 'ки' for i in input().split()])

# Валидный номер
# s = input()
# d = s.replace('-', '')
# ls1 = []
# if d.isdigit():
#     ls = s.split('-')
#     for i in range(len(ls)):
#         ls1.append(len(ls[i]))
#     if (ls1 == [1, 3, 3, 4] and ls[0] == '7') or (ls1 == [3, 3, 4]):
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# Звездный прямоугольник 1
# def draw_box():
#     z = '*'
#     n = 10 # ширина прямоугольника
#     h = 14 # высота прямоугольника
#     print(z * n)
#     for i in range(h - 2):
#         print(z,' ' * (n - 2), z, sep='')
#     print(z * n)
#
# draw_box()

# Звездный треугольник 1
# def drow_triangle():
#     z = '*'
#     n = 10
#     for i in range(1, n + 1):
#         print(z * i)
#
# drow_triangle()

# Звездный треугольник
# def draw_triangle(fill, base):
#     for i in range(base // 2 + 1):
#         for j in range(i + 1):
#             print(fill, end='')
#         print()
#     for i in range(base):
#         j = i
#         while j < base // 2:
#             j += 1
#             print(fill, end='')
#         print()
#
# f = input()
# b = int(input())
#
# draw_triangle(f, b)

# ФИО
# def fio(fn, ln, mn):
#     print(ln[0].upper(), fn[0].upper(), mn[0].upper(), sep='')
#
# fn = input()
# ln = input()
# mn = input()
#
# fio(fn, ln, mn)

# Сумма цифр
# def print_digit_sum(n):
#     s = 0
#     while n != 0:
#         s += n % 10
#         n //= 10
#     print(s)
#
# n = int(input())
#
# print_digit_sum(n)

# Конвертер километров
# def convert_to_miles(s):
#     return s * 0.6214
#
# n = int(input())
#
# print(convert_to_miles(n))

# Количество дней
# def get_days(m):
#     if m == 2:
#         return 28
#     elif (m % 2 == 0 and m < 7) or (m % 2 != 0 and m > 8):
#         return 30
#     else:
#         return 31
#
# n = int(input())
#
# print(get_days(n))

# Делители 1
# def get_factors(num):
#     return [i for i in range(1, num + 1) if num % i == 0]
#
# n = int(input())
#
# print(get_factors(n))

# Делители 2
# def number_of_factors(num):
#     return (len(get_factors(num)))
#
# n = int(input())
#
# print(number_of_factors(n))

# Найти всех
# def find_all(t, s):
#     return [i for i in range(len(t)) if t[i] == s]
#
# target = input()
# symbol = input()
#
# print(find_all(target, symbol))

# Merge lists 1
# def merge(ls1, ls2):
#     res = ls1 + ls2
#     res.sort()
#     return res
#
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
#
# print(merge(numbers1, numbers2))

# Merge lists 2
# ls = [input() for _ in range(int(input()))]
# res = []
#
# for i in range(len(ls)):
#     tmp = ls[i].split()
#     for j in range(len(tmp)):
#         tmp[j] = int(tmp[j])
#     res += tmp
# res.sort()
# print(*res)

# Is Valid Triangle?
# def is_valid_triangle(a, b, c):
#     if a < b + c and b < a + c and c < a + b:
#         return True
#     else:
#         return False
#
# x = int(input())
# y = int(input())
# z = int(input())
#
# print(is_valid_triangle(x, y, z))

# Is a Number Prime?
# def is_prime(num):
#     c = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             c += 1
#     if c == 2:
#         return True
#     else:
#         return False
#
# n = int(input())
#
# print(is_prime(n))

# Next Prime
# def get_next_prime(num):
#     num += 1
#     while not is_prime(num):
#         num += 1
#     return num
#
# n = int(input())
#
# print(get_next_prime(n))

# Good password
# def is_password_good(password):
#     cu = 0
#     cl = 0
#     cd = 0
#     if len(password) >= 8:
#         for i in range(len(password)):
#             if password[i].isalpha() and password[i] == password[i].upper():
#                 cu += 1
#             if password[i].isalpha() and password[i] == password[i].lower():
#                 cl += 1
#             if password[i].isdigit():
#                 cd += 1
#         if cu >= 1 and cl >= 1 and cd >= 1:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# s = input()
#
# print(is_password_good(s))

# Ровно в одном
# def is_one_away(word1, word2):
#     c = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 c += 1
#         if len(word1) - c == 1:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# w1 = input()
# w2 = input()
#
# print(is_one_away(w1, w2))

# Палиндром
# def is_palindrome(text):
#     text = text.replace(',', '')
#     text = text.replace('-', '')
#     text = text.replace('.', '')
#     text = text.replace('?', '')
#     text = text.replace(' ', '')
#     text = text.replace('!', '')
#     text = text.upper()
#     if text == text[::-1]:
#         return True
#     else:
#         return False
#
# s = input()
#
# print(is_palindrome(s))

# BEEGEEK
# def is_valid_password(password):
#     ls = [i for i in password.split(':')]
#     c = 0
#
#     if len(ls) == 3:
#         if ls[0] == ls[0][::-1]: # 1-ое палиндром
#             c += 1
#
#         cp = 0 # 2-ое простое
#         d = int(ls[1])
#         for i in range(1, d + 1):
#             if d % i == 0:
#                 cp += 1
#         if cp == 2:
#             c += 1
#
#         if int(ls[2]) % 2 == 0: # 3-е четное
#             c += 1
#
#         if c == 3:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# psw = input()
#
# print(is_valid_password(psw))

# Правильная скобочная последовательность
# def is_correct_bracket(text):
#     c = 0
#     for i in range(len(text)):
#         if c == 0 and text[i] == ')':
#             return False
#         else:
#             if text[i] == '(':
#                 c += 1
#             else:
#                 c -= 1
#
#     if c == 0:
#         return True
#     else:
#         return False
#
# s = input()
#
# print(is_correct_bracket(s))

# Змеиный регистр
# def convert_to_python_case(text):
#     res = ''
#     for i in range(len(text)):
#         if i != 0 and text[i].isupper():
#             res += '_' + text[i]
#         else:
#             res += text[i]
#     return res.lower()
#
# s = input()
#
# print(convert_to_python_case(s))

# Середина отрезка
# def get_middle_point(x1, y1, x2, y2):
#     return (x1 + x2) / 2, (y1 + y2) / 2
#
# ls = [int(input()) for i in range(4)]
#
# x, y = get_middle_point(ls[0], ls[1], ls[2], ls[3])
# print(x, y)

# Площадь и длина
# import math
# def get_circle(radius):
#     c = 2 * math.pi * radius
#     s = math.pi * pow(radius, 2)
#     return c, s
#
# r = float(input())
#
# length, square = get_circle(r)
# print(length, square)

# Корни уравнения
# from math import *
# def solve(a, b, c):
#     d = b * b - 4 * a * c
#     if d >= 0:
#         x1 = (-1 * b - sqrt(d)) / (2 * a)
#         x2 = (-1 * b + sqrt(d)) / (2 * a)
#         return min(x1, x2), max(x1, x2)
#
# a, b, c = int(input()), int(input()), int(input())
#
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# Калькулятор доставки
# def get_shipping_cost(quantity):
#     s = 0
#     if quantity == 1:
#         return 1000
#     else:
#         s += 1000
#         for i in range(quantity - 1):
#             s += 120
#         return s
#
# q = int(input())
#
# print(get_shipping_cost(q))

# Биномиальный коэффициент
# from math import *
# def compute_binom(n, k):
#     return int(factorial(n) / (factorial(k) * factorial(n - k)))
#
# n = int(input())
# k = int(input())
#
# print(compute_binom(n, k))

# Число словами
# def number_to_words(num):
#     list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
#     list_11 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if num < 11:
#         return list_1[num - 1]
#     elif 10 < num < 20:
#         p = num % 10
#         return list_11[p - 1]
#     else:
#         p1 = num // 10
#         p = num % 10
#         if p == 0:
#             s = list_21[p1 - 2]
#         else:
#             s = list_21[p1 - 2] + ' ' + list_1[p - 1]
#         return s
#
# n = int(input())
#
# print(number_to_words(n))

# Искомый месяц
# def get_month(language, number):
#     ls_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     ls_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if language == 'ru':
#         return ls_ru[number - 1]
#     if language == 'en':
#         return ls_en[number - 1]
#
# lan = input()
# num = int(input())
#
# print(get_month(lan, num))

# Магические даты
# def is_magic(date):
#     if int(date[0:2]) > 9: # день
#         d = int(date[0:2])
#     else:
#         d = int(date[1])
#
#     if int(date[3:5]) > 9: # месяц
#         m = int(date[3:5])
#     else:
#         m = int(date[4])
#
#     if int(date[8:10]) > 9: # год
#         y = int(date[8:10])
#     else:
#         y = int(date[9])
#
#     if d * m == y:
#         return True
#     else:
#         return False
#
# date = input()
#
# print(is_magic(date))

# Панграммы
# def is_pangram(text):
#     c = 0
#     alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     for i in range(len(text)):
#         if text[i].lower() in alp:
#             c += 1
#             del alp[alp.index(text[i].lower())]
#     if c == 26:
#         return True
#     else:
#         return False
#
# text = input()
#
# print(is_pangram(text))

# Звездный треугольник
# def draw_triangle():
#     for i in range(8):
#         print(' ' * (8 - 1 - i) + '*' * (1 + i * 2))
#
# draw_triangle()