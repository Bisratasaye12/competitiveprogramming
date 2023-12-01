class Solution:
    def interpret(self, command: str) -> str:
        hashmap = {"()": "o", "G":"G", "(al)": "al"}

        ans =''
        for i, j in enumerate(command):
            if command[i] in hashmap:
                ans += hashmap[j]
            else:
                if command[i] == "(":
                    if command[i:i+2] == "()":
                        ans += "o"
                    else:
                        ans += "al"

        return ans

