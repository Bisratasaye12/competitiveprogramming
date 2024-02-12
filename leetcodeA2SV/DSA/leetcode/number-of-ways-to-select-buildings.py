class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        pz = [0]*(n + 1)
        po = [0] *(n + 1)
        count = 0

        for i in range( n):
            if s[i] == "1":
                po[i+1] = po[i] + 1
                pz[i+1] = pz[i]
            else:
                pz[i+1] = pz[i] + 1
                po[i+1] = po[i]

        for i in range(n):
            if s[i] == "0":
                count += (po[i] * (po[-1]-po[i]))
            else:
                count += (pz[i] * (pz[-1]-pz[i]))

        return count