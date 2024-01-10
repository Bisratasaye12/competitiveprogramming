class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, k = len(s2), len(s1)
        if n < k: return False
        h = defaultdict(int)
        for i in s1:
            h[i] += 1

        window = defaultdict(int)
        for i in range(k):
            window[s2[i]] += 1
        if window == h:
            return True

        l = 0
        for r in range(k,n):
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                window.pop(s2[l])

            window[s2[r]] += 1
            if window == h:
                return True
            l += 1

        return False



            