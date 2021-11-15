from collections import deque, Counter
"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""


class MyNode:
    """собственный класс узлов дерева"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def search(tree, letter):
    """Поиск в неупорядоченном бинарном дереве"""
    way = []

    def search_(graph, let):
        if graph.data == let:
            return True
        if graph.left is not None:
            way.append('0')
            if search_(graph.left, let):
                return True
        if graph.right is not None:
            way.append('1')
            if search_(graph.right, let):
                return True
        way.pop()
        return False

    if search_(tree, letter):
        return way
    else:
        return None


def Haffman(s_uncoded):
    """Функция кодирования строки"""
    s_counter = Counter(s_uncoded)  # Собираем словарь из встречающихся  букв и их количества
    sorted_deque = deque(sorted(s_counter.items(), key=lambda item: item[1]))   # сортируем словарь
    tree = None
    length = len(sorted_deque) - 1

    # собираем дерево
    for i in range(length):
        tree = MyNode(None,
                      left=sorted_deque[0][0] if isinstance(sorted_deque[0][0], MyNode) else MyNode(sorted_deque[0][0]),
                      right=sorted_deque[1][0] if isinstance(sorted_deque[1][0], MyNode) else MyNode(
                          sorted_deque[1][0]))
        new_el = tuple([tree, sorted_deque[0][1] + sorted_deque[1][1]])
        sorted_deque.popleft()
        sorted_deque.popleft()
        sorted_deque.appendleft(new_el)
        sorted_deque = deque(sorted(sorted_deque, key=lambda item: item[1]))

    dict_coded_str = {}
    # ищем по дереву буквы и сохраняем их коды
    for el in s_counter.keys():
        dict_coded_str[el] = ''.join(search(tree, el))

    return dict_coded_str

s = input('Введите строку для кодирования:')
# s = 'beep boop beer!'

dict_code = Haffman(s)
print('Закодированная строка:')
for char in s:
    print(dict_code[char], end=' ')

