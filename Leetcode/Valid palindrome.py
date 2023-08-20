class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        s = s.lower()
        for i in s:
            if i.isalnum():
                t += i

        if t == t[::-1]:
            return True
        else:
            return False
