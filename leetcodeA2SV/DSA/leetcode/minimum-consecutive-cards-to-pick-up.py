class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        m = n + 1
        r=0
        d = defaultdict(int)

        while r < n:
            if cards[r] not in d:
                d[cards[r]] = r
            else:
                m = min(m, r - d[cards[r]] + 1)
                d[cards[r]] = r

            r += 1





        return m if m <= n else -1