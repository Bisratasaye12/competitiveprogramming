class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        limit = n // 4
        win = Counter(s)
        l,r = 0,0
        mn =  n + 1
        while r < n and l <= r:
            #print(win, target)
            win[s[r]] -= 1
            while l < n and all(win[key] <= limit for key in win):
                mn = min(mn, r - l + 1)
                #print(r,l)
                win[s[l]] += 1
                l += 1
            r += 1

        return mn
        