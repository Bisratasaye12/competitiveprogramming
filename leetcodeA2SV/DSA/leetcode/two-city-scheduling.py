class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x: x[0] - x[1])
        n = len(costs) // 2
        s = 0

        for i in range(2 * n):
            if i >= n:
                s += costs[i][1]
            else:
                s += costs[i][0]

        return s
