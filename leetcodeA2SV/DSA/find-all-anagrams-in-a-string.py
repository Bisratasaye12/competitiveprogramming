class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m = len(s), len(p)
        if n < m: return []
        count = []
        target = defaultdict(int)
        for i in p:
            target[i] += 1

        window = defaultdict(int)
        for i in range(m):
            window[s[i]] += 1
        if window == target:
            count.append(0)

        l = 0
        for r in range(m, n):
            window[s[l]] -= 1
            if window[s[l]] < 1:
                window.pop(s[l])
            window[s[r]] += 1
            l += 1
            if target == window:
                count.append(l)

           
        
        return count
            

