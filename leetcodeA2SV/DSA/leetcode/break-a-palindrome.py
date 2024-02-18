class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1: return ""

        lst = [i for i in palindrome]
        if all(map(lambda x: 1 if x=="a" else 0, lst)):
            lst[-1] = "b"
            return "".join(lst)

        for i in range(n):
            if lst[i] != "a":
                lst[i] = "a"
                break

        if lst == lst[::-1]:
            lst[-1] = "b"
            lst[i] = palindrome[i]


        return "".join(lst)
