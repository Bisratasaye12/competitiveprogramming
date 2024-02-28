class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])

        l,r = 0, (n-1)*m + (m-1)

        while l <= r:
            mid = (l + r) // 2

            nr,nc = mid // m, mid % m

            if matrix[nr][nc] == target:
                return True
            elif matrix[nr][nc] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False