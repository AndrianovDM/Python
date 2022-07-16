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

def productOfPairs(array):
    new_array = []
    for i in range(len(array)//2):
        new_num = array[i] * array[-i-1]
        new_array.append(new_num)
    if len(array)%2 != 0:
        new_num = array[len(array)//2]**2
        new_array.append(new_num)
    return new_array

number = (list(tuple(input('Input array: ').split(' '))))
list = []
for i in number: 
    list.append(float(i))


print(f'{list}'+'->'+ f'{productOfPairs(list)}')
