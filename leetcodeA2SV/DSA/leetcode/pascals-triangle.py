class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = defaultdict(int)

        def paskal(index, n):
            if index == 0:
                return 1
            if index == n - 1 :
                return 1  
            if (index, n) in memo :
                return memo[(index, n)]

            memo[(index, n)] = paskal(index - 1, n - 1) + paskal(index, n-1)
            return memo[(index, n)]

        ans = []

        for i in range(1, numRows+1):
            tmp = [paskal(j,i) for j in range(i)]
            ans.append(tmp)

        return ans
            


        