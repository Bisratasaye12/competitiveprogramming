class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for i in range(1, len(points)):
            p2, p1 = points[i], points[i-1]
            x = abs(p2[0] - p1[0])
            y = abs(p2[1] - p1[1])

            time += max(x,y)

        return time

