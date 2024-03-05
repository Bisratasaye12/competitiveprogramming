class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        f = set(forbidden)
        n = len(word)

        l,r = 0,0
        mx = 0

        while r < n:
            curr = r
            while curr >= l and curr > r - 10:
                if word[curr:r+1] in f:
                    mx = max(mx, r - l)
                    l = curr + 1
                    break
                curr -= 1
                
            r += 1

        mx = max(mx, r-l)

        return mx