# Задача №1
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных

                                    # ПЕРВЫЙ МЕТОД ЗАПИСИ

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

                                    # ВТОРОЙ МЕТОД ЗАПИСИ
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 1\n')

                                    # МЕТОД ЧТЕНИЯ ДАННЫХ

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print (line)
# data.close()

                                        # ФУНКЦИИ

# def new_string(symbol, count):
#  return symbol * count
# print(new_string('!', 5)) 
# print(new_string('!')) 

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1', 'd', '2')) 
# print(concatenatio(1, 2, 3, 4)) 

                                        # РЕКУРСИЯ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

                                        # КОРТЕЖИ 
# Кортеж – это неизменяемый “список”

# t = ()
# print(type(t)) 
# t = (1,)
# print(type(t)) 
# t = (1)
# print(type(t)) 
# t = (28, 9, 1990)
# print(type(t)) 
# colors = ['red', 'green', 'blue']
# print(colors) 
# t = tuple(colors)
# print(t)

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) 
# print(t[2]) 
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) 
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

                                    # СЛОВАРИ

# Словари - Неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

                                    # МНОЖЕСТВА

# Множества - неупорядоченная совокупность элементов

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

                                # Операции над множествами

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

                                # Неизменяемое множество

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


                                        # СПИСКИ

# list1 = [1, 2, 3, 4, 5]
# list2 =list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)


# list1[0] = 123
# list2[0] = 333
# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# print(list1)
# print(list1.pop())
# print(len(list1))
# print(list1)

# print(list1)
# print(list1.insert(2,11))
# print(len(list1))
# print(list1)

# print(list1)
# print(list1.append(11))
# print(len(list1))
# print(list1)



