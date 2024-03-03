class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        

        def backtrack(i, path, tar):
            if tar == 0: ans.append(path[:])
            if tar <= 0: return

            prev = -1
            for j in range(i, n):
                if prev != candidates[j]:
                    path.append(candidates[j])
                    backtrack(j+1, path, tar - candidates[j])
                    path.pop()
                
                    prev = candidates[j]

        backtrack(0, [], target)

        return ans
