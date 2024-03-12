class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isValid(capacity):
            day, curr_cap = 1, capacity
            for weight in weights:

                if curr_cap - weight < 0:
                    day += 1
                    curr_cap = capacity

                curr_cap -= weight

            return day <= days

        l,r = max(weights), sum(weights)
        mn = r

        while l <= r:
            mid = (l+r)//2

            if isValid(mid):
                mn = min(mn, mid)
                r = mid - 1
            else:
                l = mid + 1

        return mn
