class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        j = 2*k
        new = []
        for i in range(0,len(s),j):
            new.append(s[i:i+k][::-1])
            new.append(s[i+k: i+j])

        
        return "".join(new)

