class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        sep = [ i for i in s if i!= "-"]
        n = len(sep)

        q,r = n//k, n%k
        ans = []

        if r == 0:
            for i in range(0,n,k):
                ans.append(sep[i:i+k])
        else:
            ans.append(sep[:r])
            for i in range(r,n,k):
                ans.append(sep[i:i + k])

        res = ""
        for item in ans:
            for ch in item:
                res += ch.upper()
            res += "-"

        #print(sep,ans)
        return res[:-1]