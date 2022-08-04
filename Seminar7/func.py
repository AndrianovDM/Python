def operation(oper, a, b):
    if oper == '+':
        result = a + b
        print(f'{a} + {b} = {a + b}')
    elif oper == '-':
        result = a - b
        print(f'{a} - {b} = {a - b}')
    elif oper == '*': 
        result = a * b
        print(f'{a} * {b} = {a * b}')
    else:
        result = a / b
        print(f'{a} / {b} = {a / b}')
    return result


