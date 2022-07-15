# Задача №1
# Напишите программу, 
# которая принимает на вход вещественное число и показывает сумму его цифр.

# number = float(input("Input number: "))
# number = str(number)
# num = number.split(".") 
# integer = int(num[0])
# fractional = int(num[1])
# sum = 0
# while (integer != 0): 
#     sum = sum + (integer % 10)
#     integer = integer // 10

# while (fractional != 0): # перемножаем числа дробной части
#     sum = sum + (fractional % 10)
#     fractional = fractional // 10

# print("Сумма чисел: ",sum)

# Задача №2
# Напишите программу, 
# которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал

number = int(input("Input number: "))
start = 1
for i in range(1,number+1):
    num = i * start
    start = num

print(f'{number}! = ', start)






