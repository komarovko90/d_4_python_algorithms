from collections import deque
"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он
дополнительно возвращал список вершин, которые необходимо обойти.
"""

g = [
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0]
]

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    current = start

    cost[current] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[current] = True

        for i, vertex in enumerate(graph[current]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[current]:
                    cost[i] = vertex + cost[current]
                    parent[i] = current

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                current = i

    ways = [deque([]) for _ in range(length)]
    for i in range(length):
        if i == start:
            ways[i].appendleft(start)
        elif parent[i] != -1:
            finish = i
            ways[i].append(finish)
            while parent[finish] != start:
                ways[i].appendleft(parent[finish])
                finish = parent[finish]
            ways[i].appendleft(start)

    return cost, ways

s = int(input('Стартовая вершина: '))
cost, ways = dijkstra(g, s)
for vertex, c in enumerate(cost):
    print(f'Вершина {vertex}: cтоимость - {c}, kратчайший путь - {list(ways[vertex])}')
