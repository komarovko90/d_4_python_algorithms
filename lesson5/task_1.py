"""
Задача считается решённой, если в ней использована как минимум одна коллекция
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за четыре квартала для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple
from statistics import mean

Company = namedtuple('company', 'name profit_list profit_year')
n_company = int(input('Введите количество предприятий: '))

list_company = []
for i in range(n_company):
    name = input('Введите наименование компании: ')
    profit_list = []
    for j in range(4):
        profit_list.append(int(input(f'Введите доход за квартал Q{j+1}: ')))
    list_company.append(Company(name, profit_list, sum(profit_list)))

mean_profit = mean([i.profit_year for i in list_company])
print(f'Средняя прибыль по всем компаниям за год: {mean_profit:.1f}.')

print('Компании с прибылью меньше средней:')
for i in list_company:
    if i.profit_year < mean_profit:
        print(f'{i.name}: {i.profit_year}')

print('Компании с прибылью больше средней:')
for i in list_company:
    if i.profit_year >= mean_profit:
        print(f'{i.name}: {i.profit_year}')
