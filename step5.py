def bfs_check_bipartite(graph, start, color):
    queue = [start]
    color[start] = 0  # Начинаем с одного цвета

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if color[neighbor] == -1:  # Если сосед еще не окрашен
                color[neighbor] = 1 - color[node]  # Окрашиваем в противоположный цвет
                queue.append(neighbor)
            elif color[neighbor] == color[node]:  # Если сосед имеет тот же цвет
                return False  # Граф не двудолен

    return True


def can_seat_vips(n, m, pairs):
    graph = {i: [] for i in range(n)}

    # Заполняем граф
    for u, v in pairs:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n  # -1 означает, что вершина еще не окрашена

    for i in range(n):
        if color[i] == -1:  # Если вершина еще не окрашена
            if not bfs_check_bipartite(graph, i, color):
                return "NO"

    return "YES"


# Ввод данных
N, M = map(int, input().strip().split())
pairs = [tuple(input().strip().split()) for _ in range(M)]

# Создаем отображение от символов к индексам
char_to_index = {}
index = 0

for u, v in pairs:
    if u not in char_to_index:
        char_to_index[u] = index
        index += 1
    if v not in char_to_index:
        char_to_index[v] = index
        index += 1

# Преобразуем пары в индексы
indexed_pairs = [(char_to_index[u], char_to_index[v]) for u, v in pairs]

# Проверка возможности рассадки ОВП
result = can_seat_vips(len(char_to_index), M, indexed_pairs)
print(result)