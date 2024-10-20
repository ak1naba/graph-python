def dfs(node, parent, visited, graph):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node, visited, graph):
                return True
        elif neighbor != parent:
            return True

    return False


def has_cycle(n, edges):
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

    # Проверяем наличие цикла для каждой компоненты связности
    for node in range(n):
        if node not in visited:
            if dfs(node, None, visited, graph):
                return True

    return False


# Ввод данных
N, M = map(int, input().strip().split())
edges = [input().strip().split() for _ in range(M)]

# Проверка наличия цикла
if has_cycle(N, edges):
    print("YES")
else:
    print("NO")