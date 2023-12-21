class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        sorted_ = sorted(s, key= lambda x : len(x))
        for i in range(len(s)):
            space_len = (len(sorted_[-1]) - len(s[i]))
            s[i] = s[i] + (" " * space_len)
            print(len(s[i]))

        res = []
        for i in range(len(s[-1])):
            curr = ''
            for word in s:
                curr += word[i]
            res.append(curr.rstrip())

        print(s)
        return res