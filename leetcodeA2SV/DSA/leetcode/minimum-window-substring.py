class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) > n: return ""
        d = defaultdict(int)
        l,r,mn = 0,0,"a"*(n+1)
        target = Counter(t)
        win = defaultdict(int)
        res = []
        while r < n:
            win[s[r]] += 1

            while l < n and all(key in win and win[key] >= target[key] for key in target):
                res = s[l:r+1]
                if len(res) < len(mn):
                    #print(res, "if")
                    mn = res
                #print(res)
                win[s[l]] -= 1
                if win[s[l]] == 0:
                    win.pop(s[l])
                l += 1
            
            r += 1


        return mn if len(mn) <= n else ""