# Задача №1
# Напишите программу, 
# которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.


# number_day = int(input("Number day weeks: "))

# if number_day == 6 or number_day == 7:
#     print(f'{number_day}' + '-> Day off of the week')
# elif 1<= number_day <=5:
#     print(f'{number_day}' + "-> Weekday")


# Задача №2
# Напишите программу для. 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x, y, z = map(int, input("Введите значение X, Y, Z: ").split())
# if ((not(x or y or z)) == (not x and not y and not z)) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")


# Задача №3
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# print("Введите координату точки X:")
# x = float(input())
# print("Введите координату точки Y:")
# y = float(input())

# if x > 0 and y > 0:
#     value = 1
#     print(f"Точка находится в {value} четверти")
# elif x < 0 and y > 0:
#     value = 2
#     print(f"Точка находится в {value} четверти")
# elif x < 0 and y < 0:
#     value = 3
#     print(f"Точка находится в {value} четверти")
# elif x > 0 and y <0:
#     value = 4
#     print(f"Точка находится в {value} четверти")
# elif x == 0 and (y > 0 or y < 0):
#     print(f"Точка находится на оси X")
# elif y == 0 and (x > 0 or x < 0):
#     print(f"Точка находится на оси Y")
# elif x == 0 and y == 0:
#     print("Одна из координат должна быть больше 0!!!")


# Задача №4
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input("Введите номер четверти: "))
if 5 <= quarter_number or quarter_number <= 0:
    print("Введите номер четверти от 1 до 4")
if quarter_number == 1:
    print("Дипазон значений точки: x > 0 , y > 0")
elif quarter_number == 2:
    print("Дипазон значений точки: x < 0 , y > 0")
elif quarter_number == 3:
    print("Дипазон значений точки: x < 0 , y < 0")
elif quarter_number == 4:
    print("Дипазон значений точки: x > 0 , y < 0")




