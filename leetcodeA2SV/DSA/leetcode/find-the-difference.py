class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = defaultdict(int)
        d2 = defaultdict(int)

        for j in s:
            d[j] += 1

        for i in t:
            d2[i] += 1

        for i in d2:
            if i not in d or d2[i] > d[i]:
                return i
