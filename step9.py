from collections import defaultdict, deque


def topological_sort(n, edges):
    # Создаем граф и массив для хранения входной степени
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    # Заполняем граф и считаем входные степени
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Инициализируем очередь с вершинами с нулевой входной степенью
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)

        # Уменьшаем входную степень соседей
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Если количество отсортированных вершин меньше N, значит есть цикл
    if len(sorted_order) != n:
        return "No", []

    return "Yes", sorted_order


# Ввод данных
N, M = map(int, input().strip().split())
edges = [tuple(map(int, input().strip().split())) for _ in range(M)]

# Проверка возможности построения студентов по росту
result, order = topological_sort(N, edges)
print(result)
if result == "Yes":
    print(" ".join(map(str, order)))