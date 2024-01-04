class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        maxim = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in result:
                    result += s[j]
                else:
                    break

            if len(result) > maxim:
                maxim = len(result)
            result = "" 


           
        return maxim
            


