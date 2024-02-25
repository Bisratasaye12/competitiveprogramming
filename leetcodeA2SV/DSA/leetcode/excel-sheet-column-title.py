class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []

        while columnNumber > 0:
            columnNumber -= 1  
            curr = columnNumber % 26  
            ans.append(chr(curr + ord('A')))  
            columnNumber //= 26  

        return ''.join(ans[::-1])
