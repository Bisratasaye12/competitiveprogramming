class Solution:
    def decodeString(self, s: str) -> str:

        def decode(s):
            ans = ""
            prev = 0
            repetitions = 0
            depth = 0  
            for i in range(len(s)):
                if (depth == 0 and s[i].isalpha()):
                    ans += s[i]
                    prev = i + 1
                if s[i] == "[":
                    depth += 1
                    if depth == 1: 
                        repetitions = int(s[prev:i])
                        prev = i + 1
                elif s[i] == "]":
                    depth -= 1
                    if depth == 0:  
                        while repetitions > 0: 
                            ans += decode(s[prev:i])
                            repetitions -= 1
                        prev = i + 1
            return ans

        return decode(s)