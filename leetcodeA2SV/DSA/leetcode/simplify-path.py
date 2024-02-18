class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        direc = path.split("/")
        for i in direc:
            if i == "..":
                if stack:
                    stack.pop()
            else:
                if i and i != ".":
                    stack.append(i)

        return f"/{'/'.join(stack)}"

            
