class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''

        m, idx = float("inf") , 0
        for i, j in enumerate(strs):
            if m > len(j):
                m = len(j)
                idx = i

        for i in range(len(strs[idx])):

            for string in strs:
                if string[i] != strs[idx][i]:
                    return ans
            else:
                ans += strs[idx][i]

        return ans