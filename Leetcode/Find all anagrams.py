class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        pdict = defaultdict(int)
        for i in p:
            pdict[i] += 1
        res = []
        l = 0
        k = len(p)
        if len(s) < k:
            return []
        win = defaultdict(int)
        for i in s[l:k]:
            win[i] += 1
        if win == pdict:
            res.append(l)
        
