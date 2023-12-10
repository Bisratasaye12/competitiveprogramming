class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        
        for i,j in enumerate(nums):
            d[j] = i

        for i,j in operations:
            nums[d[i]] = j
            d[j] = d[i]

        return nums