# Задача №1
# Напишите программу, 
# которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.


number_day = int(input("Number day weeks: "))

if number_day == 6 or number_day == 7:
    print(f'{number_day}' + '-> Day off of the week')
elif 1<= number_day <=5:
    print(f'{number_day}' + "-> Weekday")
