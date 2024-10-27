from collections import defaultdict, deque
import sys


def solve():
    # Чтение всех данных из ввода
    input_data = sys.stdin.read().strip().splitlines()

    # Чтение n и m
    n, m = map(int, input_data[0].strip().split())

    # Создаем граф
    graph = defaultdict(list)

    # Чтение информации о рейсах
    for line in input_data[1:]:
        dep_village, dep_time, arr_village, arr_time = map(int, line.strip().split())
        # Добавляем рейс в граф
        graph[dep_village].append((dep_time, arr_village, arr_time))

    # Список для хранения минимального времени до каждой деревни
    min_time = [float('inf')] * (n + 1)
    min_time[n] = 0  # Время в деревне n равно 0

    # Очередь для BFS: (текущее время, текущая деревня)
    queue = deque([(0, n)])  # Начинаем с деревни n и времени 0

    while queue:
        current_time, current_village = queue.popleft()

        # Проходим по всем рейсам из текущей деревни
        for dep_time, arr_village, arr_time in graph[current_village]:
            if current_time <= dep_time:  # Можно выехать на рейс
                if arr_time < min_time[arr_village]:  # Если достигли деревни быстрее
                    min_time[arr_village] = arr_time
                    queue.append((arr_time, arr_village))

    # Проверяем минимальное время до деревни m
    answer = min_time[m]
    print(answer if answer != float('inf') else -1)


# Запуск решения
solve()
