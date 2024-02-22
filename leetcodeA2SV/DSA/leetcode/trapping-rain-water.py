class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        preG, nextG = [0]*n , [0]*n

        mx = 0

        for i in range(n):
            preG[i] = mx
            mx = max(mx, height[i])

        mx = 0
        for i in range(n-1, -1, -1):
            nextG[i] = mx
            mx = max(mx, height[i])
                    
        
        water = 0
        for i in range(n):
            p,n = preG[i], nextG[i]

            tmp = min(p,n) - height[i]
            if tmp > 0:
                water += tmp


        return water