class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(float('inf'))
        ans = []

        prev, l, r = 0,0,1

        while r < len(nums):
            if nums[r] - nums[l] > 1:
                ans.append([nums[prev], nums[l]])
                prev = r
            l += 1
            r += 1

        for i, item in enumerate(ans):
            if item[0] == item[1]:
                ans[i] = str(item[0])
            else:
                ans[i] = "->".join(map(str, item))

        return ans
