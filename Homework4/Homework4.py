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

num = int(input("Input integer number: "))
list_1 = list(range(2,num+1))
new_list_one = []
for i in list_1:
    if num % i == 0:
        new_list_one.append(i)

new_list_two = []
# print(new_list_one)
for i in new_list_one:
    for j in range(2, i ):
        if i % j == 0:
            new_list_two.append(i)
            break

print(" List of prime divisors of " + f'{num}:' + f' {(list(set(new_list_one) - set(new_list_two)))}')

