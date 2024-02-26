class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        string = [i for i in s]

        l,r = 0, len(s) - 1

        while l < r:
            if string[r] in vowels and string[l] in vowels:
                string[l], string[r] = string[r], string[l]
                r -= 1
                l += 1
            if string[r] not in vowels:
                r -= 1
            elif string[l] not in vowels:
                l += 1

        return "".join(string)