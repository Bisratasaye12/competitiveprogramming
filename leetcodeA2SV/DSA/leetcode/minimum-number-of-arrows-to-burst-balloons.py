class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key= lambda x: x[1])
        points.append([float('inf'), float("inf")])
        count = 0
        t = points[0][1]


        for i in range(1, n):
            if points[i][0] > t:
                count += 1
                t = points[i][1]

        return count + 1








