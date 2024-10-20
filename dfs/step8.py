def dfs(graph, v, visited, stack):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(v)


def dfs_transposed(graph, v, visited):
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs_transposed(graph, neighbor, visited)


def count_strongly_connected_components(n, edges):
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

    visited = set()
    stack = []

    # Первый проход DFS для заполнения стека
    for i in range(n):
        if i not in visited:
            dfs(graph, i, visited, stack)

    # Второй проход DFS на транспонированном графе
    visited.clear()
    component_count = 0

    while stack:
        v = stack.pop()
        if v not in visited:
            dfs_transposed(transposed_graph, v, visited)
            component_count += 1

    return component_count


# Ввод данных
N, M = map(int, input().strip().split())
edges = [tuple(input().strip().split()) for _ in range(M)]

# Подсчет количества компонент сильной связности
result = count_strongly_connected_components(N, edges)
print(result)