class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        print(counts)
        for i,j in enumerate(s):
            if counts[j] == 1:
                return i

        return -1