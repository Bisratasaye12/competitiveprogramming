class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = defaultdict(int), defaultdict(int)
        for i in matches:
            winners[i[0]] += 1
            losers[i[1]] += 1

        answer = [[],[]]
        for i in winners:
            if i not in losers:
                answer[0].append(i)
            
        for i in losers:
            if losers[i] == 1:
                answer[1].append(i)

        answer[0].sort()
        answer[1].sort()
        return answer

