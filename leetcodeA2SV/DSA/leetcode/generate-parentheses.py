class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def check(bracket):
            stack = []
            for i in bracket:
                if i == "(":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0


        ans = []

        def backtrack(path, op, cl):
            if op >= n and cl >= n:
                ans.append("".join(path[:]))
                return

            if op < n:
                path.append("(")
                backtrack(path, op+1, cl)
                path.pop()
            if cl < op:
                path.append(")")
                backtrack(path, op, cl+1)
                path.pop()

        backtrack([], 0,0)

        return ans
            


            