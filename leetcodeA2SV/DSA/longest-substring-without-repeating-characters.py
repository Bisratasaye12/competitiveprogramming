class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1: return 1
        el_to_indices = defaultdict(int)
        l, r = 0, 0
        longest = 0

        while r < n:
            if s[r] in el_to_indices and el_to_indices[s[r]] >= l:
                longest = max(longest, r-l)
                l = el_to_indices[s[r]] + 1
              
            el_to_indices[s[r]] = r
            print(l,r)
            r += 1

        longest = max(longest, r-l)
        #print(el_to_indices)


        return longest

        

