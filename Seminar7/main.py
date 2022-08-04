from func import operation
from log import log

def main():
    menu = {'+':'Сложение', '-':'Вычитание', '*':'Умножение', '/': 'Деление'}
    print(menu)
    oper = str(input('Выберите действие: '))
    first = complex(input('Введите первое число: '))
    second = complex(input('Введите второе число: '))
    num = operation(oper, first, second)
    logger = log(str(num))

if __name__ == '__main__':
    main()