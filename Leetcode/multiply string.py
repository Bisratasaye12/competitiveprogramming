class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if int(num1)>int(num2):
            larg = num1
            sm = num2
        else:
            sm = num1
            larg = num2
            
        temp = [[0] for _ in range(len(sm))]
        
        for i, d in enumerate(sm[::-1]):
            for n in larg[::-1]:
                res = int(d) * int(n)
                t = temp[i].pop()
                r1, q1 = res % 10, res//10
                temp[i] += [r1 + t, q1]
            temp[i] = [0]*i + temp[i]
        stack = []
        final = ''
        for i in range(len(num1) + len(num2) + 1):
            for part in temp:
                if part:
                    stack.append(part.pop(0))
            sums = sum(stack)
            r = sums%10
            q = sums//10
            final += str(r)
            stack = [q]
             
        final = int(final[::-1])   
        return str(final)
