                                            # Задача №1
# Число фибоначи

# n = int (input())
# a0 = 0
# a1 = 1
# x = 1

# for i in range(n):
#     x = a0 + a1
#     a0 = a1
#     a1 = x
# print(a0)

                                            # Задача №_2
# Напишите программу, которая принимает на вход число N 
# и выдаёт последовательность из N членов.
# Заполнение случайными числами!

                                    # ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ

# from random import randint
# number = int (input('Введите число:'))
# numbers = []
# for i in range(number):
#    num = randint(0,number)
#    numbers.append(num)
# print(numbers)

                                    # ВТОРОЙ ВАРИАНТ РЕШЕНИЯ
# n = int (input('Введите кол-во элементов:'))
# x = 1
# for i in range(n):
#     if n -1 == i:
#         print(x)
#     else:
#         print(x, end = ', ')
#     x = x *(-3)


                                        # Задача №3
# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.

import numbers
n = int(input('Введите кол-во элементов:'))
number = {}
for i in range(1, n+1):
    number[i] = 3 * i + 1
print(number)
