# Задача №1
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sumelements(arr):
#     sum = 0
#     for i in range(len(arr)):
#         if i%2 != 0:
#             sum = arr[i]+sum
#     return sum

# number = (list(tuple(input('Input array: ').split(' '))))
# list = []
# for i in number: 
#     list.append(float(i))

# print(sumelements(list))


# Задача №2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def productOfPairs(array):
#     new_array = []
#     for i in range(len(array)//2):
#         new_num = array[i] * array[-i-1]
#         new_array.append(new_num)
#     if len(array)%2 != 0:
#         new_num = array[len(array)//2]**2
#         new_array.append(new_num)
#     return new_array

# number = (list(tuple(input('Input array: ').split(' '))))
# list = []
# for i in number: 
#     list.append(float(i))

# print(f'{list}'+'->'+ f'{productOfPairs(list)}')

# Задача №3
# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# def maxMinNumber(array, maxmin):

#     if maxmin == 'max':
#         max_number = array[0]%1
#         for i in range(len(array)):
#             if array[i]%1 > max_number:
#                 max_number = array[i]%1
#         return max_number
    
#     if maxmin == 'min':
#         min_number = array[0]%1
#         for i in range(len(array)):
#             if array[i]%1 < min_number:
#                 min_number = array[i]%1

#         return min_number

# arr = (list(tuple(input('Input array: ').split(' '))))
# list = []
# for i in arr: 
#     list.append(float(i))

# max_num = round(maxMinNumber(list, 'max'),2)
# min_num = round(maxMinNumber(list, 'min'),2)

# print(f'{list}'+' -> '+ 'max: ' f'{max_num}' + ' min: ' f'{min_num}' )
# print('number difference: ' + f'{max_num - min_num}')


# Задача №4
# Напишите программу, 
# которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# number = int(input('Input number: '))
# def ConvertNumber(number):
#     bin_num = ''
#     while number > 0:
#         bin_num = str(number % 2) + bin_num
#         number = number // 2
#     return bin_num

# bin_number = ConvertNumber(number)

# print(f'{number}' + ' convert -> ' + f'{bin_number}')


# Задача №5
# *Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def negaFibonachi(num):
#     arr_right = [ 0, 1 ]
#     arr_left = [ 0, 1 ]

#     for i in range(num-1):
#         new_num_right = arr_right[i] + arr_right[i + 1]
#         arr_right.append(new_num_right)
#         new_num_left = arr_left[i] - arr_left[i+1]
#         arr_left.append(new_num_left)
#     arr_left.pop (0)
#     arr_right.pop (1)
#     arr_right.reverse()
#     arr = arr_right + arr_left
#     arr.reverse()
#     return arr

# print(negaFibonachi(8))

       

    





        

