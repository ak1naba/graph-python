def find_cycle_dfs(graph, v, visited, parent, path):
    visited[v] = True
    path.append(v)

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if find_cycle_dfs(graph, neighbor, visited, v, path):
                return True
        elif neighbor != parent:
            path.append(neighbor)
            return True

    path.pop()
    return False


def find_shortest_cycle(n, edges):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    shortest_cycle = None

    for start in range(n):
        visited = [False] * n
        path = []

        if find_cycle_dfs(graph, start, visited, -1, path):
            cycle_start = path[-1]
            cycle = []
            cycle_found = False

            for node in reversed(path):
                cycle.append(node)
                if node == cycle_start and cycle_found:
                    break
                if node == cycle_start:
                    cycle_found = True

            unique_cycle = sorted(set(cycle))
            if shortest_cycle is None or len(unique_cycle) < len(shortest_cycle):
                shortest_cycle = unique_cycle

    return shortest_cycle


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = find_shortest_cycle(n, edges)

if result:
    print(" ".join(map(str, result)))
else:
    print("Цикл не найден")