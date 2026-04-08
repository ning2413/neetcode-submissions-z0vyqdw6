class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * n
        prevRow[-1] = 1 if obstacleGrid[-1][-1] == 0 else 0
        for i in range(m - 1, -1, -1):
            currRow = [0] * n
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] != 1:
                    if j + 1 < n:
                        currRow[j] = currRow[j + 1]
                    currRow[j] += prevRow[j]
                else:
                    currRow[j] = 0
            prevRow = currRow
        return prevRow[0]