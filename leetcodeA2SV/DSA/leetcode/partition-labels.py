class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = defaultdict(int)
        n = len(s)
        for i in range(n):
            ends[s[i]] = i
        res = []

        print(ends)
        i = 0
        while i < n:
            end = ends[s[i]]
            mx = end
            j = i + 1
            while j < end:
                mx = max(mx, ends[s[j]])
                end = mx
                j += 1
            print(mx)
            res.append(mx - i + 1)
            i = mx + 1

        return res

            
