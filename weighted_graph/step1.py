import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если мы уже нашли более короткий путь к текущей вершине, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(n):
            weight = graph[current_vertex][neighbor]
            if weight > 0:  # Если есть ребро
                distance = current_distance + weight

                # Если найден более короткий путь к соседней вершине
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end] if distances[end] != float('inf') else -1

# Чтение входных данных
def main():
    first_line = input()
    n, start, end = map(int, first_line.split())
    start -= 1  # Приводим к индексу массива
    end -= 1    # Приводим к индексу массива

    # Создание матрицы смежности
    graph = []
    print()
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    # Вычисление кратчайшего расстояния
    result = dijkstra(graph, start, end)
    print(result)

if __name__ == "__main__":
    main()