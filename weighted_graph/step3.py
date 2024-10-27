from collections import defaultdict, deque


def solve():
    # Чтение n и t
    n, max_time = map(int, input().strip().split())

    # Создаем граф: для каждой дороги храним (город, время, ограничение по весу)
    graph = defaultdict(list)

    # Читаем все строки дорог из ввода
    while True:
        try:
            line = input().strip()
            if not line:
                break  # Прерываем, если ввода больше нет
            u, v, time, weight_limit = map(int, line.split())
            # Добавляем дороги в обе стороны
            graph[u].append((v, time, weight_limit))
            graph[v].append((u, time, weight_limit))
        except EOFError:
            break  # Прерываем цикл при конце ввода (в случае использования EOF)

    # Функция для проверки, можно ли перевезти груз `weight` за время ≤ max_time
    def can_transport(weight):
        # Очередь для BFS: (город, затраченное время)
        queue = deque([(1, 0)])  # Начинаем с города 1 и времени 0
        visited = [float('inf')] * (n + 1)  # Минимальное время до каждого города
        visited[1] = 0  # Начинаем с города 1

        while queue:
            current_city, current_time = queue.popleft()

            # Проверяем все соседние города
            for neighbor, travel_time, weight_limit in graph[current_city]:
                # Если дорога подходит по весу и время не превышает лимит
                if weight_limit >= weight and current_time + travel_time < visited[neighbor]:
                    visited[neighbor] = current_time + travel_time
                    # Если мы достигли города n, проверяем время
                    if neighbor == n and visited[neighbor] <= max_time:
                        return True
                    queue.append((neighbor, visited[neighbor]))

        # Если мы не смогли добраться до города n за нужное время
        return False

    # Бинарный поиск по весу груза
    left, right = 1, 10 ** 6  # Веса в задаче от 1 до 1_000_000
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_transport(mid):
            answer = mid  # Если груз можно перевезти, обновляем ответ
            left = mid + 1  # Пробуем найти больший вес
        else:
            right = mid - 1  # Иначе уменьшаем вес

    # Выводим максимальный возможный вес
    print(answer)


# Запуск решения
solve()
