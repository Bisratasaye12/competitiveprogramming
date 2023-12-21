class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        """
        sort nums
        put two pointers 
        using a loop that stops when the second pointer is equal to length of nums
        starting the first for the first pointer and from the second for the second pointer
        move the right pointer if the element is one greater than the previous
        else 
            find the length by subtracting the first pointer from second pointer + 1 
            maximize the length using a variable
            bring the left pointer to the current position
        
        """
        if len(nums) == 0:
            return 0
        _max_len = 0
        l, r = 0,1
        nums =  list(sorted(set(nums)))
        print(nums)
        while r < len(nums):
            if nums[r] - nums[r-1] == 1:
                r += 1
            else:
                _max_len = max(_max_len, r-l)
                print(_max_len)
                l = r
                r += 1
        _max_len = max(_max_len, r-l)

        return _max_len