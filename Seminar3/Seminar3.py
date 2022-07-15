# Задача №1
# Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

# import time

# print(int(str(time.time_ns())[-4] + str(time.time_ns())[-3]))
# for i in range(10):
#     time.sleep(0.1)
#     if i%2 == 0:
#         print(int(str(time.time_ns())[-4] + str(time.time_ns())[-3]))
#     else:
#         print(int(str(time.time_ns())[-4] + str(time.time_ns())[-3]))

# Задача №2
# Задайте список. 
# Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# ПРИМЕР 1
# def Searchlist(arr, nmber):
#     for i in arr:
#         if i == str(nmber):
#             return 'Yes'
#     return 'No'

# list1 = ['hello', '12', 'red', '567']
# print(Searchlist(list1, 12))

# ПРИМЕР 2
# def Searchlist(arr, nmbers):
#     if str(nmbers) in arr:
#         return 'Yes'
#     return 'No'

# list1 = ['hello', '12', 'red', '567']
# print(Searchlist(list1, 12))


