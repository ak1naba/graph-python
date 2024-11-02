import numpy as np


def floyd_warshall(adj_matrix):
    # Преобразуем входную матрицу в формат NumPy для удобства
    dist = np.array(adj_matrix, dtype=float)
    n = dist.shape[0]

    # Заменяем 0 на бесконечность, если это не главная диагональ
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = float('inf')

    # Основной цикл алгоритма Флойда
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def longest_shortest_path(adj_matrix):
    # Выполняем алгоритм Флойда
    shortest_paths = floyd_warshall(adj_matrix)

    # Находим самый длинный путь среди кратчайших
    longest_path = 0
    for i in range(len(shortest_paths)):
        for j in range(len(shortest_paths)):
            if shortest_paths[i][j] < float('inf'):
                longest_path = max(longest_path, shortest_paths[i][j])

    return int(longest_path)  # Приводим результат к целому числу


def input_adjacency_matrix():
    print("Введите матрицу смежности (строки через Enter, значения через пробел):")
    adj_matrix = []

    while True:
        line = input()
        if line == "":  # Прекращаем ввод, если строка пустая
            break
        row = list(map(int, line.split()))
        adj_matrix.append(row)

    return adj_matrix


def main():
    adj_matrix = input_adjacency_matrix()
    result = longest_shortest_path(adj_matrix)
    print(result)


if __name__ == "__main__":
    main()
