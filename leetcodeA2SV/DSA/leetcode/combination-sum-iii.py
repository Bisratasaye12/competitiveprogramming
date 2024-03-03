class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(i, path, tar):
            if len(path) == k and tar == 0:
                ans.append(path[:])
            if len(path) >= k or tar <= 0:
                return

            prev = -1
            for j in range(i, 10):
                if prev != j:
                    path.append(j)
                    backtrack(j + 1, path, tar - j)
                    path.pop()

                    prev = j

        backtrack(1, [], n)
        return ans


            
                