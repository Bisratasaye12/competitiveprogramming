class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp = capacity
        steps = 0

        for i in range(len(plants)):
            if temp - plants[i] >= 0:
                steps += 1
                temp -= plants[i]
            else:
                steps += (2*i + 1)
                temp = capacity - plants[i]

        return steps
