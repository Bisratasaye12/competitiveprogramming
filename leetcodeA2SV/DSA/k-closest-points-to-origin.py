class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points.sort(key= lambda x: math.sqrt((x[0]**2) + (x[1]**2)))

        res = []
        for i in range(k):
            res.append(points[i])

        return res