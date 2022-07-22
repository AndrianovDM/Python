# Задача №1 
# Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141


# num = int(input("Enter the number of decimal places for pi: "))
# i= 0
# number_pi = 0
# while i < num:
#     num_summ =  (1/ 16**(i)) * ((4 / ( 8*i + 1 )) - (2 / ( 8*i + 4 )) - (1 / ( 8*i + 5 )) - (1 / ( 8*i + 6 )))
#     number_pi += num_summ
#     i+=1
# print("Number PI: " + f'{round(number_pi, num)}')


# Задача №2
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых делителей числа N. (1 - составное число)

# num = int(input("Input integer number: "))
# list_1 = list(range(2,num+1))
# new_list_one = []
# for i in list_1:
#     if num % i == 0:
#         new_list_one.append(i)

# new_list_two = []
# # print(new_list_one)
# for i in new_list_one:
#     for j in range(2, i ):
#         if i % j == 0:
#             new_list_two.append(i)
#             break

# print(" List of prime divisors of " + f'{num}:' + f' {(list(set(new_list_one) - set(new_list_two)))}')


# Задача №3
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

number = (list(tuple(input('Input array: ').split(' '))))
list = []
for i in number: 
    list.append(float(i))
print(f"Old array: {list}")

new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(f"New array: {new_list}")


# Задача №4
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint

# k = int(input("Input integer number: "))
# list = [randint(0, 100) for i in range(k+1)]

# def polynomial(k , array ):
#     equation =''
#     for i in range(k):
#         polyn = f'{array[i]}*'+ f'x^{k-i} + '
#         equation = equation + polyn
#         if i == k-2:
#             break
#     equation = 'Example: ' + equation + f'{array[k-1]}*x' + f' + {array[k]}' + ' = 0'
#     return equation

# print(polynomial(k, list))        


