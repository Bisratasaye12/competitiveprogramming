class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        _max = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r-l)
                l += 1
            else:
                area = height[r] * (r - l)
                r -= 1
            if area > _max:
                _max = area
            
        return _max
