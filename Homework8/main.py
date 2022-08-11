# Задание на семинаре:
# Создать решение для вывода детей по фамилии

# Домашнее задание:
# Дополнить таблицу 


database = {}
db = {'parents':1, 'children':2}

def reading_file_to_dict(number_file):
    with open(f'C:\\Users\\Dmitry\\Downloads\\Postgraduate studies\\Homework program\\Python\\Homework8\\{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        # print(data)
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))
        print(database)

def print_childrens(second_name):
    id = [i[0] for i in database[db['parents']] if second_name in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:4]) + '\n' for i in deti])

# Создал фильтр который позволяет определить по фамилии работает ли человек или нет

def print_job(second_name):
    id_parents = [i[0] for i in database[1] if second_name in i][0]
    id_children = [i[0] for i in database[2] if second_name in i][0]
    id_parents = [i for i in database[3] if id_parents == i[1] or id_children == i[1]]
    print(*[' '.join(i[2:3]) + '\n' for i in id_parents])

reading_file_to_dict(1)
print()
reading_file_to_dict(2)
print()
reading_file_to_dict(3)
print()
print_job('Ivanov')

