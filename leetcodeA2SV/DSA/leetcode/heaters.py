class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def minDist(house):
            l,r = 0, len(heaters)-1
            mn = float('inf')

            while l <= r:
                mid = (l+r)//2

                mn = min(mn, abs(heaters[mid] - house))
                if heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid - 1

            return mn

        heaters.sort()
        mxRadius = float('-inf')

        for house in houses:
            mxRadius = max(mxRadius, minDist(house))

        return mxRadius





