class Solution:
    def scoreOfParentheses(self, s: str) -> int:
       
        stack = []
        output, r = 0, 0

        for i in s:

            if i == "(":
                stack.append(0)
            elif i == ")":
                mul = stack.pop()
                if mul == 0:
                    r = 1
                else:
                    r = mul * 2

                if not stack:
                    output += r
                else:
                    stack[-1] += r

        return output
