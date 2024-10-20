def dfs(graph, vertex, visited, stack, depth):
    global min_cycle_length
    visited[vertex] = True
    stack.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor in stack:  # Цикл найден
            cycle_length = depth - stack.index(neighbor) + 1  # +1 для включения начальной вершины
            min_cycle_length = min(min_cycle_length, cycle_length)
        elif not visited[neighbor]:
            dfs(graph, neighbor, visited, stack, depth + 1)

    stack.pop()  # Удаляем вершину из стека при возвращении

def main():
    global min_cycle_length
    min_cycle_length = float('inf')

    # Чтение входных данных
    first_line = input().strip().split()
    N, M = map(int, first_line)

    graph = {i: [] for i in range(N)}

    for _ in range(M):
        u, v = map(int, input().strip().split())
        graph[u].append(v)  # ориентированный граф

    # Поиск кратчайшего цикла
    for vertex in range(N):
        visited = [False] * N
        dfs(graph, vertex, visited, [], 0)

    # Вывод результата
    print(min_cycle_length)

main()