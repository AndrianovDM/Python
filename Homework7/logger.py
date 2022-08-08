
def data_add_logger(data, method):
    if method == 1:
        with open('data_one.txt','a', encoding = 'utf-8') as file:
            file.write('{},{},{},{};\n'
                        .format(data['Фамилия: '], data['Имя: '], data['Телефон: '], data['Комментарий: ']))
    if method == 2:
        with open('data_two.txt','a', encoding = 'utf-8') as file:
            file.write('{},\n\n{},\n\n{},\n\n{};\n\n'
                        .format(data['Фамилия: '], data['Имя: '], data['Телефон: '], data['Комментарий: ']))

