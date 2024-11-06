import heapq
from collections import defaultdict
import sys


def min_travel_time(start, end, buses):
    # Создаём граф для хранения рейсов между деревнями
    graph = defaultdict(list)
    for start_village, departure_time, end_village, arrival_time in buses:
        graph[start_village].append((departure_time, end_village, arrival_time))

    # Инициализация очереди с приоритетом и посещенных узлов
    pq = []
    visited = defaultdict(lambda: float('inf'))

    # Добавляем в очередь все рейсы из начальной деревни `start`
    for departure_time, next_village, arrival_time in graph[start]:
        heapq.heappush(pq, (arrival_time, next_village, departure_time))
        visited[(next_village, arrival_time)] = arrival_time

    # Начинаем поиск пути
    while pq:
        current_time, current_village, start_time = heapq.heappop(pq)

        # Если достигли целевой деревни, возвращаем результат
        if current_village == end:
            return current_time - start_time

        # Проходим по всем рейсам из текущей деревни
        for departure_time, next_village, arrival_time in graph[current_village]:
            # Проверяем, можем ли мы воспользоваться этим рейсом после текущего времени
            if current_time <= departure_time:
                # Если нашли более короткое время до следующей деревни, обновляем очередь и visited
                if arrival_time < visited[(next_village, arrival_time)]:
                    visited[(next_village, arrival_time)] = arrival_time
                    heapq.heappush(pq, (arrival_time, next_village, start_time))

    # Если не удалось добраться до целевой деревни, возвращаем -1
    return -1


# Чтение входных данных
if __name__ == "__main__":
    input_data = sys.stdin.read().strip().splitlines()

    # Первая строка содержит n и m
    first_line = input_data[0].split()
    start = int(first_line[0])
    end = int(first_line[1])

    buses = []

    # Остальные строки содержат рейсы автобусов
    for line in input_data[1:]:
        if line.strip():
            buses.append(list(map(int, line.split())))

    # Вызов функции и вывод результата
    result = min_travel_time(start, end, buses)
    print(result)
