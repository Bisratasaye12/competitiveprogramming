class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        def inbound(r,c):
            return 0<=r<n and 0<=c<n
        
        r, c = 0,0
        r1, c1 = 0, n-1
        s = 0
        while inbound(r,c) and inbound(r1, c1):
            if (r,c) != (r1, c1):
                s += (mat[r][c] + mat[r1][c1])
                #print(mat[r][c], mat[r1][c1])
            else:
                s += mat[r][c]
                #print(mat[r][c])
            r, c = r + 1, c + 1
            r1, c1 = r1 + 1, c1 - 1

        return s

