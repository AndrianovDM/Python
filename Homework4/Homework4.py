# Задача №1 
# Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141


num = int(input("Enter the number of decimal places for pi: "))
i= 0
number_pi = 0
while i < num:
    num_summ =  (1/ 16**(i)) * ((4 / ( 8*i + 1 )) - (2 / ( 8*i + 4 )) - (1 / ( 8*i + 5 )) - (1 / ( 8*i + 6 )))
    number_pi += num_summ
    i+=1
print("Number PI: " + f'{round(number_pi, num)}')

