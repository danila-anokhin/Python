# Назад, вперёд и наоборот
# s = input().split()
# if len(s) % 2 == 1:
#     ld = s[-1]
#     s = s[:-1]
#     for i in range(0, len(s) - 1, 2):
#         s[i], s[i + 1] = s[i + 1], s[i]
#     s.append(ld)
# else:
#     for i in range(0, len(s) - 1, 2):
#         s[i], s[i + 1] = s[i + 1], s[i]
#
# print(*s)

# Сдвиг в развитии
# s = input().split()
# ld = [s[-1]]
# s = s[:-1]
# ld.extend(s)
# print(*ld)

# Различные элементы
# s = input().split()
# c = 1
# d = s[0]
# for i in range(len(s)):
#     if s[i] != d:
#         d = s[i]
#         c += 1
# print(c)

# Произведение чисел
# n = int(input())
# ls = []
#
# for i in range(n):
#     ls.append(int(input()))
#
# res = int(input())
# flag = False
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if ls[i] * ls[j] == res:
#             flag = True
#             break
#         else:
#             continue
#
# if flag:
#     print('ДА')
# else:
#     print('НЕТ')

# Камень, ножницы, бумага
def rps(tim, rus):
    if tim == rus:
        return 'ничья'
    elif tim == 'камень':
        if rus == 'ножницы':
            return 'Тимур'
        else:
            return 'Руслан'
