class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1
        first = nums[0]

        while l < r:
            mid = (l+r)//2

            if nums[mid] < nums[(mid-1)%n] and nums[mid] < nums[(mid+1)%n]:
                return nums[mid]
            elif nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1       



        return nums[l]