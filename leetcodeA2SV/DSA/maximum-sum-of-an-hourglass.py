class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        _sum = 0
        def inbound(r,c):
            return 0 <= r < m and 0 <= c < n

        for row in range(m):
            for col in range(n):
                tl, tr, bl, br = (row-1, col-1), (row-1, col +1), (row +1, col-1), (row+1, col+1)
                for t in (tl, tr,bl,br):
                    if not inbound(t[0], t[1]):
                        break
                else:
                    n_sum = grid[tl[0]][tl[1]] + grid[tr[0]][tr[1]] + grid[bl[0]][bl[1]] + grid[br[0]][br[1]] + grid[row-1][col] + grid[row][col] + grid[row+1][col]
                    print(n_sum)
                    _sum = max(_sum, n_sum)


        return _sum
