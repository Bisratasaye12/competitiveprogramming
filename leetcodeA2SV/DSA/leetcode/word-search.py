class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n, m = len(board), len(board[0])
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def backtrack(r, c, path_index):
            if path_index == len(word):
                return True

            for i, j in dirs:
                nr, nc = r + i, c + j

                if (nr, nc) not in visited and inbound(nr, nc) and board[nr][nc] == word[path_index]:
                    visited.add((nr, nc))
                    if backtrack(nr, nc, path_index + 1):
                        return True
                    visited.remove((nr, nc))

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if backtrack(i, j, 1):
                        return True
                    visited.remove((i, j))

        return False
