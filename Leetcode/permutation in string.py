class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h = defaultdict(int)
        for i in s1:
            h[i] += 1

        l,k = 0, len(s1)-1
        m = l + k

        window = defaultdict(int)
        while m < len(s2):

            for i in range(l,m+1):
                window[s2[i]] += 1

            if window == h:
                return True
            else:
                window = defaultdict(int)
            l += 1
            m += 1
       
        return False
        
