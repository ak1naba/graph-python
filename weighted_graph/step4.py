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
    # Начинаем с первого рейса: текущее время - это время отправления первого рейса
    heapq.heappush(pq, (0, n))  # (время, деревня)
    visited = defaultdict(lambda: float('inf'))
    visited[n] = 0

    while pq:
        current_time, current_village = heapq.heappop(pq)

        # Логи для отладки
        print(f"Текущая деревня: {current_village}, текущее время: {current_time}")

        # Если мы достигли целевой деревни
        if current_village == m:
            return current_time

        # Если текущее время больше уже посещенного времени для этой деревни
        if current_time > visited[current_village]:
            continue

        # Обработка всех рейсов из текущей деревни
        for departure_time, next_village, arrival_time in graph[current_village]:
            print(
                f"Проверяем рейс: {current_village} -> {next_village}, время отправления: {departure_time}, время прибытия: {arrival_time}")
            if current_time <= departure_time:  # Можно успеть на автобус
                wait_time = departure_time - current_time  # Время ожидания до отправления
                total_time = current_time + wait_time + (arrival_time - departure_time)

                print(f"Время ожидания: {wait_time}, общее время до {next_village}: {total_time}")

                if total_time < visited[next_village]:  # Проверяем лучшее время для следующей деревни
                    visited[next_village] = total_time
                    heapq.heappush(pq, (total_time, next_village))
                    print(f"Обновлено время для {next_village}: {total_time}")

    return -1


# Чтение входных данных
if __name__ == "__main__":
    input_data = sys.stdin.read().strip().splitlines()

    if not input_data:
        print("Нет входных данных.")
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
        print("Нет рейсов автобусов.")
        sys.exit(1)

    # Вызов функции и вывод результата
    result = min_travel_time(n, m, buses)
    print("Минимальное время:", result)