from collections import defaultdict, deque

def solve():
    # Чтение n и m
    start_village, target_village = map(int, input().strip().split())

    # Создаем граф для хранения рейсов: {откуда: [(время отправления, куда, время прибытия)]}
    graph = defaultdict(list)
    while True:
        try:
            dep_village, dep_time, arr_village, arr_time = map(int, input().strip().split())
            if dep_time <= arr_time:  # Только корректные рейсы
                graph[dep_village].append((dep_time, arr_village, arr_time))
        except EOFError:
            break

    # Очередь для BFS: (деревня, текущее время, накопленное время)
    queue = deque([(start_village, 0, 0)])  # Начинаем с деревни start_village в 0 минут
    visited = defaultdict(lambda: float('inf'))  # Минимальное время прибытия в деревни
    visited[start_village] = 0

    min_time = float('inf')  # Минимальное время для маршрута до целевой деревни

    while queue:
        current_village, current_time, total_time = queue.popleft()

        # Перебираем все рейсы, отправляющиеся из текущей деревни
        for dep_time, next_village, arr_time in graph[current_village]:
            # Можно ли воспользоваться этим рейсом?
            if dep_time >= current_time and arr_time < visited[next_village]:
                visited[next_village] = arr_time
                # Если добрались до целевой деревни, обновляем минимальное время
                if next_village == target_village:
                    min_time = min(min_time, total_time + (arr_time - current_time))
                else:
                    # Добавляем в очередь следующий рейс
                    queue.append((next_village, arr_time, total_time + (arr_time - current_time)))

    # Выводим результат
    print(min_time if min_time != float('inf') else -1)

# Запуск решения
solve()
