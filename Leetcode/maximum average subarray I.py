class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        m = k-1
        _sum = sum(nums[:m+1])
        maxavg = _sum / k
        #print(_sum,l,m)
        while m < len(nums):
            if m < len(nums) -1:
                _sum = _sum - nums[l] + nums[m+1]
                avg = _sum/k
                #print(_sum,l,m)
                if avg > maxavg:
                    maxavg = avg
            m += 1
            l += 1

        return maxavg

