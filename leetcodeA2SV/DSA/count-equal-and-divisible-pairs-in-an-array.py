class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indices = []

        for i, num in enumerate(nums):
            indices.append((num,i))

        indices.sort(key=lambda x: x[0])

        count = 0
        for j in range(len(nums)-1):
            l = j+1
            while (l < len(nums)) and indices[j][0] == indices[l][0]:
                if (indices[j][1] * indices[l][1]) % k == 0:
                    #print(indices[j][1] * indices[l][1])
                    count += 1
                l += 1
        print(indices)

        return count