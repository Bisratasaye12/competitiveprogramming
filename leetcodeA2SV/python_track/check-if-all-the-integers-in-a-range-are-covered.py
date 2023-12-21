class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        inters = set(range(ranges[0][0], ranges[0][1] + 1))

        for i in ranges:
            m = set(range(i[0], i[1]+1))
            print(m)
            inters = inters.union(m)

        print(inters)

        return set(range(left, right+1)) <= inters