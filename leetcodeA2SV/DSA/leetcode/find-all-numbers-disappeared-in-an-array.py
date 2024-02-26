class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        ans = []
        for i in range(1, len(nums)+1):
            if i not in d:
                ans.append(i)


        return ans