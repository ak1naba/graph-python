from collections import deque


def bfs_shortest_cycle(graph, start):
    queue = deque([start])
    visited = {start: None}  # хранит предшественников вершин

    while queue:
        current_vertex = queue.popleft()

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited[neighbor] = current_vertex
                queue.append(neighbor)
            elif neighbor != visited[current_vertex]:  # найден цикл
                return reconstruct_cycle(visited, current_vertex, neighbor)

    return None


def reconstruct_cycle(visited, start, end):
    cycle = []
    cycle.append(end)

    # Восстанавливаем путь от конечной вершины до стартовой
    while start is not None:
        cycle.append(start)
        start = visited[start]

    cycle.reverse()  # Переворачиваем для правильного порядка
    return cycle


def main():
    # Чтение входных данных
    first_line = input().strip().split()
    N, M = map(int, first_line)

    graph = {i: [] for i in range(N)}

    for _ in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)  # неориентированный граф

    # Поиск кратчайшего цикла
    shortest_cycle = None
    for vertex in range(N):
        shortest_cycle = bfs_shortest_cycle(graph, vertex)
        if shortest_cycle:
            break

    # Вывод результата в порядке возрастания
    if shortest_cycle:
        print(" ".join(map(str, sorted(shortest_cycle))))


main()