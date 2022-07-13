# Задача №1 
# Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

# print ("Input number_1:")
# number_1 =  int(input())
# print ("Input number_2:")
# number_2 = int(input())

# if number_2 == number_1**2:
#     print(f'{number_1}', ' = ', f'{number_2}')
# elif number_1 == number_2**2:
#     print(f'{number_2}', ' = ',  f'{number_1}')
# else:
#     print("Not square")

# Второй вариант решения 

# a, b = map(int, input().split)
# if a ** 2 == b or b ** 2 == a:
#     print("Yes")
# else:
#     print("No")


# Задача №2 
# Напишите программу, 
# которая на вход принимает 5 чисел и находит максимальное из них.

# print("Input five numbers")
# number = list(map(int, input().split()))

# max_number =  number[0]
# for i in number:
#     if i > max_number:
#         max_number = i
# print(max_number)

# Задача №3 
# Напишите программу, 
# которая будет на вход принимать число N и выводить числа от -N до N.

# первый вариант решения

# print("Input numbers")
# number = int(input())
# print(*range(-number, number+1))

# второй вариант решения

# n = int(input('Введите число: '))
# for i in range(-n, n + 1):
#     print(i, end = ' ')


# Задача №4 
# Напишите программу, 
# которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# n = float(input('Введите число: '))
# print(int((n * 10) % 10))


# Задача №5
# Напишите программу, 
# которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# n = int (input())
# if ((n % 5 == 0 and n % 10 == 0) or (n % 15 == 0)) and n % 30 != 0:
#     print("Yes")
# else:
#     print("No")


