"""
Задача считается решённой, если в ней использована как минимум одна коллекция
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict
from collections import deque


def addition_hex(num1, num2):
    # функция сложения hex, по принципу сложения в столбик
    hx1 = deque(num1.upper())
    hx2 = deque(num2.upper())
    hx1.reverse()
    hx2.reverse()
    if len(hx2) > len(hx1):
        hx1, hx2 = hx2, hx1
    res = deque()
    remainder = 0
    i = 0
    while i <= len(hx1):
        if len(hx2) > i:
            digit = (hex_to_dec[hx1[i]] + hex_to_dec[hx2[i]] + remainder) % 16
            res.append(dec_to_hex[digit])
            remainder = (hex_to_dec[hx1[i]] + hex_to_dec[hx2[i]] + remainder) // 16
        elif len(hx1) > i:
            digit = (hex_to_dec[hx1[i]] + remainder) % 16
            res.append(dec_to_hex[digit])
            remainder = (hex_to_dec[hx1[i]] + remainder) // 16
        elif remainder != 0:
            res.append(dec_to_hex[remainder])
        i += 1
    res.reverse()
    return ''.join(list(res))


def my_dex(string):
    # перевод hex в dec
    dex = 0
    num = deque(string.upper())
    num.reverse()
    for i in range(len(num)):
        dex += hex_to_dec[num[i]] * 16 ** i
    return dex

# Определение словарей соответствия чисел HEX->DEC
signs = '0123456789ABCDEF'
hex_to_dec = defaultdict(int)
counter = 0
for key in signs:
    hex_to_dec[key] += counter
    counter += 1
# DEC->HEX
dec_to_hex = dict(zip(hex_to_dec.values(), hex_to_dec.keys()))

print('HEX калькулятор.')
op = None
while True:
    op = input('Введите "+" для сложения, "*" для умножения, "0" выход: ')
    if op == '0':
        break

    num1 = input('Введите 1е число: ')
    num2 = input('Введите 2е число: ')
    if op == '+':
        print(f'{num1.upper()} + {num2.upper()} = {addition_hex(num1, num2)}')
    elif op == '*':
        # переводим одно из чисел в dec и складываем второе число dec количество раз
        res = '0'
        for i in range(my_dex(num2)):
            res = addition_hex(res, num1)
        print(f'{num1.upper()} * {num2.upper()} = {res}')
    else:
        print('Некорректный ввод.')
