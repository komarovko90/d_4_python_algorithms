"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число. Проанализировать скорость и
сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй - классический способ проверки числа на простоту
"""

import cProfile

def test_prime_num(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

# 1 вариант Решето Эратосфена
def func_sieve (n):
    size = max(3, n**2)
    result = [2]  # массив для простых чисел, первое простое 2 вводим вручную
    sieve = [i for i in range(size)]    # массив для чисел, число соответствует индексу
    sieve[1] = 0    # единицу обнуляем вручную

    i = 0   # индекс текущего простого числа
    while i < n:
        p = result[i]   # запоминаем текущее простое число
        i += 1

        for j in range(p*2, size, p):  # обнуляем все кратные ему числа в массиве
            if sieve[j] != 0:
                sieve[j] = 0

        while p+1 < size:  # ищем следующее ненулевое число
            if sieve[p+1] != 0:
                break
            p += 1

        if p + 1 >= size:   # если выйдем за границы, расширяем массив
            for k in range(size, size*2):
                sieve.append(k)
            size *= 2
            result = [2]    # возвращаемся к начальной стадии просеивания
            i = 0
        else:
            result.append(p+1)  # иначе добавляем значение в массив простых чисел
    return result[n]

# вариант 1
# python -m timeit -n 5 -s "import task_2" "task_2.func_sieve(300)"

# .func_sieve(10)"
# 500 loops, best of 5: 26.7 usec per loop

# .func_sieve(100)"
# 500 loops, best of 5: 3.16 msec per loop

# unc_sieve(200)"
# 50 loops, best of 5: 13.4 msec per loop

# unc_sieve(300)"
# 50 loops, best of 5: 31.7 msec per loop

# nc_sieve(1000)"
# 5 loops, best of 5: 414 msec per loop


# cProfile.run('func_sieve(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.003    0.003    0.003    0.003 task_2.py:19(func_sieve) 100
# 1    0.026    0.026    0.032    0.032 task_2.py:19(func_sieve) 300
# 1    0.350    0.350    0.424    0.424 task_2.py:19(func_sieve) 1000

# 2 вариант классический
def func_classic_prime (n):
    prime = 2   # первое простое число
    i = 1   # индекс для поиска n-го простого
    num = 3     # доп параметр, для того, чтобы проверять только нечетные числа
    while i <= n:   # пока не найдем n е простое число
        flag = False    # флаг для выхода из цикла
        while True:     # цикл проверки числа на деление без остатка
            for k in range(2, num):
                if num % k == 0:
                    flag = True
                    break
            if flag:    # если число не является простым
                num += 2    # назначаем новое для проверки
                flag = False    # снимаем флаг
            else:
                i += 1      # нашли простое число
                prime = num     # сохраняем его
                num += 2    # назначаем новое для следующего цикла
                break
    return prime

# вариант 2
# python -m timeit -n 5 -s "import task_2" "task_2.func_classic_prime(100)"

# nc_classic_prime(100)"
# 5 loops, best of 5: 1.73 msec per loop

# nc_classic_prime(300)"
# 5 loops, best of 5: 25.6 msec per loop

# nc_classic_prime(1000)"
# 5 loops, best of 5: 418 msec per loop

# cProfile.run('func_classic_prime(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.002    0.002    0.002    0.002 task_2.py:75(func_classic_prime)
# 1    0.034    0.034    0.034    0.034 task_2.py:75(func_classic_prime)
# 1    0.441    0.441    0.441    0.441 task_2.py:75(func_classic_prime)


# test_prime_num(func_classic_prime)

# Оба алгоритма показали примерно одинаковую скорость вычислений.
# Разница незначительна. Однако второй метод занимает меньше памяти,
# так как не хранит массив с простыми числами