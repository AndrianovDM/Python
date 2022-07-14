# Задача №1
# Число фибоначи
n = int (input())
a0 = 0
a1 = 1
x = 1

for i in range(n):
    x = a0 + a1
    a0 = a1
    a1 = x
print(a0)