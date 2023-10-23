class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)

        for i in range(len(s)):
            last[s[i]] = i

        l = 0
        e = 0
        subs = []
        m = 0
        c = 1
        while l < len(s):
            e = last[s[l]]
            if e > m:
                m = e
            if l == m:
                subs.append(c)
                c = 1
            else:
                c += 1
            l += 1


        return subs
            
