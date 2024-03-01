class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        def backtrack(i, path):
            if i >= n:
                if path[:] not in ans:
                    ans.append(path[:])
                return 

            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()

            backtrack(i+1, path)

        backtrack(0, [])

        return ans