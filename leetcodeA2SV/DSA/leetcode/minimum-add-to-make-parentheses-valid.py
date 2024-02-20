class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closing = 0

        stack = []

        for i in s:
            if i == "(":
                stack.append(0)
            else:
                if stack:
                    stack.pop()
                else:
                    closing += 1

        return len(stack) + closing
