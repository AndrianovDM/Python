# Задача №28
# Напишите такое лямбда выражение transformation, чтобы 
# transformed_values получился копией values

# transformation = lambda val: val
# values = [1, 23, 42, "asdfg"]
# transformed_values =list(map(transformation, values))
# if values == transformed_values:
#     print('OK')
# else:
#     print('FAIL')


# Задача №29
# Самая далекая планета


# def find_farthest_orbit(list):
#     val = max([(list[i][0]*list[i][1]) for i in range(len(list)) if list[i][0] != list[i][1]])
#     return [list[i] for i in range(len(list)) if list[i][0]*list[i][1] == val][0]

# orbits = [(1,3), (2.5, 10), (7,2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))


# Задача №30
# Пам-парам парам -пам - пам

words = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
phrase = list(map(str, input('Введите стихотворение').split()))
sum = []
for i in phrase:
    count = 0
    for j in i:
        if j in words:
            count += 1
        else:
            count
    sum.append(count)

if len(set(sum)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
    print(count)






