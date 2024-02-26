class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for letter in ransomNote:
            d1[letter] += 1

        for letter in magazine:
            d2[letter] += 1


        for i in d1:
            if i not in d2 or d1[i] > d2[i]:
                return False
        else:
            return True