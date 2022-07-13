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

print("Input five numbers")
number = list(map(int, input().split()))

max_number =  number[0]
for i in number:
    if i > max_number:
        max_number = i
print(max_number)








