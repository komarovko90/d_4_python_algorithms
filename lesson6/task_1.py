import sys

"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;

c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.

Для расчетов времени выпонения берем следующую задачу из урока 2:
    4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
    Количество элементов (n) вводится с клавиатуры.
"""

def test_series(func):
    lst = [0, 1, 0.5, 0.75, 0.625, 0.6875]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def show_size(*var_list):
    """
    Подсчитывает размер переменных из var_list
    """
    sum_ = 0
    for i in var_list:
        sum_ += sys.getsizeof(i)
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for xx in i.items():
                    sum += show_size(xx)
            elif not isinstance(i, str):
                for xx in i:
                    sum_ += show_size(xx)
    return sum_

print('Ряд чисел: 1, -0.5, 0.25, -0.125,…')
# 1 вариант - цикл
def sum_series(n):
    a = 1
    sum = 0
    for i in range(n):
        sum += a
        a /= (-2)
    print(f'<<<Задействовано {show_size(a, n, sum)} байт памяти>>>')
    return sum

# n=2
# print(f'Сумма n элементов ряда: {sum_series(n)}')

# 2 вариант - рекурсия
memory = 0  # глоюальная переменная для подсчета памяти в вывзываемой рекурсивной функции generate_row
def generate_row(n):
    global memory
    if n <= 1:
        memory += show_size(n)
        return n
    else:
        res = generate_row(n - 1) * (- 0.5)
        memory += show_size(res)
        return res

def sum_series2(n):
    global memory
    i = 0
    result = 0
    while i <= n:
        result += generate_row(i)
        i += 1
    print(f'<<<Задействовано {show_size(n, i, result) + memory} байт памяти>>>')
    return result

n=100
print(f'Сумма n элементов ряда: {sum_series2(n)}')

# 3 вариант - цикл со списком
def sum_series3(n):
    a = -2
    lst = []
    for i in range(n):
        a /= (-2)
        lst.append(a)
    print(f'<<<Задействовано {show_size(a, n, lst)} байт памяти>>>')
    return sum(lst)

# test_series(sum_series3)
# n=100
# print(f'Сумма n элементов ряда: {sum_series3(n)}')


# print(sys.version, sys.platform)
# Python: 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52)
# WIN: [MSC v.1928 64 bit (AMD64)] win32

"""
В 1 варианте здействовано 76 байт памяти. 
При этом на размер памяти не влияет количество элементов n.

Во 2м варианте при подсчете занимаемого местаисходил из утверждения, что рекурсивный вызов функции выполняется так же, 
как и любая другая функция. То есть каждый раз при ее вызове происходит выделение доп памяти.
В результате c рекурсивной функцией при n=10 занимает 1464 байт памяти, при n=100 - 121704 байт. 


В 3 варианте при n=10 занимает 476 байт памяти, при n=100 - 3372 байт. Так в данном варианте мы используем список, 
который увеличивается в зависимости от количества элементов в нем.

Самый оптимальный 1 вариант.
"""