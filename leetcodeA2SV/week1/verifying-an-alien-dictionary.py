class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = defaultdict(int)
        for i, j in enumerate(order):
            dictionary[j] = i


        res = []
        for i in words:
            t = []
            for j in i:
                t.append(dictionary[j])
            res.append(t)

        return res == sorted(res)



