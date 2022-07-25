# Создайте программу для игры в ""Крестики-нолики"".

from random import randint

def create_arr(size, sign):
    arr = [[ i for i in range(size+1)]]
    for i in range(size): 
        arr_1 = []
        arr.append(arr_1) 
        for j in range(size+1):
            if j == 0:
                arr_1.append(i+1)
            else:
                if sign == '*':
                    arr_1.append('*')
                if sign == 'O':
                    arr_1.append('O')
                if sign == 'X':
                    arr_1.append('X')
    return arr

def outlet(arr):
    for i in arr:
        for j in i:
            print((str(j).center(5)), end = " ")
        print()

def check(arr, size):
    array_o = create_arr(size, 'O')
    array_trans_o = [[j[i] for j in array_o] for i in range(len(array_o[0]))]
    arr_trans_o = [[j[i] for j in arr] for i in range(len(arr[0]))]
    array_diag_o = []

    array_x = create_arr(size, 'X')
    array_trans_x = [[j[i] for j in array_x] for i in range(len(array_x[0]))]
    array_diag_x = []

    arr_diag_left = [] 
    for i in range(1,len(arr)):
        for j in range(1,len(arr)):
            if i == j:
                array_diag_o.append(array_o[i][j])
                array_diag_x.append(array_x[i][j])
                arr_diag_left.append(arr[i][j])

    arr_diag_right = []
    for i in range(1,len(arr)):
        arr_diag_right.append(arr[i][-i])

    for i in range(1,len(arr)):
        if arr[i] == array_o[i]:
            return 0

    for i in range(1,len(arr)):
        if arr[i] == array_x[i]:
            return 1

    for i in range(1,len(arr)):
        if arr_trans_o[i] == array_trans_o[i]:
            return 0

    for i in range(1,len(arr)):
        if arr_trans_o[i] == array_trans_x[i]:
            return 1
    
    if array_diag_o == arr_diag_left:
        return 0

    if array_diag_x == arr_diag_left:
        return 1

    if array_diag_o == arr_diag_right:
        return 0

    if array_diag_x == arr_diag_right:
        return 1

size = int(input('Введите размер поля: '))
array_base = create_arr(size, '*')
print(outlet(array_base))
count = size**2 
st = randint(1,2)
if st == 1:
    print(f'Игрок №{st} ходит первым')
    while count > 0:
        i,j = map(int,input(f'Ход игрок №{st}:').split())
        array_base[i][j] = 'O'
        print()
        outlet(array_base)
        print()  

        if check(array_base,size) == 0: 
            print("Победил игрок №1")
            break

        if check(array_base,size) == 1: 
            print("Победил игрок №2")
            break 

        count -= 1
        i,j = map(int,input('Ход игрок №2:').split())
        array_base[i][j] = 'X'
        print()
        outlet(array_base)
        print()

        if check(array_base,size) == 0: 
            print("Победил игрок №1")
            break

        if check(array_base,size) == 1: 
            print("Победил игрок №2")
            break 
        count -= 1
else:
    print(f'Игрок №{st} ходит первым')
    while count > 0:
        i,j = map(int,input(f'Ход игрок №{st}:').split())
        array_base[i][j] = 'X'
        print()
        outlet(array_base)
        print()  

        if check(array_base,size) == 0: 
            print("Победил игрок №1")
            break

        elif check(array_base,size) == 1: 
            print("Победил игрок №2")
            break 

        count -= 1
        i,j = map(int,input('Ход игрок №1:').split())
        array_base[i][j] = 'O'
        print()
        outlet(array_base)
        print()

        if check(array_base,size) == 0: 
            print("Победил игрок №1")
            break

        if check(array_base,size) == 1: 
            print("Победил игрок №2")
            break 
        count -= 1
