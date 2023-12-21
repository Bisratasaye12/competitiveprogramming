class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')
        b = float('inf')
        for i in nums:
            if (a != float('inf') and b != float('inf')) and i > b:
                return True
            if i >= b:
                b = i
            else:
                if i <= a:
                    a = i
                else:
                    b = i
        return False