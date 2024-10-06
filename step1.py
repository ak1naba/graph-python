def dfs(node, visited, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)


def count_connected_components(n, edges):
    graph = {i: [] for i in range(n)}

    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    component_count = 0

    for node in range(n):
        if node not in visited:
            dfs(node, visited, graph)
            component_count += 1

    return component_count


# Ввод данных
try:
    n, m = map(int, input().strip().split())
    edges = []

    # Словарь для отображения вершин
    vertex_map = {}
    current_index = 0

    for _ in range(m):
        u, v = input().strip().split()

        # Добавление вершин в словарь
        if u not in vertex_map:
            vertex_map[u] = current_index
            current_index += 1
        if v not in vertex_map:
            vertex_map[v] = current_index
            current_index += 1

        edges.append((vertex_map[u], vertex_map[v]))

    # Подсчет компонент связности
    result = count_connected_components(current_index, edges)
    print(result)

except ValueError:
    print("Ошибка: убедитесь, что вводите только целые числа или корректные символы.")