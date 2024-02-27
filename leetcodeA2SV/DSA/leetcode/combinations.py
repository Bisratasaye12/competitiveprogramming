class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = set()
        ans = []
        


        def backtrack(i, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return

            for choice in range(i + 1, n + 1):
                comb.append(choice)
                backtrack(choice, comb)
                comb.pop()

        backtrack(0, [])

        return ans


            
