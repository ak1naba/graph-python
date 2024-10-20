from collections import deque


def bfs_shortest_path(graph, start, goal):
    queue = deque([start])  # очередь для BFS
    visited = {start}  # множество посещённых вершин
    parent = {start: None}  # словарь для хранения предшественников

    while queue:
        current_vertex = queue.popleft()

        if current_vertex == goal:
            break

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_vertex
                queue.append(neighbor)

    # Восстановление пути от goal до start
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]

    path.reverse()  # переворачиваем путь, чтобы получить его от start до goal
    return path


def main():
    # Чтение входных данных
    first_line = input().strip().split()
    N, M, S, F = map(int, first_line)

    graph = {i: [] for i in range(N)}

    for _ in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)  # неориентированный граф

    # Поиск кратчайшего пути
    shortest_path = bfs_shortest_path(graph, S, F)

    # Вывод результата
    print(" ".join(map(str, shortest_path)))


main()