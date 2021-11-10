import random
from collections import deque

"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

def graph_generation(cnt_vertex):
    g = []
    for i in range(cnt_vertex):
        vertex = []
        while len(vertex) == 0:     # для исключения случаев, когда рандом вернул все нули
            for j in range(cnt_vertex):     # заполняем случайными связями, кроме диагонали
                num = random.randint(0, 1)
                if i != j and num == 1:
                    vertex.append(num * j)
        g.append(vertex)
    return g


def dfs(graph, start, finish, way, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    if start == finish:
        way.append(start)
        return True
    for vertex in graph[start]:
        if vertex not in visited:
            res = dfs(graph, vertex, finish, way, visited)
            if res:
                way.appendleft(start)
                return True
    return False


def dfs_way(graph, start, finish):
    way = deque([])
    res = dfs(graph, start, finish, way)
    if res:
        return f'Путь из {start} в {finish}: {list(way)}'
    else:
        return f'Из вершины {start} нельяз попасть в вершину {finish}'


n = int(input('Количество вершин: '))
gr = graph_generation(n)
print('Случайный граф')
print(*gr, sep='\n')
print('*' * 50)
s = int(input('Вершина старта: '))
f = int(input('Вершина финиша: '))
print(dfs_way(gr, s, f))
