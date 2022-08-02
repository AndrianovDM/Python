# Задача №1
# Напишите такое лямбда выражение transformation, чтобы 
# transformed_values получился копией values

transformation = lambda val: val
values = [1, 23, 42, "asdfg"]
transformed_values =list(map(transformation, values))
if values == transformed_values:
    print('OK')
else:
    print('FAIL')

