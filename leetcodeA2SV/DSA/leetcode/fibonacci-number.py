class Solution:
    def __init__(self):
        self.memo = {0:0, 1:1}


    def fib(self, n: int) -> int:
        if n < 2:
            return n

        if n in self.memo:
            result = self.memo[n]
        else:
            result = self.fib(n-1) + self.fib(n-2)

        return result
        
        