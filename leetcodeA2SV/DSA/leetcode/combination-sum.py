class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def backtrack(i, path, s):
            if s[0] >= target:
                if s[0] == target:
                    ans.append(path[:])
                return

            for j in range(i-1, n):
                if j >= 0:
                    path.append(candidates[j])
                    s[0] += candidates[j]
                    backtrack(j + 1 , path, s)
                    path.pop()
                    s[0] -= candidates[j]

        backtrack(0, [], [0])

        return ans

                    
