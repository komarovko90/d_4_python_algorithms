'''
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или
меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
'''

import random

cnt = 0
max_count = 10
number = random.randint(0, 100)
user_number = None

while number != user_number:
    cnt += 1
    if cnt > max_count:
        print ('Поражение.')
        break
    print(f'Попытка № {cnt}')
    user_number = int(input('Введите число: '))
    if number > user_number:
        print ('Ваше число  меньше.')
    elif number < user_number:
        print('Ваше число  больше.')
else:
    print ('Победа.')
