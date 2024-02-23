class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        memo = {}

        def paskal(index, n):
            if index == 0:
                return 1
            if index == n - 1:
                return 1

            if (index, n) in memo:
                return memo[(index, n)]

            memo[(index, n)] = paskal(index - 1, n - 1) + paskal(index, n - 1)

            return memo[(index, n)]

        ans = []
        for i in range(rowIndex + 1):
            ans.append(paskal(i, rowIndex + 1))

        return ans
                    
                
            