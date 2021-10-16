"""
6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.
"""

import random
array = [random.randint(0, 50) for _ in range(0, 20)]
print(array)

ind_min = 0
ind_max = 0
num_min = array[0]
num_max = array[0]
for i, el in enumerate(array):
    if num_min > el:
        num_min = el
        ind_min = i
    if num_max < el:
        num_max = el
        ind_max = i

print(f'Max: array[{ind_max}] = {array[ind_max]}')
print(f'Min: array[{ind_min}] = {array[ind_min]}')
if ind_min > ind_max:
    ind_min, ind_max = ind_max, ind_min
print(f'{array[ind_min+1:ind_max]}')
print(f'Сумма: {sum(array[ind_min+1:ind_max])}')
