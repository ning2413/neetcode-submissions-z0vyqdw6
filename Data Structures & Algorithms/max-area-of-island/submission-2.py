class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        maxArea = 0
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = 0
                    q.append([i, j])
                    grid[i][j] = 0
                    while q:
                        x, y = q.popleft()
                        area += 1
                        for mvX, mvY in directions:
                            newX = x + mvX
                            newY = y + mvY
                            if 0 <= newX < n and 0 <= newY < m:
                                if grid[newX][newY] == 1:
                                    grid[newX][newY] = 0
                                    q.append([newX, newY])
                    maxArea = max(maxArea, area)
        return maxArea

