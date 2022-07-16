# Задача №1
# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sumelements(arr):
    sum = 0
    for i in range(len(arr)):
        if i%2 != 0:
            sum = arr[i]+sum
    return sum

number = (list(tuple(input('Input array: ').split(' '))))
list = []
for i in number: 
    list.append(float(i))

print(sumelements(list))


