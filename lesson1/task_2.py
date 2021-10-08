'''
2. По введенным пользователем координатам двух точек вывести уравнение
прямой вида y = kx + b, проходящей через эти точки.
'''

print('Введите координаты [x,y] двух точек.')
x1 = int(input('Введите координату x первой точки: '))
y1 = int(input('Введите координату y первой точки: '))

x2 = int(input('Введите координату x второй точки: '))
y2 = int(input('Введите координату y второй точки: '))

if x1 == x2 & y1 == y2:
    print('Нет решения')
elif x1 == x2:
    print(f'x = {x1}')
elif y1 == y2:
    print(f'y = {y1}')
else:
    k = (y2-y1)/(x2-x1)
    b = y2-k*x2
    if b >= 0:
        sign = '+'
    else:
        sign = ''
    print(f'y={k}x{sign}{b}')