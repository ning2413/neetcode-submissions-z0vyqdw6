class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def bfs(q, visited):
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m and
                        0 <= ny < n and
                        (nx, ny) not in visited and
                        heights[nx][ny] >= heights[x][y]
                    ):
                        q.append((nx, ny))
                        visited.add((nx, ny))
        
        pacificq = collections.deque()
        atlanticq = collections.deque()
        pacific = set()
        atlantic = set()

        for i in range(m):
            pacificq.append((i, 0))
            pacific.add((i, 0))
            atlanticq.append((i, n - 1))
            atlantic.add((i, n - 1))
        for j in range(n):
            pacificq.append((0, j))
            pacific.add((0, j))
            atlanticq.append((m - 1, j))
            atlantic.add((m - 1, j))
        bfs(pacificq, pacific)
        bfs(atlanticq, atlantic)

        return list(pacific & atlantic)
        