def dfs(x, y, m, n, grid, visited):
    # Направления для движения (вверх, вниз, влево, вправо)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))


def count_fragments(m, n, grid):
    visited = [[False] * n for _ in range(m)]
    fragment_count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.' and not visited[i][j]:
                # Найдена новая компонента связности
                visited[i][j] = True
                dfs(i, j, m, n, grid, visited)
                fragment_count += 1

    return fragment_count


# Ввод данных
M, N = map(int, input().strip().split())
grid = [input().strip() for _ in range(M)]

# Подсчет фрагментов
result = count_fragments(M, N, grid)
print(result)