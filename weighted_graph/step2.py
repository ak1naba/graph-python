import sys
import heapq


def solve():
    # Чтение числа городов N
    n = int(input().strip())

    # Чтение стоимости посещения каждого города
    taxes = list(map(int, input().strip().split()))

    # Чтение количества дорог M
    m = int(input().strip())

    # Создаем граф в виде списка смежности
    graph = [[] for _ in range(n)]

    # Чтение дорог и построение графа
    for _ in range(m):
        u, v = map(int, input().strip().split())
        # Приводим города к нумерации от 0 для удобства (Python индексация с 0)
        u -= 1
        v -= 1
        # Дорога добавляется в обе стороны, так как граф неориентированный
        graph[u].append(v)
        graph[v].append(u)

    # Алгоритм Дейкстры для поиска минимальной стоимости маршрута
    def dijkstra(start, end):
        # Массив для хранения минимальной стоимости до каждого города
        min_cost = [float('inf')] * n
        min_cost[start] = taxes[start]

        # Очередь с приоритетом (куча)
        pq = [(taxes[start], start)]  # (стоимость, город)

        while pq:
            current_cost, u = heapq.heappop(pq)

            # Если текущая стоимость уже больше известной, пропускаем
            if current_cost > min_cost[u]:
                continue

            # Проходим по соседям текущего города
            for v in graph[u]:
                new_cost = current_cost + taxes[v]
                if new_cost < min_cost[v]:
                    min_cost[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        # Возвращаем минимальную стоимость до конечного города без учета двойного старта
        return min_cost[end] - taxes[start]

    # Запуск алгоритма Дейкстры из 1-го города в N-й
    result = dijkstra(0, n - 1)

    # Если до конечного города добраться нельзя, выводим -1
    print(result if result != float('inf') else -1)


# Запуск решения
solve()
