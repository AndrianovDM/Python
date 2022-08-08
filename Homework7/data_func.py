def сreate_data():
    family = str(input('Фамилия: '))
    name  = str(input('Имя: '))
    number = str(input('Телефон: '))
    comment = str(input('Комментарий: '))
    data = {'Фамилия: ':family, 'Имя: ': name, 'Телефон: ': number, 'Комментарий: ': comment}
    return data

def view_data(method):
    if method == 1:
        file = open('data_one.txt','r', encoding = 'utf-8')
        print(*file.readlines())
        file.close()

    if method == 2:
        file = open('data_two.txt','r', encoding = 'utf-8')
        count = 0
        for i in file.readlines():
            if count%2 == 0:
                print(i)
            count = count + 1
        file.close()

def delete_data(method, index):
    if method == 1:
        file = open('data_one.txt','r', encoding = 'utf-8')
        arr = list(file.readlines())
        if index == 0:
            arr.pop(0)
        else:
            arr.pop(index)
        with open('data_one.txt','w', encoding = 'utf-8') as file:
            file.write('')
        for i in arr:
            with open('data_one.txt','a', encoding = 'utf-8') as file:
                file.write('{}'.format(i))

    if method == 2:
        file = open('data_two.txt','r', encoding = 'utf-8')
        arr = list(file.readlines())
        if index == 0:
            for i in range(8):
                arr.pop(0)
        else:
            for i in range((8*index)-8, 8*index):
                arr.pop(((8*index)-8))
        with open('data_two.txt','w', encoding = 'utf-8') as file:
            file.write('')
        for i in arr:
            with open('data_two.txt','a', encoding = 'utf-8') as file:
                file.write('{}'.format(i))

def export_import(method):
    if method == 1:
        file = open('data_one.txt','r', encoding = 'utf-8')
        arr = list(file.readlines())
        for i in arr:
            for j in i:
                if j ==',':
                    j = ',\n\n'
                if j == ';':
                    j = ';\n\n'
                with open('data_two_import.txt','a', encoding = 'utf-8') as file:
                    file.write('{}'.format(j))
    if method == 2:
        file = open('data_two.txt','r', encoding = 'utf-8')
        arr = list(file.readlines())
        for i in arr:
            for j in i:
                if j =='\n':
                    j = ''
                if j ==';':
                    j = ';\n'
                with open('data_one_import.txt','a', encoding = 'utf-8') as file:
                    file.write('{}'.format(j))

# def save_data():
#     pass
# print(сreate_data())

# srr = [1,2,3,4,5,6,7,8,9]
# srr.pop(0)
# print(srr)