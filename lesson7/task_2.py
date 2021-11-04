import random

"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами 
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
Сортировка слиянием (Merge Sort)
"""

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

my_list = [random.randint(0, 49) for _ in range(30)]
# my_list = [i for i in range(10)]
# random.shuffle(my_list)


print(my_list)

print(merge_sort(my_list))
