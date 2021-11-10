"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


N = int(input('Введите количество друзей: '))
g = []
is_visited = [False] * N

# Строим списки смежности
fr = 0
while fr < N-1:     # проходим всех друзей, кроме последнего, так с ним все здороваются сами
    vertexes = []
    is_visited[fr] = True   # исключаем предыдущего, так как он поздоровался со всеми
    for i in range(N):
        if fr != i and not is_visited[i]:
            vertexes.append(i)
    g.append(vertexes)
    fr += 1

print('Получившийся граф')
print(*g, sep='\n')

print('*' * 20)
sum_ = 0
for j in g:
    sum_ += len(j)
print(f'Количество рукопожатий: {sum_}')
