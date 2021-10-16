"""
3. В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы.
"""

import random

array = [random.randint(0, 100) for _ in range(0, 15)]
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

array[ind_min], array[ind_max] = num_max, num_min
print(f'Max: array[{ind_max}] = {num_max}')
print(f'Min: array[{ind_min}] = {num_min}')
print('Замена:')
print(array)

