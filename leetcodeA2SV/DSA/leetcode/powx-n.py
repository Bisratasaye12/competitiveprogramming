

class Solution:
    def myPow(self, x: float, n: int) -> float:
        new = abs(n) if n%2 else abs(n)
        if n == 0: return 1
        
        def p(x,n):
            if n <= 1:
                return x
            
            if n%2:
                return x * p(x*x, (n-1)//2)
            else:
                return p(x*x, n//2)

        if n < 0:
            return 1 / p(x,new)
        else:
            return p(x,new)
                    