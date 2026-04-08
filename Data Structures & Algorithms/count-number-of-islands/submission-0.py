class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    q.append([i, j])
                    while q:
                        x, y = q.popleft()
                        grid[x][y] = '0'
                        for _x, _y in directions:
                            newX = x + _x
                            newY = y + _y
                            if 0 <= newX < n and 0 <= newY < m:
                                if grid[newX][newY] == '1':
                                    q.append([newX, newY])
                    count += 1
        return count
