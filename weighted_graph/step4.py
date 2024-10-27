from collections import defaultdict, deque

def solve():
    # Чтение первой строки с начальной и конечной деревнями
    start_village, target_village = map(int, input().strip().split())

    # Граф для хранения рейсов: {деревня: [(время_выезда, след_деревня, время_прибытия)]}
    graph = defaultdict(list)

    # Чтение данных о рейсах
    while True:
        try:
            dep_village, dep_time, arr_village, arr_time = map(int, input().strip().split())
            graph[dep_village].append((dep_time, arr_village, arr_time))
        except EOFError:
            break  # Прерываем цикл, когда ввод заканчивается

    # Очередь для BFS: (текущая деревня, текущее время)
    queue = deque([(start_village, 0)])  # Начинаем с первой деревни и времени 0
    visited = defaultdict(lambda: float('inf'))  # Храним минимальное время прибытия в деревню
    visited[start_village] = 0

    # Переменная для хранения минимального времени до целевой деревни
    min_time = float('inf')

    while queue:
        current_village, current_time = queue.popleft()

        # Проходим по всем рейсам из текущей деревни
        for dep_time, next_village, arr_time in graph[current_village]:
            # Если можем сесть на этот рейс (учитываем расписание)
            if dep_time >= current_time and arr_time < visited[next_village]:
                visited[next_village] = arr_time

                # Если дошли до конечной деревни, обновляем минимальное время
                if next_village == target_village:
                    min_time = min(min_time, arr_time)

                # Добавляем в очередь новый рейс для дальнейшего поиска
                queue.append((next_village, arr_time))

    # Выводим результат
    print(min_time if min_time != float('inf') else -1)

# Запуск решения
solve()
