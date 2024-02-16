class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        r = 0
        count = 0

        for i in nums:
            while i > r + 1:
                r += r + 1
                count += 1

                if r >= n:
                    return count
            
            r += i
            if r >= n:
                return count

        
        while n > r:
            r += r + 1
            count += 1

        return count



            
