class Solution:
    def sortSentence(self, s: str) -> str:
        def comparator(s):
            return s[-1]

        s = list(s.split())

        s.sort(key=comparator)
        for i in range(len(s)):
            s[i] = s[i][:-1]


        return " ".join(s)