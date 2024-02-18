class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        rowSkyline = [0]*n
        colSkyline = [0]*m

        for r in range(n):
            rowSkyline[r] = max(grid[r])

        for c in range(m):
            mx = grid[0][c]
            for r in range(n):
                mx = max(mx, grid[r][c])

            colSkyline[c] = mx

        ans = 0
        for r in range(n):
            for c in range(m):
                new = min(rowSkyline[r], colSkyline[c])
                ans += (new - grid[r][c])

        return ans

        