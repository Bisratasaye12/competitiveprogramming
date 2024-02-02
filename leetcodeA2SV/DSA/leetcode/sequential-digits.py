class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        q1, q2, n1, n2 = low, high, [], []

        while q1 != 0:
            n1.append(q1%10)
            q1 //= 10

        while q2 != 0:
            n2.append(q2%10)
            q2 //= 10

        k = abs(len(n1) - len(n2))
        mn = min(len(n1), len(n2))
        n1, n2 = n1[::-1], n2[::-1]


        for i in range(mn, mn + k + 1):
            l = 1
            
            while l <= 9:
                if l + i <= 10:
                    n = range(l, l+i)
                    if len(n) == i:
                        num = int("".join(map(str, n )))
                        if low <= num <= high:
                            res.append(num)
                        
                l += 1

        res.sort()
        return res
            



        

