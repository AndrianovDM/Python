# Задача №1
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# stroka = '267 12 963'
# list_1 = stroka.split()
# max = int(list_1[0])
# min = int(list_1[0])
# for i in list_1:
#     if int(i) > max:
#         max = int(i)
#     if int(i) < min:
#         min = int(i)

# print(max)
# print(min)


# Задача №2
# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if D == 0:
    print(f'Один корень и он равен = {round(-b /(2 * a),2)}') 
elif D < 0:
    print('Корней нет')
else:
    print(f'Первый корень равен = {round((-b + D**0.5)/(2 * a),2)}')
    print(f'Второй корень равен = {round((-b - D**0.5)/(2 * a),2)}')

    