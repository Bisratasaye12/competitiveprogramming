class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {"(":")", "{":"}", "[":"]"}

        for i in range(len(s)):
            if s[i] in p:
                stack.append(s[i])

            else:
                if not stack:
                    return False

                popped = stack.pop()

                if s[i] != p[popped]:
                    return False

            
        return stack == []
