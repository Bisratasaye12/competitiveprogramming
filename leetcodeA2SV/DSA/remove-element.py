class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        x = float('inf')
        v_count = 0

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = x
                v_count += 1


        nums.sort()
        return len(nums) - v_count
        