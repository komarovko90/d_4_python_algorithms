"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его
значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и
«максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

array = [random.randint(-50, 50) for _ in range(0, 20)]
print(array)
negative_ind = [i for i, el in enumerate(array) if el < 0]
num_max = array[negative_ind[0]]
ind_max = negative_ind[0]
for i in negative_ind:
    if num_max < array[i]:
        num_max = array[i]
        ind_max = i

print(f'Max negative: array[{ind_max}] = {array[ind_max]}')
