class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = 0,0
        odd = 0
        count = 0
        count_subarray = 0

        while r < n:
            if nums[r] % 2:
                odd += 1
                count_subarray = 0
            
            while odd == k:
                if nums[l]%2:
                    odd -= 1
                count_subarray += 1
                l += 1

            count += count_subarray
            r += 1
            
            

        return count