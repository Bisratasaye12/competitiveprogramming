class Solution:
    def frequencySort(self, s: str) -> str:
        counts = defaultdict(int)
        sn = []
        for i in s:
            counts[i] += 1
            sn.append(i)

        sn.sort(key= lambda x:(counts[x], x), reverse= True)
        print(counts,sn)
        return "".join(sn)