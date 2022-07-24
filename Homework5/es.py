def outlet(arr):
    for i in arr:
        for j in i:
            print('%3s' %(j), end = " ")
        print()

arr = [[0, 1, 2, 3],
       [1, '2', '*', '*'],
       [2, '*', '2', '*'],
       [3, '*', '*', '2']]

arrr = [[0, 1, 2, 3],
       [1, '*', '*', '2'],
       [2, '*', '2', '*'],
       [3, '2', '*', '*']]

l1 = [[4, 5, 3, 9],
      [7, 1, 8, 2],
      [5, 6, 4, 7]]

arr_diag_right = []

for i in range(1,len(arrr)):
    print(arrr[i][-i])

