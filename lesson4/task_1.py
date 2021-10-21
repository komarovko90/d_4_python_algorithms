import cProfile
import functools
"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

Для расчетов времени выпонения берем следующую задачу из урока 2:
    4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    Количество элементов (n) вводится с клавиатуры.
"""


def test_series(func):
    lst = [0, 1, 0.5, 0.75, 0.625, 0.6875]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

# 1 вариант - цикл
def sum_series(n):
    a = 1
    sum = 0
    for i in range(n):
        sum += a
        a /= (-2)
    return sum

# вариант 1
# python -m timeit -n 1000 -s "import task_1" "task_1.sum_series(10)
# .sum_series(10)
# 1000 loops, best of 5: 1.19 usec per loop

# .sum_series(100)
# 1000 loops, best of 5: 15.7 usec per loop

# .sum_series(1000)
# 1000 loops, best of 5: 102 usec per loop

# .sum_series(10000)
# 1000 loops, best of 5: 1.13 msec per loop

# cProfile.run('sum_series(1000)')
# 1 task_1.py: 24(sum_series) 10
# 1 task_1.py: 24(sum_series) 100
# 1 task_1.py: 24(sum_series) 1000
# 1 task_1.py: 24(sum_series) 10000

# 2 вариант - рекурсия
def generate_row(n):
    if n <= 1:
        return n
    else:
        return generate_row(n - 1) * (- 0.5)

def sum_series2(n):
    i = 0
    result = 0
    while i <= n:
        result += generate_row(i)
        i += 1
    return result

# test_series(sum_series2)
# вариант 2
# python -m timeit -n 1000 -s "import task_1" "task_1.sum_series2(10)

# .sum_series2(10)
# 1000 loops, best of 5: 10.1 usec per loop

# .sum_series2(100)
# 1000 loops, best of 5: 904 usec per loop

# .sum_series2(500)
# 1000 loops, best of 5: 26.3 msec per loop

# .sum_series2(1000) - error

# cProfile.run('sum_series2(500)')

# 56/11    0.000    0.000    0.000    0.000 task_1.py:53(generate_row) - 10
# 5051/101    0.002    0.000    0.002    0.000 task_1.py:53(generate_row) - 100
# 125251/501    0.056    0.000    0.056    0.000 task_1.py:53(generate_row) - 500

# 3 вариант - рекурсия c мемоизацией

@functools.lru_cache()
def generate_row2(n):
    if n <= 1:
        return n
    else:
        return generate_row2(n - 1) * (- 0.5)

def sum_series3(n):
    i = 0
    result = 0
    while i <= n:
        result += generate_row2(i)
        i += 1
    return result

# вариант 3
# python -m timeit -n 1000 -s "import task_1" "task_1.sum_series3(10)

# .sum_series3(10)
# 1000 loops, best of 5: 2.22 usec per loop

# .sum_series3(100)
# 1000 loops, best of 5: 18.4 usec per loop

# .sum_series3(1000)
# 1000 loops, best of 5: 566 usec per loop

# .sum_series3(10000)
# 1000 loops, best of 5: 5.98 msec per loop

# cProfile.run('sum_series3(10000)')

# 11    0.000    0.000    0.000    0.000 task_1.py:91(generate_row2) - 10
# 101    0.000    0.000    0.000    0.000 task_1.py:91(generate_row2) - 100
# 1001    0.000    0.000    0.000    0.000 task_1.py:91(generate_row2) - 1000
# 10001    0.004    0.000    0.004    0.000 task_1.py:91(generate_row2) - 10000

# По всем показателям лучший вариант 1 - цикл
