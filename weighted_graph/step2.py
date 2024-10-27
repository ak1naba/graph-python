import heapq


def dijkstra(n, costs, graph):
    min_costs = [float('inf')] * n
    min_costs[0] = costs[0]  # Начальная стоимость
    pq = [(costs[0], 0)]  # (стоимость, город)

    while pq:
        current_cost, current_city = heapq.heappop(pq)

        # Если достигли последнего города
        if current_city == n - 1:
            return current_cost

        # Если текущая стоимость больше минимальной, пропускаем
        if current_cost > min_costs[current_city]:
            continue

        # Проходим по всем соседям текущего города
        for neighbor in graph[current_city]:
            new_cost = current_cost + costs[neighbor]  # Учитываем налог на вход в соседний город
            if new_cost < min_costs[neighbor]:
                min_costs[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return -1 if min_costs[n - 1] == float('inf') else min_costs[n - 1]


def main():
    n = int(input())  # Ввод количества городов
    costs = list(map(int, input().split()))  # Ввод стоимости за посещение каждого города
    m = int(input())  # Ввод количества дорог

    # Создание графа
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)  # Индексы городов начинаются с 0
        graph[v - 1].append(u - 1)

    result = dijkstra(n, costs, graph)
    print(result)


if __name__ == "__main__":
    main()
