class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        
        p = 0
        for i in spaces:
            res += s[p:i] + " "
            p = i
        res += s[p:]
        return res