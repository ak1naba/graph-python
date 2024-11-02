import numpy as np


def floyd_warshall(adj_matrix):
    dist = np.array(adj_matrix, dtype=float)
    n = dist.shape[0]

    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = float('inf')

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def longest_shortest_path(adj_matrix):
    shortest_paths = floyd_warshall(adj_matrix)

    longest_path = 0
    for i in range(len(shortest_paths)):
        for j in range(len(shortest_paths)):
            if shortest_paths[i][j] < float('inf'):
                longest_path = max(longest_path, shortest_paths[i][j])

    return int(longest_path)


def input_adjacency_matrix():
    adj_matrix = []

    while True:
        try:
            line = input()
            row = list(map(int, line.split()))
            adj_matrix.append(row)
        except EOFError:
            break  # Завершаем ввод при получении EOF
        except ValueError:
            print("Пожалуйста, введите только целые числа.")

    return adj_matrix


def main():
    adj_matrix = input_adjacency_matrix()
    result = longest_shortest_path(adj_matrix)
    print(result)


if __name__ == "__main__":
    main()
