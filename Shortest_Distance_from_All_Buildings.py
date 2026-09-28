from collections import deque

class Solution:
    def shortestDistance(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        distance = [[0] * cols for _ in range(rows)]
        reach = [[0] * cols for _ in range(rows)]
        buildings = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    buildings += 1
                    queue = deque([(r, c, 0)])
                    visited = [[False] * cols for _ in range(rows)]
                    visited[r][c] = True

                    while queue:
                        x, y, dist = queue.popleft()

                        for dx, dy in directions:
                            nx = x + dx
                            ny = y + dy

                            if (
                                0 <= nx < rows
                                and 0 <= ny < cols
                                and grid[nx][ny] == 0
                                and not visited[nx][ny]
                            ):
                                visited[nx][ny] = True
                                distance[nx][ny] += dist + 1
                                reach[nx][ny] += 1
                                queue.append((nx, ny, dist + 1))

        answer = float("inf")

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and reach[r][c] == buildings:
                    answer = min(answer, distance[r][c])

        return -1 if answer == float("inf") else answer
