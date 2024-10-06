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
pairs = [tuple(map(int, input().strip().split())) for _ in range(M)]

# Проверка возможности рассадки ОВП
result = can_seat_vips(N, M, pairs)
print(result)