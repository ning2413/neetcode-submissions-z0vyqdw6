class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(q, visited):
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < m and
                        0 <= ny < n and 
                        (nx, ny) not in visited and
                        board[nx][ny] == 'O'
                    ):
                        q.append((nx, ny))
                        visited.add((nx, ny))

        O_q = collections.deque()
        visited = set()

        for i in range(m):
            if board[i][0] == 'O':
                O_q.append((i, 0))
                visited.add((i, 0))
            if board[i][n - 1] == 'O':
                O_q.append((i, n - 1))
                visited.add((i, n - 1))
        for j in range(n):
            if board[0][j] == 'O':
                O_q.append((0, j))
                visited.add((0, j))
            if board[m - 1][j] == 'O':
                O_q.append((m - 1, j))
                visited.add((m - 1, j))
        bfs(O_q, visited)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'


