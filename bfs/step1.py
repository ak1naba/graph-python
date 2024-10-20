from collections import deque


def bfs_shortest_path(graph, start, goal):
    queue = deque([(start, 0)])  # (текущая вершина, расстояние от начальной)
    visited = set()  # множество посещённых вершин

    while queue:
        current_vertex, current_distance = queue.popleft()

        if current_vertex == goal:
            return current_distance

        if current_vertex not in visited:
            visited.add(current_vertex)
            for neighbor in graph[current_vertex]:
                queue.append((neighbor, current_distance + 1))

    return -1  # если путь не найден


def main():
    # Чтение входных данных
    first_line = input().strip().split()
    N, M, A, B = map(int, first_line)

    graph = {i: [] for i in range(N)}

    for _ in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)  # неориентированный граф

    # Поиск кратчайшего пути
    shortest_distance = bfs_shortest_path(graph, A, B)
    print(shortest_distance)


## Сделана обработка ошибки на отсвутвие связи, ответ будет -1