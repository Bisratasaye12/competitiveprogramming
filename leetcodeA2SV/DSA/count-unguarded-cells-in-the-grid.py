class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        visited = [[0]*n for i in range(m)]
       
        for r, c in walls + guards:
            visited[r][c] = 1
       

        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for (row, col) in guards:
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                while inbound(nr, nc) and visited[nr][nc] != 1:
    
                    visited[nr][nc] = 2
                    nr, nc = nr + dr, nc + dc
        #print(visited)

        res = 0
        for row in range(m):
            for col in range(n):
                if visited[row][col] == 0:
                    #print((row, col))  
                    res += 1

        return res


    