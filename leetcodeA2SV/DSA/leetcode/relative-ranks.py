class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = defaultdict(int)

        for i,j in enumerate(score):
            d[j] = i


        ans = [0]*len(score)
        score.sort(reverse= True)

        for i,j in enumerate(score):
            idx = d[j]
            if i == 0:
                ans[idx] = "Gold Medal"
            elif i == 1:
                ans[idx] = "Silver Medal"
            elif i == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(i+1)

        return ans