def dfs(node, visited, graph):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)


def is_tree(n, m, edges):
    if m != n - 1:
        return False  # Условие для дерева: количество рёбер должно быть N - 1

    graph = {i: [] for i in range(n)}
    vertex_map = {}
    current_index = 0

    # Создаем граф и отображаем вершины
    for u, v in edges:
        if u not in vertex_map:
            vertex_map[u] = current_index
            current_index += 1
        if v not in vertex_map:
            vertex_map[v] = current_index
            current_index += 1

        graph[vertex_map[u]].append(vertex_map[v])
        graph[vertex_map[v]].append(vertex_map[u])

    visited = set()

    # Запускаем DFS с первой вершины
    dfs(0, visited, graph)

    # Проверяем, все ли вершины были посещены
    return len(visited) == n


# Ввод данных
N, M = map(int, input().strip().split())
edges = [input().strip().split() for _ in range(M)]

# Проверка, является ли граф деревом
if is_tree(N, M, edges):
    print("YES")
else:
    print("NO")