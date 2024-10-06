def dfs(graph, v, visited):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def is_strongly_connected(n, edges):
    # Создаем граф и его транспонированную версию
    graph = {i: [] for i in range(n)}
    transposed_graph = {i: [] for i in range(n)}

    vertex_map = {}
    current_index = 0

    for u, v in edges:
        if u not in vertex_map:
            vertex_map[u] = current_index
            current_index += 1
        if v not in vertex_map:
            vertex_map[v] = current_index
            current_index += 1

        graph[vertex_map[u]].append(vertex_map[v])
        transposed_graph[vertex_map[v]].append(vertex_map[u])

    # Проверяем достижимость из первой вершины
    visited = set()
    dfs(graph, 0, visited)

    if len(visited) != n:
        return "NO"

    # Проверяем достижимость из первой вершины в транспонированном графе
    visited.clear()
    dfs(transposed_graph, 0, visited)

    if len(visited) != n:
        return "NO"

    return "YES"


# Ввод данных
N, M = map(int, input().strip().split())
edges = [tuple(input().strip().split()) for _ in range(M)]

# Проверка на сильную связность орграфа
result = is_strongly_connected(N, edges)
print(result)