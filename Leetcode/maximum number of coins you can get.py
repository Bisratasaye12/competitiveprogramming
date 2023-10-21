class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = len(piles) -2
        s = 0
        for i in range(len(piles)//3):
            print(piles[l])
            s += piles[l]
            l -= 2

        return s
