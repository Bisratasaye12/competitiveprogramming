class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers) 
        p,s = [], [0]*(n+1)

        r = 0
        for i in range(n):
            p.append(r)
            if customers[i] == "N":
                r += 1
        p.append(r)
        
        r = 0
        for j in range(n - 1, -1, -1):
            if customers[j] == "Y":
                r += 1

            s[j] = r
        print(p, s)

        mnidx = 0
        res = [p[0] + s[0]]

        for i in range(1, n+1):
            Sum = p[i] + s[i]
            if Sum < res[mnidx]:
                mnidx = i
            res.append(Sum)

        return mnidx


            