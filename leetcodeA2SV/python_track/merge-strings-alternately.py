class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f, s = 0,0
        merged = ''

        while f < len(word1) and s < len(word2):
            merged += (word1[f]  + word2[s])
            f += 1
            s += 1

        if f >= len(word1):
            merged += word2[s:]
        else:
            merged += word1[f:]

        return merged