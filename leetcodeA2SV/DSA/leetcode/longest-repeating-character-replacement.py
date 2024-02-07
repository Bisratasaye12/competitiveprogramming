class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,m, length= 0,0,0
        chars = defaultdict(int)

        while m < len(s):
            chars[s[m]] += 1
            while (m - l + 1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1
            length = max((m-l+1), length)
            m += 1

        return length
             