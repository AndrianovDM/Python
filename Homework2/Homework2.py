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

# while (fractional != 0): 
#     sum = sum + (fractional % 10)
#     fractional = fractional // 10

# print("Sum number: ",sum)

# Задача №2
# Напишите программу, 
# которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал

# number = int(input("Input number: "))
# start = 1
# for i in range(1,number+1):
#     num = i * start
#     start = num

# print(f'{number}! = ', start)


# Задача №3
# Задана последовательность натуральных чисел, завершающаяся числом 0. 
# Требуется определить значение второго по величине элемента в этой последовательности, 
# то есть элемента, который будет наибольшим, если из последовательности удалить наибольший элемент.

number = (list(tuple(input().split(' '))))
list = []
for i in number: 
    list.append(float(i))
max_number_one =  list[len(list)-1]

for i in list:
    if i > max_number_one:
        max_number_one = i
list.pop(list.index(max_number_one))

max_number_second =  list[len(list)-1]

for j in list:
    if j > max_number_second:
        max_number_second = j
print("Second max number: ", max_number_second)
















