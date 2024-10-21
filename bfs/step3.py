from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start: 0}  # хранит расстояние от стартовой вершины
    farthest_vertex = start
    max_distance = 0

    while queue:
        current_vertex = queue.popleft()
        current_distance = visited[current_vertex]

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited[neighbor] = current_distance + 1
                queue.append(neighbor)

                # Обновляем максимальное расстояние и соответствующую вершину
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    farthest_vertex = neighbor

    return farthest_vertex, max_distance

def main():
    # Чтение входных данных
    first_line = input().strip().split()
    N, M = map(int, first_line)

    graph = {i: [] for i in range(N)}

    for _ in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)  # неориентированный граф

    # Первый BFS для нахождения самой удалённой вершины от произвольной
    arbitrary_start = 0
    farthest_from_start, _ = bfs(graph, arbitrary_start)

    # Второй BFS для нахождения самой удалённой вершины от найденной
    farthest_vertex, _ = bfs(graph, farthest_from_start)

    # Вывод результата в порядке возрастания
    result = sorted([farthest_from_start, farthest_vertex])
    print(result[0], result[1])

main()