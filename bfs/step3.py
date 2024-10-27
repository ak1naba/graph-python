from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start: 0}
    farthest_vertex = start

    while queue:
        current_vertex = queue.popleft()

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                visited[neighbor] = visited[current_vertex] + 1
                queue.append(neighbor)
                farthest_vertex = neighbor  # Обновляем самую удалённую вершину

    # Возвращаем самую удалённую вершину и её расстояние
    return farthest_vertex, visited[farthest_vertex]

def main():
    N, M = map(int, input().strip().split())
    graph = {i: [] for i in range(N)}

    for _ in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    # Первый BFS: найти самую удалённую вершину от 0
    farthest_from_start, _ = bfs(graph, 0)

    # Второй BFS: найти самую удалённую вершину от найденной
    farthest_vertex, _ = bfs(graph, farthest_from_start)

    # Выводим вершины в порядке возрастания
    result = sorted([farthest_from_start, farthest_vertex])
    print(result[0], result[1])

# Запуск основной функции
main()
