class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort()
        l,r = 0,1
        
        m = 0
        while r < len(points):
            m = max(m, abs(points[r][0] - points[l][0]))
            l += 1
            r += 1

        return m
