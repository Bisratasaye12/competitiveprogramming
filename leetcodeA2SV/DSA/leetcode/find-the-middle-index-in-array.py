class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] *(n)
        suff = [0] * (n)

        r = 0
        for i in range(n):
            pre[i] = r
            r += nums[i]

        r = 0
        for i in range(n-1, -1, -1):
            suff[i] = r
            r += nums[i]

        ans = -1
        for j in range(n):
            if pre[j] == suff[j]:
                ans = j
                break
        else:
            return -1
        return ans

