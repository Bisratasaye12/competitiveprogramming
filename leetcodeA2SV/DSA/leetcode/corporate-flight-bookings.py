class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n

        for s,e,seat in bookings:
            ans[s-1] += seat
            if e < n:
                ans[e] -= seat

        for i in range(1,n):
            ans[i] += ans[i-1]

        return ans
            