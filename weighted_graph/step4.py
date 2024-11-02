import heapq
from collections import defaultdict
import sys


def min_travel_time(n, m, buses):
    # Создаём граф для хранения рейсов между деревнями
    graph = defaultdict(list)
    for start_village, departure_time, end_village, arrival_time in buses:
        graph[start_village].append((departure_time, end_village, arrival_time))

    # Инициализация очереди с приоритетом и посещенных узлов
    pq = []
    visited = defaultdict(lambda: float('inf'))

    # Находим минимальное время отправления из деревни n
    initial_departures = [d for d, _, _ in graph[n]]
    if not initial_departures:
        return -1
    min_departure = min(initial_departures)

    # Начинаем с минимального времени отправления из деревни n
    heapq.heappush(pq, (min_departure, n))
    visited[n] = min_departure

    while pq:
        current_time, current_village = heapq.heappop(pq)

        # Если достигли целевой деревни, возвращаем результат
        if current_village == m:
            return current_time - min_departure

        # Если текущее время больше уже посещенного времени для этой деревни, пропускаем
        if current_time > visited[current_village]:
            continue

        # Проходим по всем доступным рейсам из текущей деревни
        for departure_time, next_village, arrival_time in graph[current_village]:
            if current_time <= departure_time:
                total_time = arrival_time  # Учитываем время прибытия в следующую деревню

                # Если нашли более короткое время до следующей деревни, обновляем очередь и visited
                if total_time < visited[next_village]:
                    visited[next_village] = total_time
                    heapq.heappush(pq, (total_time, next_village))

    # Если не удалось добраться до целевой деревни, возвращаем -1
    return -1


# Чтение входных данных
if __name__ == "__main__":
    input_data = sys.stdin.read().strip().splitlines()

    if not input_data:
        sys.exit(1)

    # Первая строка содержит n и m
    first_line = input_data[0].split()
    n = int(first_line[0])
    m = int(first_line[1])

    buses = []

    # Остальные строки содержат рейсы автобусов
    for line in input_data[1:]:
        if line.strip():
            buses.append(list(map(int, line.split())))

    if not buses:
        print(-1)
        sys.exit(1)

    # Вызов функции и вывод результата
    result = min_travel_time(n, m, buses)
    print(result)
