class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gf, c = 0, 0
        g.sort()
        s.sort()
        m = 0

        while gf < len(g) and c < len(s):
            if g[gf] > s[c]:
                c += 1
            else:
                gf += 1
                c += 1
                m += 1

        return m
