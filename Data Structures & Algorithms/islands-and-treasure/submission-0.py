class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        while q:
            i, j = q.popleft()

            for x, y in directions:
                newX = i + x
                newY = j + y
                if 0 <= newX < m and 0 <= newY < n:
                    if grid[newX][newY] == 2147483647:
                        grid[newX][newY] = grid[i][j] + 1
                        q.append([newX, newY])
