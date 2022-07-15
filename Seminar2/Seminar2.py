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
