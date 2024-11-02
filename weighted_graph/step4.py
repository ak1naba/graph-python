import heapq
from collections import defaultdict
import sys


def min_travel_time(n, m, buses):
    graph = defaultdict(list)

    # Заполнение графа
    for start_village, departure_time, end_village, arrival_time in buses:
        graph[start_village].append((departure_time, end_village, arrival_time))

    # Инициализация очереди с приоритетом и посещенных узлов
    pq = []
    visited = defaultdict(lambda: float('inf'))

    # Найдём минимальное время отправления из деревни n
    min_departure = min((d for d, _, _ in graph[n]), default=None)
    if min_departure is None:
        return -1

    # Начинаем с минимального времени отправления первого рейса из деревни n
    heapq.heappush(pq, (min_departure, n))  # (время, деревня)
    visited[n] = min_departure

    while pq:
        current_time, current_village = heapq.heappop(pq)

        # Если мы достигли целевой деревни
        if current_village == m:
            return current_time - min_departure  # Вернём итоговое время поездки

        # Если текущее время больше уже посещенного времени для этой деревни
        if current_time > visited[current_village]:
            continue

        # Обработка всех рейсов из текущей деревни
        for departure_time, next_village, arrival_time in graph[current_village]:
            if current_time <= departure_time:  # Можно успеть на автобус
                total_time = arrival_time  # Сразу задаём общее время до прибытия

                if total_time < visited[next_village]:  # Проверяем лучшее время для следующей деревни
                    visited[next_village] = total_time
                    heapq.heappush(pq, (total_time, next_village))

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
        if line.strip():  # Проверяем на пустую строку
            buses.append(list(map(int, line.split())))

    if not buses:
        print(-1)
        sys.exit(1)

    # Вызов функции и вывод результата
    result = min_travel_time(n, m, buses)
    print(result)
