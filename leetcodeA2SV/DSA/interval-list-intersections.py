class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n,m = len(firstList), len(secondList)
        l,r = 0, 0
        res = []

        while l < n and r < m:
            item1, item2 = firstList[l], secondList[r]
            s1, e1 = item1[0], item1[1]
            s2, e2 = item2[0], item2[1]

            if s1 <= e2 and s2 <= e1:
                res.append([max(s1,s2), min(e1, e2)])

            if e1 < e2:
                l += 1
            elif e1 == e2:
                l += 1
                r += 1
            else:
                r += 1

        return res
                
        

        