class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prevS, nextS = [-1]*n, [-1]*n

        stack = []
        for i,j in enumerate(heights):

            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()

            if stack:
                prevS[i] = stack[-1]

            stack.append(i)

        stack = []
        for k,l in enumerate(heights):

            while stack and heights[stack[-1]] > l:
                elem = stack.pop()
                nextS[elem] = k

            stack.append(k)


        mxArea = 0
        for i in range(n):
            val = heights[i]
            l = prevS[i] 
            r = nextS[i] if nextS[i] != -1 else n

            area = val * ((r - l - 1) )
            mxArea = max(mxArea, area)

        
        return mxArea