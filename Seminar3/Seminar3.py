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


# Задача №3
# Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*
# - список: ["qwerty", "asd", "zxc", "qwerty", "ertqwe"], ищем: "qwerty", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# def SearchElem(arr, element):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == element:
#             count += 1
#         if count == 2:
#             return f'yes: {i + 1}'
#     return 'no'

# print(SearchElem(["123", "234", 123, "567"], '123'))

