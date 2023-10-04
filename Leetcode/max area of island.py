class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def inbound(r,c):
            return 0<=r<m and 0<=c<n

        dirc = [(0,1),(0,-1),(1,0),(-1,0)]

        count = 0
        visited = set()
        elements = []
        def dfs(r,c):
            if grid[r][c] != 1 or (r,c) in visited:
                return 
            if grid[r][c] == 1:
                visited.add((r,c))
                elements.append((r,c))
            for dr,dc in dirc:
                nr, nc = dr + r, dc + c
                if inbound(nr,nc) and (nr,nc) not in visited and grid[i][j]==1:
                    dfs(nr,nc)
            
        x = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    if len(elements) > x:
                        x = len(elements)
                    elements = []
       
        return x

        
