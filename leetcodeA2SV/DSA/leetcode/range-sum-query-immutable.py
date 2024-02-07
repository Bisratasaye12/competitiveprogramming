class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        r = 0
        for i in range(len(nums)):
            r += self.nums[i]
            self.nums[i] = r


    def sumRange(self, left: int, right: int) -> int:
        #print(self.nums)
        if left != 0:
            return self.nums[right] - self.nums[left - 1]
        else:
            return self.nums[right] 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)