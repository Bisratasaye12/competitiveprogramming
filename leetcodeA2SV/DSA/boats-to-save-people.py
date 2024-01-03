class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people)-1
        people.sort()
        b = 0
        while l <= r:
            if l == r:
                b += 1
                break
            if people[l] + people[r] <= limit:
                b += 1
                l += 1
                r -= 1
            else:
                b += 1
                r -= 1
       
        return b