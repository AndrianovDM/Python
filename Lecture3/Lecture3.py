                                # Анонимные, lambda функции
# Идея: часто описывать функцию некогда и незачем

# def sum(x):
#  return x+10

# def mult(x):
#  return x**2

# print(sum(mult(2)))

# sum = lambda x: x+10
# mult = lambda x: x**2

# print(sum(2))

# def h(f, g, x): return f(g(x))h = lambda f, g, x: f(g(x))
# h(sum, mult, 5)
# h(lambda x: x+10, lambda x: x**2, 5)

# ЗАДАЧА №1
# В файле хранятся числа, нужно выбрать четные и
# составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()

# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)

# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]

# Первый вариант решения
# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))

# Второй вариант решения
# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int, data))
# data = list(filter(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e**2), data))
# print(data)

                                        # List Comprehension

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

# ПРИМЕР#1
# list = []
# for i in range(1,101):
#     if(i%2 == 0):
#         list.append(i)
# print(list)

# ПРИМЕР#2
# list_1 = [ i for i in range(1,101) if(i%2 == 0)]
# print(list_1)

# ПРИМЕР#3
# def f(x):
#     return x**2

# list_1 = [(i,f(i)) for i in range(1,101) if(i%2 == 0)]
# print(list_1)


                                            # Функция map


# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.

# li = [x for x in range(1, 20)]

# li = list(map(lambda x:x +10, li))
# print(li)

# data =  map(int , input('Input data').split())


                                        # Функция filter

# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для
# которых функция вернула True.

# data = [x for x in range(10)]
# print(data)
# res  = list(filter(lambda x: x%2==0, data))
# print(res)


                                         # Функция zip

# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из
# элементов входных данных.

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]

# data =  list(zip(users, ids))
# print(data)


                                        # Функция enumerate

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.

# users = ['user1', 'user2', 'user3', 'user4', 'user5']

# data =  list(enumerate(users))
# print(data)
