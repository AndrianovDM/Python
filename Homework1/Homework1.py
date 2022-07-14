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

x, y, z = map(int, input("Введите значение X, Y, Z: ").split())
if ((not(x or y or z)) == (not x and not y and not z)) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")

