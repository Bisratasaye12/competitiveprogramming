class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEatAll(bananas):
            hours = 0

            for pile in piles:
                hours += (math.ceil(pile/bananas))
            return hours <= h

        l,r = 1, max(piles)
        k = r

        while l <= r:
            mid = (l+r)//2

            if canEatAll(mid):
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1

        return k
