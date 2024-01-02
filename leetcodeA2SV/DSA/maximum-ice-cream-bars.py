class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        sorted_costs = [0] * (max(costs) + 1)

        for i in costs:
            sorted_costs[i] += 1
        count = 0

        for i, j in enumerate(sorted_costs):
            
            for k in range(j):
                coins -= i
                if coins < 0:
                    break
                count += 1
                

        return count