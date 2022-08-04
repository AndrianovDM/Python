# Задача №1

summa = 100
i = 0
count = 0
while summa != 0:
    if i ==0:
        print("Сейчас ходит пользователь, возьмите опред кол-во конфет (от 1 до 28): ")
        n = int(input())
        while n < 1 or n > 28:
            print('!!!!!!!!')   
            n = int(input())
        summa = summa - n
        print(f'Пользователь взял {n} конфет \nОсталось {summa} конфет')
        i = 1
    else:
        count = summa % 29
        summa = summa - count
        print(f'ИИ взял {count} конфет \nОсталось {summa} конфет')
        i = 0
if i == 1:
    print('Пользователь выиграл ')
else:
    print('ИИ выиграл ')
