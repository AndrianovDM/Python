                                   # Типы данных и переменная 
# int, float, boolean, str, list, None
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value  = 12334
# print(type(value))

# s = 'hello world'
# print(s) # вывод строки
# print(a, b, s)
# print (a, ' - ', b,' - ', s)
# print ('{} - {} - {}'.format(a, b, s))
# print (f'{a} - {b} - {s}')

                                        # Массивы

# list = ['1','2','3','Hello World', 1,2,4.5, True]
# print(list)

                                      #print , input

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, b)
# print (f'{a} {b}')
# print(a, '+', b, '=', a+b)

                                  # Логические операции

# > , >= , <, <=, ==, !=
# not, and, or -  не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 4 < 5 
# print(a)

# func = 1
# T = 4
# x = 123

# print(func<T>(x))

# f = [1,2,34,5]
# print(f)
# print(not 2 in f)
# is_odd = not f[0] % 2 
# print(is_odd)

                              # Управляющие конструкции if, else  

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)


# original = 4342
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# for i in 1,2,4,5,6:
#     print(i**2)

# for i in range(1,5):
#     print(i)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...


# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
