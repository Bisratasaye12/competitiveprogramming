class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {"a", "e", "i", "o", "u"}
        v_count = 0
        
        for i in range(k):
            if s[i] in vowels:
                v_count += 1
        mx = v_count
        l = 0
        for r in range(k, n):
            if s[l] in vowels:
               v_count -= 1

            if s[r] in vowels:
               v_count += 1

            mx = max(mx, v_count)
            l += 1
        return mx

       
