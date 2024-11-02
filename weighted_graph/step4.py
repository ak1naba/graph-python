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

    # Запускаем поиск от деревни n с минимальным временем отправления
    initial_departure = min((d for d, _, _ in graph[n]), default=None)
    if initial_departure is None:
        return -1

    # Добавляем минимальное время отправления как стартовое
    heapq.heappush(pq, (initial_departure, n))
    visited[n] = initial_departure

    while pq:
        current_time, current_village = heapq.heappop(pq)

        # Если достигли целевой деревни, возвращаем время поездки
        if current_village == m:
            return current_time - initial_departure

        # Обработка всех рейсов из текущей деревни
        for departure_time, next_village, arrival_time in graph[current_village]:
            if current_time <= departure_time:  # Можно успеть на рейс
                total_time = arrival_time  # Новое время до прибытия в следующую деревню

                # Обновляем время, если нашли более короткий путь
                if total_time < visited[next_village]:
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
