# Задача №1
# Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

import time

from numpy import _2Tuple
from sympy import li

print(int(str(time.time_ns())[-4] + str(time.time_ns())[-3]))
for i in range(10):
    time.sleep(0.1)
    if i%2 == 0:
        print(int(str(time.time_ns())[-4] + str(time.time_ns())[-3]))
    else:
        print(int(str(time.time_ns())[-4] + str(time.time_ns())[-3]))
