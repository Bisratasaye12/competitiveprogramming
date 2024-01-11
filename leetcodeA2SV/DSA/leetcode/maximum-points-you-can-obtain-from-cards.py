class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        t_sum = sum(cardPoints)
        s = 0
        ms =  0

        for i in range(n-k):
            s += cardPoints[i]

        l = 0
        for r in range(n-k, n):
            ms = max(ms, t_sum - s)
            s -= cardPoints[l]
            s += cardPoints[r]
            l += 1


        ms = max(ms, t_sum - s)
        return ms