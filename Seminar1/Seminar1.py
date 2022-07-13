# Задача №1 
# Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

print ("Input number_1:")
number_1 =  int(input())
print ("Input number_2:")
number_2 = int(input())

if number_2 == number_1**2:
    print(f'{number_1}', ' = ', f'{number_2}')
elif number_1 == number_2**2:
    print(f'{number_2}', ' = ',  f'{number_1}')
else:
    print("Not square")





