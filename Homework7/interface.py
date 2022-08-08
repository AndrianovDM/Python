from data_func import view_data 
from data_func import delete_data
from data_func import export_import
from data_func import сreate_data
from logger import data_add_logger

def main_menu():
    while True:
        print('Добро пожаловать в телефонный справочник!\n Выберите одно из:')
        menu = {'1':'Создать новый справочник\n', '2': 'Посмотреть справочник данных\n', '3': 'Добавить новую запись\n', '4': 'Удалить запись\n', '5': 'Экспорт-Импорт\n', '6': 'Выход\n'}
        print(' 1:' ,menu['1'], '2:', menu['2'], '3:', menu['3'], '4:', menu['4'], '5:', menu['5'], '6:', menu['6'])
        option = int(input('Выбрать:'))

        if option == 1:
            menu_one = {'1':'Создать в формате 1\n', '2': 'Создать в формате 2\n'}
            print(' 1:' ,menu_one['1'], '2:', menu_one['2'])
            option_one = int(input('Выбрать:'))
            data = сreate_data()
            if option_one == 1:
                data_add_logger(data, option_one)
            if option_one == 2:
                data_add_logger(data, option_one)
                
        elif option == 2:
            menu_two = {'1':'Показать в формате 1\n', '2': 'Показать в формате 2\n'}
            print(' 1:' ,menu_two['1'], '2:', menu_two['2'])
            option_two = int(input('Выбрать:'))
            if option_two == 1:
                view_data(option_two)
            if option_two == 2:
                view_data(option_two)

        elif option == 3:
            menu_three = {'1':'Дбавить в формат 1\n', '2': 'Дбавить в формат 2\n'}
            print(' 1:' ,menu_three['1'], '2:', menu_three['2'])
            option_three = int(input('Выбрать:'))
            data = сreate_data()
            if option_three == 1:
                data_add_logger(data, option_three)
            if option_three == 2:
                data_add_logger(data, option_three)

        elif option == 4: 
            menu_four = {'1':'Удалить в формате 1\n', '2': 'Удалить в формате 2\n'}
            print(' 1:' ,menu_four['1'], '2:', menu_four['2'])
            option_four = int(input('Выбрать:'))
            if option_four == 1:
                view_data(option_four)
                option_five = int(input('Выбрать номер элемента:'))
                delete_data(option_four, option_five-1)
            if option_four == 2:
                view_data(option_four)
                option_five = int(input('Выбрать номер элемента:'))
                delete_data(option_four, option_five-1)

        elif option == 5: 
            menu_six = {'1':'Формат 1 импортировать в формат 2\n', '2': 'Формат 2 импортировать в формат 1\n'}
            print(' 1:' ,menu_six['1'], '2:', menu_six['2'])
            option_six = int(input('Выбрать:'))
            if option_six == 1:
                export_import(option_six)
            if option_six == 2:
                export_import(option_six)

        elif option == 6: 
            break

