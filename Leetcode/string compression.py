class Solution:
    def compress(self, chars: List[str]) -> int:
        l, m = 0,1
        s = ''
        while m < len(chars):
            if chars[l] != chars[m]:
                f = m - l
                if f != 1:
                    s += chars[l] + str(f)
                else:
                    s += chars[l]
                l=m
            m += 1
            
        if (m-l) != 1:
            s += chars[l] + str(m-l)
        else:
            s += chars[l]
        
        for i,j in enumerate(s):
            chars[i] = j

        return len(s)

     
