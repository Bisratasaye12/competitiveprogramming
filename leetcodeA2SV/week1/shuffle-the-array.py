class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first, second = nums[:n], nums[n:]
        j = 0
        for i in range(0,2*n - 1,2):
            nums[i] = first[j]
            nums[i+1] = second[j]
            j += 1 
        return nums

