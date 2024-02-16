class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        ones = 0
        longest = 0

        for i in counts:
            if counts[i] == 1:
                ones += 1
                continue

            if counts[i]%2 == 0:
                longest += counts[i]
            else:
                longest += counts[i] - 1
                ones += 1

        if ones >= 1:
            longest += 1

        return longest
