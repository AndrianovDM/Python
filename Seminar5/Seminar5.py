'''
r - read (читать)
w - write (удаляет все данные, которые были, и записывает новые)
a - appened (добавить)

'''

# file = open ('1.txt', 'r', encoding = 'utf-8')
# print(file.readlines())

# file = open ('1.txt', 'w', encoding = 'utf-8')
# print(file.write('6'))

# file = open ('1.txt', 'a', encoding = 'utf-8')
# file.close()
# print(file.write('\n6'))

# with open('1.txt', 'a', encoding = 'utf-8') as file:
#     file.write('\n6')


# x = lambda y: y**10
# print(x(5))

# x, y = map(int, ('12', '34'))
# print(x, y)

# x, y = filter(int, ('12', '34'))  фозвращает true или false
# print(type(x), type(y))

# a, b = map(int, input().split())
# print(a+b)


# Задача №1
# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного,чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

# with open('1.txt', 'r', encoding = 'utf-8') as file:
#     arr = file.readlines()
#     arr = [int(i) for i in arr[0].split()]
#     for i in range(1, len(arr)):
#         if arr[i] -1 != arr[i-1]:
#             print((arr[i - 1] + arr[i])/2)


# Задача №2
# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# arr = [1, 5, 2, 3, 4, 6, 1, 7]
# print(min(arr), max(arr), sep = ", ")


# Задача №3
#  Напишите программу, удаляющую из текста все слова, содержащие "абв"

# print(''.join(input().lower().split('абв')))
