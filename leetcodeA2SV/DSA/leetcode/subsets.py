class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(num, subset):
            
            ans.append(subset[:])
                 

            for i in range(num, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

            

        backtrack(0,[])

        return ans

            
                