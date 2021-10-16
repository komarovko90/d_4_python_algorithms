"""
8. Матрица 4x5 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

import random

matrix = []
for i in range(0,4):
    line = []
    for j in range(0, 4):
        line.append(int(input(f'Введите элемент матрицы [{i+1}][{j+1}]: ')))
    line.append(sum(line))
    matrix.append(line)

for line in matrix:
    for item in line:
        print(f'{item:<4}', end='')
    print()


