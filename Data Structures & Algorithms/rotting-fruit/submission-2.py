class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = collections.deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i, j, 0])
        max_time = 0
        while q:
            x, y, t = q.popleft()
            max_time = max(max_time, t)
            for dx, dy in directions:
                newX = x + dx
                newY = y + dy
                if 0 <= newX < m and 0 <= newY < n:
                    if grid[newX][newY] == 1:
                        q.append([newX, newY, t + 1])
                        grid[newX][newY] = 2
                        fresh -= 1

        return max_time if fresh == 0 else -1