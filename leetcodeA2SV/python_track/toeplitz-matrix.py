class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n,m = len(matrix), len(matrix[0])
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < m

        for i in range(n):
            r, c = i,0
            target = matrix[r][c]
            nr, nc = r, c
            while inbound(nr,nc):
                if matrix[nr][nc] != target:
                    return False
                nr, nc = nr + 1, nc + 1

        for i in range(m):
            r, c = 0, i
            target = matrix[r][c]
            nr, nc = r, c
            while inbound(nr,nc):
                if matrix[nr][nc] != target:
                    return False
                nr, nc = nr + 1, nc + 1


        return True



         