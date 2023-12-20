class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeroes, ones = defaultdict(int), defaultdict(int)
        zc,oc = 0,0
        n = len(nums)

        for i in range(n):
            zeroes[i] = zc
            if nums[i] == 0:
                zc += 1
        zeroes[n] = zc

        ones[n] = 0
        for j in range(n-1, -1,-1):
            if nums[j] == 1:
                oc += 1

            ones[j] = oc

        m = float('-inf')
        for i in zeroes:
            m = max(zeroes[i] + ones[i], m)

        res = []
        for i in zeroes:
            if zeroes[i] + ones[i] == m:
                res.append(i)
        return res
            
