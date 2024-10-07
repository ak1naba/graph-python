def dfs(graph, u, visited, disc, low, parent, bridges):
    visited[u] = True
    disc[u] = low[u] = dfs.time
    dfs.time += 1

    for v in graph[u]:
        if not visited[v]:  # Если v не посещена
            parent[v] = u
            dfs(graph, v, visited, disc, low, parent, bridges)

            # Проверяем минимальное время входа для u
            low[u] = min(low[u], low[v])

            # Если минимальное время входа для v больше времени входа для u,
            # то (u, v) является мостом
            if low[v] > disc[u]:
                bridges.append((u, v))

        elif v != parent[u]:  # Обновляем low[u] для обратного ребра
            low[u] = min(low[u], disc[v])


def find_bridges(n, edges):
    graph = {i: [] for i in range(n)}

    # Заполняем граф
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    disc = [float('inf')] * n
    low = [float('inf')] * n
    parent = [-1] * n
    bridges = []

    # Инициализируем время входа
    dfs.time = 0

    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, disc, low, parent, bridges)

    return len(bridges)


# Ввод данных
N, M = map(int, input().strip().split())
edges = [tuple(input().strip().split()) for _ in range(M)]

# Создаем отображение от символов к индексам
char_to_index = {}
index = 0

for u, v in edges:
    if u not in char_to_index:
        char_to_index[u] = index
        index += 1
    if v not in char_to_index:
        char_to_index[v] = index
        index += 1

# Преобразуем пары в индексы
indexed_edges = [(char_to_index[u], char_to_index[v]) for u, v in edges]

# Проверка количества мостов в графе
result = find_bridges(len(char_to_index), indexed_edges)
print(result)