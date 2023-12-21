class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat), len(mat[0])

        res = []
        row, col, move_up = 0,0,True

        while row < m and col < n:
            if move_up:
                while row > 0 and col < n-1:
                    res.append(mat[row][col])
                    row -= 1
                    col += 1

                res.append(mat[row][col])
                if col == n-1:
                    row += 1                    
                else:
                    col += 1

            else:
                while col > 0 and row < m-1:
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                res.append(mat[row][col])
                if row == m -1:
                    col += 1
                else:
                    row += 1

            move_up = not move_up

        return res



